from flask import Flask, request, render_template, url_for, session, redirect, jsonify
import os
import re
import psycopg2
from functions import *


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/contact.html", methods=["POST", "GET"])
def render_contact():
    if request.method == "POST":
        email = request.form.get("email")
        phone = request.form.get("telefon")
        message = request.form.get("message")

        # Regex-mönster för att validera e-postadress
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        # Regex-mönster för att validera telefonnummer (exakt 10 siffror)
        phone_pattern = r"^\d{10}$"
        # Regex-mönster för att validera meddelandet (minst 3 tecken)
        message_pattern = r"^(?=\s*\S)(.{3,}(?:\s+\S+){0,299}\s*)$"

        # Validera e-postadress
        if not re.match(email_pattern, email):
            return render_template("contact.html", message="Felaktig e-postadress!")

        # Validera telefonnummer
        if not re.match(phone_pattern, phone):
            return render_template("contact.html", message="Felaktigt telefonnummer, fyll i 10 siffror!")

        # Validera meddelandet
        if not re.match(message_pattern, message):
            return render_template("contact.html", message="Meddelandet måste vara minst 3 tecken långt!")

        # Spara data till databasen
        if save_message_to_database(email, phone, message):
            return render_template("contact.html", message="Tack för ditt meddelande, vi återkommer inom kort.")
        else:
            return render_template("contact.html", message="Ett fel uppstod vid spara meddelandet. Försök igen senare.")
    else:
        return render_template("contact.html")




@app.route("/logincontact.html", methods=["GET", "POST"])
def render_logincontact():
    if request.method == "POST":
        email = request.form.get("email")
        phone = request.form.get("telefon")
        message = request.form.get("message")

        # Regex-mönster för att validera e-postadress
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        # Regex-mönster för att validera telefonnummer (exakt 10 siffror)
        phone_pattern = r"^\d{10}$"
        # Regex-mönster för att validera meddelandet (minst 3 tecken)
        message_pattern = r"^(?=\s*\S)(.{3,}(?:\s+\S+){0,299}\s*)$"

        # Validera e-postadress
        if not re.match(email_pattern, email):
            return render_template("logincontact.html", message="Felaktig e-postadress!")

        # Validera telefonnummer
        if not re.match(phone_pattern, phone):
            return render_template("logincontact.html", message="Felaktigt telefonnummer, fyll i 10 siffror!")

        # Validera meddelandet
        if not re.match(message_pattern, message):
            return render_template("logincontact.html", message="Meddelandet måste vara minst 3 tecken långt!")

        # Spara data till databasen
        if save_message_to_database(email, phone, message):
            return render_template("logincontact.html", message="Tack för ditt meddelande, vi återkommer inom kort.")
        else:
            return render_template("logincontact.html", message="Ett fel uppstod vid spara meddelandet. Försök igen senare.")
    else:
        return render_template("logincontact.html")



if __name__ == "__main__":
    app.run(debug=True)   