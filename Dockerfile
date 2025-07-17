# 1. Imagen base de Python
FROM python:3.13

# 2. Establecer el directorio de trabajo
WORKDIR /app
# 3. Copiar los archivos del proyecto
COPY . /app

RUN apt-get update && apt-get install -y netcat-openbsd
# 4. Instalar las dependencias del proyecto
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

#dar permiso a los archivos 
RUN chmod +x entrypoint.sh
# 5. Exponer el puerto en el que corre Django
EXPOSE 8000
# 6. Comando para iniciar el servidor de desarrollo de Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 7. Comando para ejecutar el script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]