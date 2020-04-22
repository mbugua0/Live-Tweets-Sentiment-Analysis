# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:21:49 2020

@author: jmmungai
"""

from flask import Flask, request, render_template, redirect
import gzip
import dill

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "This page is about Tweet analysis"

@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method == "GET":
        tweet = request.args.get("tweet")
    else:
        tweet = request.form["text"]#text is the name assigned to the text field on the html form 
        
    print(tweet)
    
    with gzip.open("../../Desktop/Documentations/DATASCIENCE/WORLDQUANT/Twitter/pickle/sentiment_analysis1.dll.gz","rb") as f:
        model = dill.load(f)
        
    #prob = model.predict_proba([tweet][0,1])   
    pred = model.predict([tweet])
    
    return "Sentiment is: {}".format(pred[0])

if __name__ == '__main__':
    app.run()