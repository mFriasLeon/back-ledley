FROM python:3.11-slim

# Instalar poetry
RUN pip install --no-cache-dir poetry

# Configurar poetry para no usar entornos virtuales
ENV POETRY_VIRTUALENVS_CREATE=false

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . .

# Instalar dependencias
RUN poetry install --no-interaction --no-ansi --no-root


# Exponer el puerto (opcional)
EXPOSE 8000

# Comando por defecto al arrancar el contenedor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

