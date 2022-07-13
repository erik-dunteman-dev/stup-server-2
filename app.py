# Init is ran on server startup
def init():
    global model

# Inference is ran for every server call
def inference(model_inputs:dict) -> dict:
    global model

    model_inputs["hello"] = "world"

    return model_inputs
