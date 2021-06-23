from flask import Flask, request, jsonify, render_template, make_response
import logging
import sys
import datetime
import platform
import os


logger = logging.getLogger("preply-test-app")
logger.setLevel(logging.INFO)
hdl = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)-15s: %(message)s")
hdl.setFormatter(formatter)
logger.addHandler(hdl)

app = Flask("preply-test-app", template_folder="templates")

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "meta": {
            "product": "Preply Test Application",
            "generated_at": datetime.datetime.now().isoformat(),
            "generated_by": platform.node()
        }})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "health": "OK",
        "meta:": {
            "product": "Preply Test Application",
            "generated_at": datetime.datetime.now().isoformat(),
            "generated_by": platform.node()
        }})

@app.route("/ready", methods=["GET"])
def ready():
    return jsonify({
        "ready": "OK",
        "meta:": {
            "product": "Preply Test Application",
            "generated_at": datetime.datetime.now().isoformat(),
            "generated_by": platform.node()
        }})

@app.route("/", methods=["GET"])
def index():
    secret = os.environ.get('SECRET', '')
    resp = make_response(render_template("index.html", secret=secret))

    return resp

if __name__ == "__main__":
    app.run()
