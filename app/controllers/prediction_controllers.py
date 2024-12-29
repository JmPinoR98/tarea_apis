from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    """
    Clase para estructurar y validar los datos necesarios para la predicción.
    """
    uso_cpu: float = Field(..., ge=0, le=1, description='Porcentaje de uso de CPU (0 a 1)')
    uso_memoria: float = Field(..., ge=0, le=1, description='Porcentaje de uso de Memoria (0 a 1)')
    tiempo_ejecucion: float = Field(..., ge=0, le=1, description='Tiempo de Ejecucion')
    tipo_proceso_aplicacion: int = Field(..., description='Tipo de Proceso - Aplicacion - (0, 1)')
    tipo_proceso_servicio: int = Field(..., description='Tipo de Proceso - Servicio - (0, 1)')
    tipo_proceso_sistema: int = Field(..., description='Tipo de Proceso - Sistema - (0, 1)')