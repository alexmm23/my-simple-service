from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "¡Hola desde Flask!"})

@app.route("/saludo/<nombre>")  
def saludo(nombre):
    return jsonify({"message": f"¡Hola {nombre}!"})

@app.route("/about")
def about():
    return jsonify({"message": "About Us"})
@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):  
    return jsonify({"resultado": num1 + num2})
#comentario de prueba
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
