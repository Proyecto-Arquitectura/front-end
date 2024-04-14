# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt y los instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto de los archivos de tu proyecto
COPY . .

# Comando para iniciar el servidor web
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
