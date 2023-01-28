from flask import Flask, request, jsonify
import tensorflow.keras.applications as kapp
import tensorflow.keras.preprocessing.image as kimage
import tensorflow.keras.models as kmodels
import numpy as np
import tensorflow.keras.utils as utils

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

@app.route("/similarity_test", methods=["POST"])
def similarity_test():
    

@app.route("/image-similarity", methods=["POST"])
def image_similarity():
    img1_path = request.json['img1_path']
    img2_path = request.json['img2_path']

    features1 = get_image_feature(img1_path)
    features2 = get_image_feature(img2_path)

    cosine_similarity = np.dot(features1, features2) / (np.linalg.norm(features1) * np.linalg.norm(features2))
    return jsonify({"similarity": cosine_similarity})

if __name__ == "__main__":
    app.run()