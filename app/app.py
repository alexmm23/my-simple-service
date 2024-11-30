from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "¡Hola desde Flask!"})

@app.route("/saludo/<nombre>")  
def saludo(nombre):
    return jsonify({"message": f"¡Hola {nombre}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
