from flask import Flask, jsonify, render_template, request, redirect, json
from tinydb import TinyDB, Query
from datetime import datetime

app = Flask(__name__)

logs = TinyDB('../db/logs.json')

def log_request():
    # Function to log HTTP requests
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request_data = {
        'timestamp': current_time,
        'method': request.method,
        'path': request.path,
        'query_string': request.query_string.decode('utf-8'),
        'remote_addr': request.remote_addr,
        'user_agent': request.user_agent.string
    }
    logs.insert(request_data)

@app.before_request
def before_request():
    # Log HTTP requests before processing
    log_request()


# Retorna mensagem pong
@app.route("/ping", methods=["GET"])
def pong():
    return jsonify({"resposta" : "pong"})


# Retorna mensagem enviado pelo usuário
@app.route("/echo", methods=["POST"])
def echo():
    message = request.get_json()

    send_back_message = {"resposta" : message["dados"]}

    return send_back_message

# Retorna a página de logs
@app.route("/dash")
def dash():
    return render_template("logs.html")


# retornas o logs para componente HTMX
@app.route("/info")
def info():
    return logs.all()


@app.route("/clear_logs", methods=["GET"])
def clear_logs():
    # Route to clear logs
    logs.truncate()  # Truncate the logs table, removing all data


if __name__ == "__main__":
    app.run(debug=True)