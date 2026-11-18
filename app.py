from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud-Lab-05</h1>
    <p>Containerized DevOps Platform</p>
    <p>Application is running successfully.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Cloud-Lab-05",
        "version": "1.0.0"
    }), 200

@app.route("/info")
def info():
    return jsonify({
        "application": "Cloud-Lab-05",
        "description": "Containerized DevOps Platform",
        "environment": "development",
        "technology": "Python + Flask"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)