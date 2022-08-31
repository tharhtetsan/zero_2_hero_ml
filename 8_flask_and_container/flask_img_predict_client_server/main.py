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
    img_data = request.json["img_data"][0]
    print("img_data:",type(img_data))
    jpg_as_str = str.encode(img_data)
    jpg_original = base64.b64decode(jpg_as_str)
    print("jpg_original:",type(jpg_original))
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    new_img = cv2.imdecode(jpg_as_np, flags=1)
    
    result = modelwork.predict_img_by_arr(img=new_img)
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