# Imagen base
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto (Flask por defecto usa el 5000)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "main.py"]
