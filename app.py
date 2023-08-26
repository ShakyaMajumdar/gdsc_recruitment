from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    conf_resp = requests.get("https://gdscdev.vercel.app/api")
    conf_json = conf_resp.json()
    if not conf_json["status"]:
        raise Exception 
    return render_template("home.html", conferences=conf_json["content"]["data"])
