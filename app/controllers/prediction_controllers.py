from pydantic import BaseModel

class PredictionInput(BaseModel):
    uso_cpu: float
    uso_memoria: float
    tiempo_ejecucion: float
    tipo_proceso_aplicacion: int
    tipo_proceso_servicio: int
    tipo_proceso_sistema: int