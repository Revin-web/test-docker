from flask import Flask

app = Flask(__name__)

@app.route("/")
def info():
    return """
        <h1>Welcome!</h1>
        <p><strong>Name:</strong> Revin N</p>
        <p><strong>Role:</strong> DevOps Engineer</p>
        <p><strong>Skills:</strong> Python, Docker, AWS, CI/CD, GitHub Actions</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
