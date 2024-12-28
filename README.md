# ML API Project

Este proyecto contiene una API desarrollada con FastAPI que permite realizar predicciones usando un modelo de Machine Learning. La API incluye funcionalidades CRUD (Create, Read, Update, Delete) para gestionar las predicciones almacenadas en una base de datos simulada (lista Python).

## Estructura del proyecto
```
/app
  ├── controllers/
  │     └── prediction_controllers.py
  ├── models/
  │     └── models.py
  ├── main.py
  ├── requirements.txt
  └── Dockerfile
```

### Descripción de los archivos principales

- **controllers/prediction_controllers.py**: Contiene las rutas de la API para interactuar con el modelo y la base de datos simulada.
- **models/models.py**: Define los esquemas de datos, la base de datos simulada y la función para cargar el modelo ML.
- **main.py**: Archivo principal que inicia la aplicación e incluye las rutas del controlador.
- **modelo_ml.pkl**: Archivo serializado del modelo de Machine Learning.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **Dockerfile**: Archivo para containerizar la aplicación.

## Requisitos previos

1. **Instalar Docker**:
   - [Guía de instalación](https://docs.docker.com/get-docker/).

2. **Modelo de Machine Learning**:
   - Debes tener un archivo `model.pkl` previamente entrenado y guardado en el directorio principal del proyecto.

3. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```

---

## Instrucciones para ejecutar el proyecto

### 1. Construir la imagen Docker
Ejecuta el siguiente comando desde el directorio principal (donde se encuentra el `Dockerfile`):
```bash
docker build -t ml-api .
```

### 2. Ejecutar el contenedor
Inicia el contenedor con el siguiente comando:
```bash
docker run -d -p 8000:8000 ml-api
```
Esto expondrá la API en el puerto `8000` de tu máquina local.

### 3. Verificar que el contenedor está corriendo
Para confirmar que el contenedor está en ejecución, usa:
```bash
docker ps
```
Deberías ver el contenedor con el nombre de la imagen `ml-api`.

---

## Uso de la API

### Endpoints disponibles

1. **GET** `/predictions`:
   - Obtiene todas las predicciones almacenadas.
   - Ejemplo:
     ```bash
     curl -X GET http://localhost:8000/predictions
     ```

2. **GET** `/predictions/{id}`:
   - Obtiene una predicción por su ID.
   - Ejemplo:
     ```bash
     curl -X GET http://localhost:8000/predictions/1
     ```

3. **POST** `/predictions`:
   - Realiza una nueva predicción y la almacena.
   - Datos de entrada (JSON):
     ```json
     {
        "uso_cpu": 0.8,
        "uso_memoria": 0.4,
        "tiempo_ejecucion": 0.9,
        "tipo_proceso_aplicacion": 0,
        "tipo_proceso_servicio": 1,
        "tipo_proceso_sistema": 0
    }
     ```
   - Ejemplo:
     ```bash
     curl -X POST -H "Content-Type: application/json" \
     -d '{"uso_cpu": 0.8,"uso_memoria": 0.4,"tiempo_ejecucion": 0.9,"tipo_proceso_aplicacion": 0,"tipo_proceso_servicio": 1,"tipo_proceso_sistema": 0}' \
     http://localhost:8000/predictions
     ```

4. **PUT** `/predictions/{id}`:
   - Actualiza una predicción existente por ID.
   - Datos de entrada (JSON):
     ```json
     {
        "uso_cpu": 0.8,
        "uso_memoria": 0.4,
        "tiempo_ejecucion": 0.9,
        "tipo_proceso_aplicacion": 0,
        "tipo_proceso_servicio": 1,
        "tipo_proceso_sistema": 0
    }
     ```
   - Ejemplo:
     ```bash
     curl -X PUT -H "Content-Type: application/json" \
     -d '{"uso_cpu": 0.8,"uso_memoria": 0.4,"tiempo_ejecucion": 0.9,"tipo_proceso_aplicacion": 0,"tipo_proceso_servicio": 1,"tipo_proceso_sistema": 0}' \
     http://localhost:8000/predictions/1
     ```

5. **DELETE** `/predictions/{id}`:
   - Elimina una predicción por su ID.
   - Ejemplo:
     ```bash
     curl -X DELETE http://localhost:8000/predictions/1
     ```

---

## Detener y eliminar contenedores

### Detener el contenedor
Para detener el contenedor en ejecución:
```bash
docker stop <container_id>
```

### Eliminar el contenedor
Para eliminar el contenedor detenido:
```bash
docker rm <container_id>
```

### Eliminar la imagen Docker
Si deseas eliminar la imagen creada:
```bash
docker rmi ml-api
```

## Contacto
Si tienes preguntas o necesitas soporte, contacta al desarrollador del proyecto.

