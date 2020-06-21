## Entorno virtual
Crear entorno de virtualización para dependencias
> `virtualenv venv -p python3`

Ejecutar entorno de virtualización para dependencias
> `source venv/bin/activate`

Desactivar entorno de virtualización para dependencias
> `deactivate`

## Frezear e instalar dependencias
Freezear dependencias en archivo requirements
> `pip freeze > requirements.txt`

Instalar dependencias 
> `pip install -r requirements.txt`

## Alembic
Iniciar alembic
> `alembic init app`