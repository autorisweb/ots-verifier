# Verificador de Estampillas OpenTimestamps

Este microservicio permite verificar si un hash SHA-256 fue registrado en la blockchain utilizando el protocolo OpenTimestamps (OTS).

## ¿Para qué sirve?

Sirve para comprobar que un archivo (cualquiera) fue registrado en una fecha determinada, brindando prueba de existencia digital sin revelar su contenido.

## ¿Cómo funciona?

Se envía un hash en formato SHA-256 mediante una petición `POST` y el sistema devuelve si la estampilla existe, si está pendiente o si aún no ha sido anclada en la blockchain.

## Endpoint

### `POST /verify`

#### Cuerpo esperado:
```json
{
  "hash": "aca_va_el_hash"
}
