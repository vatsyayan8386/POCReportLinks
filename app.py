from flask import Flask, render_template, url_for, flash, redirect, session, Blueprint
from sklearn.externals import joblib
from flask import request
import numpy as np
import os
from chatbot import CB
import spacy
import en_core_web_md
nlp = en_core_web_md.load()

from flask_session import Session
app = Flask(__name__, template_folder='template',static_folder='static')

dir_path = os.path.dirname(os.path.realpath(__file__))

#@app.route('/Files/<path:filename>')
#def download(filename):
 #   return send_from_directory(directory='Files', filename=filename)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/AbbvieDM_password")
def AbbvieDM_password():
    return render_template("AbbvieDM_password.html")



@app.route("/AbbvieDM")
def AbbvieDM():
    return render_template("AbbvieDM.html")

@app.route("/AcuityBrandsWellness_password")
def AcuityBrandsWellness_password():
    return render_template("AcuityBrandsWellness_password.html")

@app.route("/AcuityBrandsWellness")
def AcuityBrandsWellness():
    # if form.validate_on_submit():
    return render_template("AcuityBrandsWellness.html")

@app.route("/ApexToolHCCR_password")
def ApexToolHCCR_password():
    # if form.validate_on_submit():
    return render_template("ApexToolHCCR_password.html")

@app.route("/ApexToolHCCR")
def ApexToolHCCR():
    # if form.validate_on_submit():
    return render_template("ApexToolHCCR.html")

@app.route("/MastercardWellness_password")
def MastercardWellness_password():
    return render_template("MastercardWellness_password.html")

@app.route("/MastercardWellness")
def MastercardWellness():
    return render_template("MastercardWellness.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)