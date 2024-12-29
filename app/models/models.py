import pickle

def get_model(file_path: str):
    """
    Carga un modelo de Machine Learning desde un archivo .pkl.

    Args:
        file_path (str): Ruta al archivo .pkl que contiene el modelo.

    Returns:
        object: Modelo deserializado listo para usar.
    """
    with open(file_path, "rb") as f:
        model = pickle.load(f)
    return model