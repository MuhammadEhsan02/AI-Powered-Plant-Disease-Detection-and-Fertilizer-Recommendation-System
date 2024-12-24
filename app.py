from flask import Flask, render_template, redirect, request
import os
import torch
import torchvision.transforms.functional as TF
from PIL import Image
import pandas as pd
import numpy as np
import CNN

disease_info = pd.read_csv(r'C:\Users\ehsan\Desktop\Plant Disease\code_files\disease_info.csv', encoding='latin-1')
supplement_info = pd.read_csv(r'C:\Users\ehsan\Desktop\Plant Disease\code_files\supplement_info.csv', encoding='latin-1')

model = CNN.CNN(38)
model.load_state_dict(torch.load(r'C:\Users\ehsan\Desktop\Plant Disease\code_files\Plant_Disease_Detection_Model.pth', map_location=torch.device('cpu')))
model.eval()

def prediction(path_image):
    image = Image.open(path_image)
    image = image.resize((224,224), Image.Resampling.NEAREST)
    input_data = TF.to_tensor(image)
    input_data = input_data.view(-1,3,224,224)
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/contact")
def contact_page():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engin_page():
    return render_template('index.html')

@app.route('/base')
def modile_device_detected_page():
    return render_template('base.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/upload' + filename)
        image.save(file_path)
        print(file_path)
        pred = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description =disease_info['description'][pred]
        prevent = disease_info['Possible Steps'][pred]
        image_url = disease_info['image_url'][pred]
        supplement_name = supplement_info['supplement name'][pred]
        supplement_image_url = supplement_info['supplement image'][pred]
        supplement_buy_link = supplement_info['buy link'][pred]
        return render_template('submit.html' , title = title , desc = description , prevent = prevent , 
                               image_url = image_url , pred = pred ,sname = supplement_name ,
                                 simage = supplement_image_url , buy_link = supplement_buy_link)


@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', supplement_image = list(supplement_info['supplement image']),
                           supplement_name = list(supplement_info['supplement name']), 
                           disease = list(disease_info['disease_name']), buy = list(supplement_info['buy link']))



if __name__ == "__main__":
    app.run(debug=True)