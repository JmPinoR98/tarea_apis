import pickle

def get_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model