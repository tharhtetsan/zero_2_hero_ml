from flask import Flask,request


@app.get("/")
def homePage():
    return "Hello this v0.0.0.1...."

@app.post("/predict")
def predict_img():
    request_data = request.json
    img_path = request_data["img_path"]
    