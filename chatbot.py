from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
import en_core_web_md
nlp = en_core_web_md.load()
# Creating ChatBot Instance
CB = ChatBot('ChatBot')
 # Training with Personal Ques & Ans
conversation = [
    "Hi",
    "Hi there, Do you want to run a Standard Report, Press Yes!",
    "Yes",
    "Thank You,Please mention the report name in Capital Letters",
    "STANDARDQUITFORLIFE",
    "Please mention the Policy Number",
    "0012345",
    "Please mention the Start Date in mmddyyyy format",
    "01012020",
    "Please mention the End Date in mmddyyyy format",
    "01312020",
    "Thank you for your Inputs, Your report will run shortly, Please check in the output folder",
    "Thank You",
    "Thank you , Have a Great Day ahead!"
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
#trainer_corpus.train('chatterbot.corpus.english')


'''
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(CB.get_response(userText))
app.run(debug = True,port=5003)
'''