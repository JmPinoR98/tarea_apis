from fastapi import FastAPI, HTTPException
from controllers.prediction_controllers import PredictionInput
from models.models import get_model

# Inicialización de la aplicación de FastAPI
app = FastAPI()

# Historial de predicciones
data = {}

# Traducción de resultados de predicción
pred_meaning = {
    0: "No es un proceso problemático",
    1: "Es un proceso problemático"
}

# Métodos GET para el historial de predicciones
@app.get("/predictions")
def get_predictions():
    """
    Devuelve el historial completo de predicciones.
    """
    return {
        "message": "Se retorna el histórico de predicciones",
        "data": data
    }

@app.get("/predictions/{id_prediction}")
def get_prediction_by_id(id_prediction: int):
    """
    Devuelve una predicción específica basada en su ID.
    """
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"ID = {id_prediction} no encontrado")
    
    return {
        "message": f"Se retorna el registro con ID = {id_prediction}",
        "data": data[id_prediction]
    }

@app.post("/predict")
def set_prediction(prediction_input: PredictionInput):
    """
    Realiza una predicción utilizando el modelo y guarda el resultado en el historial.
    """
    # Realizar predicción
    prediction = model.predict([[
        prediction_input.cpu_usage,
        prediction_input.memory_usage,
        prediction_input.execution_time,
        float(prediction_input.process_type_application),
        float(prediction_input.process_type_service),
        float(prediction_input.process_type_system)
    ]]).tolist()
    
    # Generar un ID único para la predicción
    id = len(data) + 1
    
    # Guardar la predicción en el historial
    data[id] = {
        "data": {
            "cpu_usage": prediction_input.cpu_usage,
            "memory_usage": prediction_input.memory_usage,
            "execution_time": prediction_input.execution_time,
            "process_type_application": prediction_input.process_type_application,
            "process_type_service": prediction_input.process_type_service,
            "process_type_system": prediction_input.process_type_system
        },
        "prediction": prediction[0]
    }
    
    # Retornar la respuesta
    return {
        "message": "Predicción exitosa",
        "data": {
            "id": id,
            "cpu_usage": prediction_input.cpu_usage,
            "memory_usage": prediction_input.memory_usage,
            "execution_time": prediction_input.execution_time,
            "process_type_application": prediction_input.process_type_application,
            "process_type_service": prediction_input.process_type_service,
            "process_type_system": prediction_input.process_type_system
        },
        "prediction": pred_meaning[prediction[0]]
    }

@app.put("/predict/{id_prediction}")
def update_prediction(id_prediction: int, prediction_input: PredictionInput):
    """
    Actualiza los datos y la predicción de una entrada existente en el historial.
    """
    # Verificar si el ID existe en el historial
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"ID = {id_prediction} no encontrado")

    # Realizar la predicción con los nuevos datos
    prediction = model.predict([[
        prediction_input.cpu_usage,
        prediction_input.memory_usage,
        prediction_input.execution_time,
        float(prediction_input.process_type_application),
        float(prediction_input.process_type_service),
        float(prediction_input.process_type_system)
    ]]).tolist()
    
    # Actualizar la predicción en el historial
    data[id_prediction] = {
        "data": {
            "cpu_usage": prediction_input.cpu_usage,
            "memory_usage": prediction_input.memory_usage,
            "execution_time": prediction_input.execution_time,
            "process_type_application": prediction_input.process_type_application,
            "process_type_service": prediction_input.process_type_service,
            "process_type_system": prediction_input.process_type_system
        },
        "prediction": prediction[0]
    }
    
    # Retornar la respuesta
    return {
        "message": f"Predicción actualizada para el ID = {id_prediction} exitosamente",
        "data": {
            "id": id_prediction,
            "cpu_usage": prediction_input.cpu_usage,
            "memory_usage": prediction_input.memory_usage,
            "execution_time": prediction_input.execution_time,
            "process_type_application": prediction_input.process_type_application,
            "process_type_service": prediction_input.process_type_service,
            "process_type_system": prediction_input.process_type_system
        },
        "prediction": pred_meaning[prediction[0]]
    }

@app.delete("/delete/{id_prediction}")
def delete_prediction(id_prediction: int):
    """
    Elimina una predicción del historial basada en su ID.
    """
    # Verificar si el ID existe en el historial
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"ID = {id_prediction} no encontrado")

    # Eliminar la predicción del historial
    data.pop(id_prediction)
    
    # Retornar la respuesta
    return {
        "message": f"Predicción para el ID = {id_prediction} eliminada exitosamente del historial",
    }