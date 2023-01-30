from flask import Flask, request, jsonify, render_template
import tensorflow.keras.applications as kapp
import tensorflow.keras.preprocessing.image as kimage
import tensorflow.keras.models as kmodels
import numpy as np
import tensorflow.keras.utils as utils
from anchor import *

app = Flask(__name__)

vgg_model = kapp.VGG16(weights='imagenet', include_top=False)
model = kmodels.Model(inputs=vgg_model.input, outputs=vgg_model.get_layer('block5_pool').output)

def get_image_feature(img_path):
    img = utils.load_img(img_path, target_size=(224, 224))
    img = utils.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = kapp.vgg16.preprocess_input(img)
    features = model.predict(img)
    features = features.flatten()
    return features

@app.route("/")
def similarity_image():
    q, p_path, h_path, sim = random_sim()
    return render_template('sim_img.html', q=q, p_path=p_path, h_path=h_path, sim=sim)

@app.route("/sim_test", methods=["POST"])
def sim_test():
    p_path = str(request.form['p_path'])
    sim = float(request.form['sim'])
    return render_template('sim_test.html', p_path=p_path, sim=sim)

@app.route("/image-similarity", methods=["POST"])
def image_similarity():
    f = request.files['file']
    img_path = 'D:/k-digital/source/web_mk2/similarity/static/img/similarity/img.jpg'
    f.save(img_path)
    p_path = str(request.form['p_path'])
    sim = float(request.form['sim'])

    features1 = get_image_feature(p_path)
    features2 = get_image_feature(img_path)

    cosine_similarity = np.dot(features1, features2) / (np.linalg.norm(features1) * np.linalg.norm(features2))
    print(cosine_similarity)
    if cosine_similarity >= sim:
        return render_template('success.html')
    else:
        return render_template('fail.html')

if __name__ == "__main__":
    app.run()