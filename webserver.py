from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "open web server"

def host():
    app.run(host="0.0.0.0", port=8080)

def run():
    server = Thread(target=host)
    server.start()