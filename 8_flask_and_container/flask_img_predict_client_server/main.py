from flask import Flask,request
from model_work import modelWork
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.get("/")
def homePage():
    return "Hello this v0.0.0.1...."

@app.post("/predict_img")
def test_method():
    img_data = request.json["img_data"]
    jpg_as_np = np.frombuffer(img_data, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    print(img)
    return "ok"
    result = modelwork.predict_img_by_arr(img=img_data)
    return result


@app.post("/predict_imgurl")
def predict_img():
    request_data = request.json
    img_path = request_data["img_path"]
    result = modelwork.predict_img_by_path(img_path=img_path)
    return result

    
modelwork = modelWork()
modelwork.load_model()

app.run(debug=False, host="0.0.0.0",port = 8080)