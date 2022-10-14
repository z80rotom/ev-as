from flask import Flask

app = Flask(__name__)

@app.route("/api/ev_script")
def ev_script():
    return "Hello World!"

app.run("192.168.1.198", 8080)