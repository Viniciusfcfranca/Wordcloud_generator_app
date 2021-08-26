from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
import io
import base64
from PIL import Image
import json
import biblioteca1

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("test.html")

@app.route('/predict', methods = ['POST'])
def predict():
    features = [x for x in request.form.values()]
    x = features[0]
    y = features[1]

    a = biblioteca1.wordcloud1(data=x, language= y)
    a.graph() 

    im = Image.open("tmp/wordcloud.png")
    data = io.BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    
    return render_template("test.html", img_data=encoded_img_data.decode('utf-8'))

if __name__ == "__main__":
    app.run()
