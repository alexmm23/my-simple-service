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

    if(num1 < 0 or num2 < 0):
        return jsonify({"error": "Los números deben ser positivos"})
    
    if(type(num1) != int or type(num2) != int):
        return jsonify({"error": "Los números deben ser enteros"})
    
    return jsonify({"resultado": num1 + num2})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
