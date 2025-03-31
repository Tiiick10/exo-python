from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    result = ""
    exercice = request.form.get("exercice")

    if request.method == "POST":
        if exercice == "1":
            try:
                annee = int(request.form["annee"])
                age = 2025 - annee
                result = f"Vous avez {age} ans."
            except:
                result = "Veuillez entrer une année valide."

        elif exercice == "2":
            try:
                celsius = float(request.form["celsius"])
                fahrenheit = (celsius * 9 / 5) + 32
                result = f"{celsius}°C équivaut à {fahrenheit:.2f}°F."
            except:
                result = "Veuillez entrer une température valide."

        elif exercice == "3":
            try:
                rayon = float(request.form["rayon"])
                surface = math.pi * rayon ** 2
                result = f"La surface du cercle est de {surface:.2f} cm²."
            except:
                result = "Veuillez entrer un rayon valide."

        elif exercice == "4":
            try:
                poids = float(request.form["poids"])
                taille = float(request.form["taille"])
                imc = poids / (taille ** 2)
                if imc < 18.5:
                    interpretation = "maigreur"
                elif imc < 25:
                    interpretation = "poids normal"
                elif imc < 30:
                    interpretation = "surpoids"
                else:
                    interpretation = "obésité"
                result = f"Votre IMC est de {imc:.2f} → {interpretation}"
            except:
                result = "Veuillez entrer un poids et une taille valides."

    return render_template("index.html", result=result, exercice=exercice)

if __name__ == "__main__":
    app.run(debug=True)
