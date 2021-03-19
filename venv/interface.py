from flask import Flask, redirect, url_for, render_template, request
from twilio.rest import Client
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', content='Add a Text', url='Add an Image URL')

@app.route("/", methods=["POST"])
def message():
    if request.method == "POST":
        text = request.form["nm"]
        image = request.form["nm2"]
        def send(text, image):
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)
            
            message = client.messages.create(
                                        body=text,
                                        from_='+',
                                        media_url=[image],
                                        to='+'
                                            )

        return send(text, image)

if __name__=="__main__":
    app.run()

