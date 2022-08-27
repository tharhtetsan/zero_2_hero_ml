from flask import Flask,request
from model_work import modelWork

app = Flask(__name__)

@app.get("/")
def homePage():
    return "Hello this v0.0.0.1...."

@app.post("/predict")
def predict_img():
    request_data = request.json
    img_path = request_data["img_path"]
    result = modelwork.predict_img(img_path=img_path)
    return result

    
modelwork = modelWork()
modelwork.load_model()

app.run(debug=False, host="0.0.0.0",port = 8080)