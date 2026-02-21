from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/api/health")
def health():
    return jsonify(status="ok")


@app.get("/api/echo")
def echo():
    msg = request.args.get("msg", "hello")
    return jsonify(echo=msg)


@app.post("/api/items")
def create_item():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify(error="Missing 'name'"), 400
    # In serverless, don’t rely on in-memory storage for “real” persistence.
    return jsonify(id="temp-id", name=name), 201
