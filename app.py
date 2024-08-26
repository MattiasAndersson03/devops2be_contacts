from flask import Flask, request, render_template, url_for, session, redirect, jsonify
import os
import re
# import psycopg2
# from functions import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/contact.html", methods=["POST", "GET"])
def render_contact():
    if request.method == "POST":
        # Kontrollera om filen meddelande.txt finns, annars skapas den
        if not os.path.isfile("meddelanden.txt"):
            with open("meddelanden.txt", "w", encoding="utf-8"):
                pass  # Skapar filen om den inte finns

        # Regex-mönster för att validera e-postadress
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        # Regex-mönster för att validera telefonnummer (exakt 10 siffror)
        phone_pattern = r"^\d{10}$"
        # Regex-mönster för att validera meddelandet (minst 3 tecken)
        message_pattern = r"^(?=\s*\S)(.{3,}(?:\s+\S+){0,299}\s*)$"

        # Validera e-postadress
        if not re.match(email_pattern, request.form["email"]):
            return render_template("/contact.html", message="<span style='color: white;'>Felaktig e-postadress!</span>")

        # Validera telefonnummer
        if not re.match(phone_pattern, request.form["telefon"]):
            return render_template("/contact.html", message="<span style='color: white;'>Felaktigt telefonnummer, fyll i 10 siffror!</span>")

        # Validera meddelandet
        if not re.match(message_pattern, request.form["message"]):
            return render_template("/contact.html", message="<span style='color: white;'>Meddelandet måste vara minst 3 tecken långt!</span>")

        # Om allt är korrekt, spara datan
        with open("meddelanden.txt", "a", encoding="utf-8") as file:
            file.write(f"{request.form['email']}, {request.form['telefon']}, {request.form['message']}\n")
        return render_template("/contact.html", message="<span style='color: white;'>Tack för ditt mail, vi återkommer inom kort.</span>")
    else:
        return render_template("contact.html")

@app.route("/logincontact.html", methods=["GET", "POST"])
def render_logincontact():
    if request.method == "POST":
        # Kontrollera om filen meddelande.txt finns, annars skapas den
        if not os.path.isfile("meddelanden.txt"):
            with open("meddelanden.txt", "w", encoding="utf-8"):
                pass  # Skapar filen om den inte finns

        # Regex-mönster för att validera e-postadress
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        # Regex-mönster för att validera telefonnummer (exakt 10 siffror)
        phone_pattern = r"^\d{10}$"
        # Regex-mönster för att validera meddelandet (minst 3 tecken)
        message_pattern = r"^(?=\s*\S)(.{3,}(?:\s+\S+){0,299}\s*)$"

        # Validera e-postadress
        if not re.match(email_pattern, request.form["email"]):
            return render_template("/logincontact.html", message="<span style='color: white;'>Felaktig e-postadress!</span>")

        # Validera telefonnummer
        if not re.match(phone_pattern, request.form["telefon"]):
            return render_template("/logincontact.html", message="<span style='color: white;'>Felaktigt telefonnummer, fyll i 10 siffror!</span>")

        # Validera meddelandet
        if not re.match(message_pattern, request.form["message"]):
            return render_template("/logincontact.html", message="<span style='color: white;'>Meddelandet måste vara minst 3 tecken långt!</span>")

        # Om allt är korrekt, spara datan
        with open("meddelanden.txt", "a", encoding="utf-8") as file:
            file.write(f"{request.form['email']}, {request.form['telefon']}, {request.form['message']}\n")
        return render_template("/logincontact.html", message="<span style='color: white;'>Tack för ditt mail, vi återkommer inom kort.</span>")
    else:
        return render_template("logincontact.html") 

if __name__ == "__main__":
    app.run(debug=True)    
    