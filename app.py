from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configura tu conexión a la base de datos
db_config = {
    "host": "bu05lnrbsbg3sfxjqy8u-mysql.services.clever-cloud.com",
    "user": "u6edweftcokchocx",
    "password": "6VP2sbN6WXyvalRAfXDI",
    "database": "bu05lnrbsbg3sfxjqy8u",
}


@app.route("/data", methods=["POST"])
def insert_data():
    data = request.json
    campo1 = data["campo1"]

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO capacidad_esp32 (capacidad) VALUES (%s)", (campo1))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success"}), 201
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)}), 500
