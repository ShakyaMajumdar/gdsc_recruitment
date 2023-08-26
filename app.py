import datetime
from flask import Flask, render_template
import requests
import werkzeug.exceptions

app = Flask(__name__)


@app.route("/")
def home():
    conf_resp = requests.get("https://gdscdev.vercel.app/api")
    if not (conf_resp.ok and (conf_json := conf_resp.json())["status"]):
        raise werkzeug.exceptions.BadGateway
    return render_template("home.html", conferences=conf_json["content"]["data"])


@app.template_filter()
def format_datetime(dt):
    return datetime.datetime.fromisoformat(dt).strftime("%d %B, %Y")


@app.errorhandler(werkzeug.exceptions.BadGateway)
def handle_bad_gateway(e):
    return render_template("502.html"), 502
