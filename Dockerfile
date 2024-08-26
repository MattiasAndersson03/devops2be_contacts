# Välj en officiell Python-bild som bas
FROM python:3.11-slim

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera applikationens kod till containern
COPY . .

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Exponera port (Flask körs på en viss port)
EXPOSE 5003

# Sätt miljövariabler för Flask
ENV FLASK_APP=app.py

# Starta Flask-applikationen
CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]