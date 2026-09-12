# Imagen base oficial de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Comando por defecto al ejecutar el contenedor
CMD ["python", "pruebas.py"]
