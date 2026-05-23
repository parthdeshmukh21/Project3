from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Project3 DevOps Pipeline Working! Lets crack it now"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
