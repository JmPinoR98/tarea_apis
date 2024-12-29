# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de la aplicación al contenedor
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY controllers/ /app/controllers/
COPY models/ /app/models/

# Instalar las dependencias necesarias desde requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exponer el puerto 8000 para que la aplicación sea accesible
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]