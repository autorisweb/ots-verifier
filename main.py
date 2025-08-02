import subprocess
import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/verify", methods=["POST"])
def verify():
    if 'file' not in request.files:
        return jsonify({"error": "Archivo no enviado"}), 400

    file = request.files['file']

    if not file.filename.endswith(".ots"):
        return jsonify({"error": "El archivo debe tener extensión .ots"}), 400

    filepath = f"/tmp/{file.filename}"
    file.save(filepath)

    try:
        result = subprocess.run(["ots", "verify", filepath], capture_output=True, text=True)
        output = result.stdout
        if result.returncode == 0:
            return jsonify({"valid": True, "details": output})
        else:
            return jsonify({"valid": False, "details": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
