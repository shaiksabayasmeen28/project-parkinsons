import os
import pandas as pd
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, send_from_directory
from tensorflow.keras.preprocessing import image
from keras.models import load_model

app = Flask(__name__)


Classes=['Based on the spiral image produced above you are healthy,proven with a model accuracy of','Based on the spiral image produced above, you are detected with Parkinsons disease with the model accuracy of']

print(Classes)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images",filename)

@app.route("/upload",methods=["POST","GET"])
def upload():
    if request.method=='POST':
        print("hdgkj")
        m = int(request.form["alg"])
        acc = pd.read_csv("Acc.csv")


        myfile = request.files['file']
        fn = myfile.filename
        mypath = os.path.join("images/", fn)
        myfile.save(mypath)

        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)

        if m==1:
            print("bv2")
            new_model = load_model('models\Mobilenet.h5')
            test_image = image.load_img(mypath, target_size=(256, 256))
            test_image = image.img_to_array(test_image)
            test_image/=255
            a = acc.iloc[m - 1, 1]

        elif m==2:
            print("bv2")
            new_model = load_model(r'C:\Users\0618\Documents\projects\FEB\TK141036-JASHVITHA-PARKINSON’S DISEASE DETECTION USING DEEP LEARNING TECHNIQUES\CODE\Backend\CNN.h5')
            test_image = image.load_img(mypath, target_size=(256, 256))
            test_image = image.img_to_array(test_image)
            test_image/=255
            a = acc.iloc[m - 1, 1]

        elif m==3:
            print("bv2")
            new_model = load_model(r'C:\Users\0618\Documents\projects\FEB\TK141036-JASHVITHA-PARKINSON’S DISEASE DETECTION USING DEEP LEARNING TECHNIQUES\CODE\Backend\resenet50.h5')
            test_image = image.load_img(mypath, target_size=(256, 256))
            test_image = image.img_to_array(test_image)
            test_image/=255
            a = acc.iloc[m - 1, 1]

        test_image = np.expand_dims(test_image,axis=0)
        result = new_model.predict(test_image)
        preds = Classes[np.argmax(result)]

     
        return render_template("result.html", text=preds, image_name=fn, a=round(a * 100, 3))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)