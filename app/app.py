import os
from flask import Flask, jsonify

app = Flask(__name__)

ENV_NAME = os.getenv("ENV_NAME", "local")

@app.route("/healthz")
def healthz():
    return jsonify(
        status="ok",
        service="app",
        env=ENV_NAME
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
