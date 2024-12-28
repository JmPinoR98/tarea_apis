from fastapi import FastAPI, HTTPException
from controllers.prediction_controllers import PredictionInput
from models.models import get_model

app = FastAPI()
data = {}
pred_meaning = {
    0: "No es un proceso problematico",
    1: "Es un proceso problematico"
}

@app.get('/predictions')
def get_predictions():
    return {
        "message": "Se retorna el historico de predicciones",
        "data": data
    }

@app.get('/predictions/{id_prediction}')
def get_predictions(id_prediction: int):
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"Id = {id_prediction} not found")
    return {
        "message": f"Se retorna el registro con id = {id_prediction}",
        "data": data[id_prediction]
    }

@app.post('/predict')
def set_prediction(prediction_input: PredictionInput):
    prediction = get_model().predict([[
        prediction_input.uso_cpu, 
        prediction_input.uso_memoria, 
        prediction_input.tiempo_ejecucion, 
        float(prediction_input.tipo_proceso_aplicacion), 
        float(prediction_input.tipo_proceso_servicio), 
        float(prediction_input.tipo_proceso_sistema)
    ]]).tolist()
    id = len(data) + 1
    data[id] = {
        "data": {
            "uso_cpu":prediction_input.uso_cpu, 
            "uso_memoria":prediction_input.uso_memoria, 
            "tiempo_ejecucion":prediction_input.tiempo_ejecucion, 
            "tipo_proceso_aplicación":prediction_input.tipo_proceso_aplicacion, 
            "tipo_proceso_servicio":prediction_input.tipo_proceso_servicio, 
            "tipo_proceso_sistema":prediction_input.tipo_proceso_sistema
        },
        "prediccion": prediction[0]
    }
    return {
        "message": "Prediccion Exitosa",
        "data": {
            "id": id,
            "uso_cpu":prediction_input.uso_cpu, 
            "uso_memoria":prediction_input.uso_memoria, 
            "tiempo_ejecucion":prediction_input.tiempo_ejecucion, 
            "tipo_proceso_aplicación":prediction_input.tipo_proceso_aplicacion, 
            "tipo_proceso_servicio":prediction_input.tipo_proceso_servicio, 
            "tipo_proceso_sistema":prediction_input.tipo_proceso_sistema
        },
        "prediccion": pred_meaning[prediction[0]]
    }

@app.put('/predict/{id_prediction}')
def set_prediction(id_prediction: int,prediction_input: PredictionInput):
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"Id = {id_prediction} not found")
    prediction = get_model().predict([[
        prediction_input.uso_cpu, 
        prediction_input.uso_memoria, 
        prediction_input.tiempo_ejecucion, 
        float(prediction_input.tipo_proceso_aplicacion), 
        float(prediction_input.tipo_proceso_servicio), 
        float(prediction_input.tipo_proceso_sistema)
    ]]).tolist()
    data[id_prediction] = {
        "data": {
            "uso_cpu":prediction_input.uso_cpu, 
            "uso_memoria":prediction_input.uso_memoria, 
            "tiempo_ejecucion":prediction_input.tiempo_ejecucion, 
            "tipo_proceso_aplicación":prediction_input.tipo_proceso_aplicacion, 
            "tipo_proceso_servicio":prediction_input.tipo_proceso_servicio, 
            "tipo_proceso_sistema":prediction_input.tipo_proceso_sistema
        },
        "prediccion": prediction[0]
    }
    return {
        "message": f"Se ha actualizado la Prediccion para el id = {id_prediction} exitosamente",
        "data": {
            "id": id_prediction,
            "uso_cpu":prediction_input.uso_cpu, 
            "uso_memoria":prediction_input.uso_memoria, 
            "tiempo_ejecucion":prediction_input.tiempo_ejecucion, 
            "tipo_proceso_aplicación":prediction_input.tipo_proceso_aplicacion, 
            "tipo_proceso_servicio":prediction_input.tipo_proceso_servicio, 
            "tipo_proceso_sistema":prediction_input.tipo_proceso_sistema
        },
        "prediccion": pred_meaning[prediction[0]]
    }

@app.delete('/delete/{id_prediction}')
def delete_prediction(id_prediction: int):
    if id_prediction not in data.keys():
        raise HTTPException(status_code=404, detail=f"Id = {id_prediction} not found")
    data.pop(id_prediction)
    return {
        "message": f"Se ha eliminado del historial la Prediccion para el id = {id_prediction} exitosamente",
    }