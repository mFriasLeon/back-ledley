FROM python:3.11-slim

# Instalar poetry
RUN pip install --no-cache-dir poetry

# Configurar poetry para no usar venv
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Copiar archivos de poetry e instalar dependencias
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-interaction --no-ansi

# Copiar el resto del código
COPY . /app/

# Exponer puerto (opcional)
EXPOSE 8000

# Comando por defecto
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
