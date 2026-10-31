from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

DB_HOST=os.getenv("DB_HOST","localhost")
DB_NAME=os.getenv("DB_NAME","attendance")
DB_USER=os.getenv("DB_USER","postgres")
DB_PASSWORD=os.getenv("DB_PASSWORD","password")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/attendance", methods=["POST"])
def mark_attendance():

    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO attendance
        (employee_name, attendance_date,status)
        VALUES (%s,%s,%s)
        """,
        (
            data["employee_name"],
            data["attendance_date"],
            data["status"]
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message":"Attendance saved"})


@app.route("/attendance", methods=["GET"])
def get_attendance():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM attendance")

    rows = cur.fetchall()

    result=[]

    for row in rows:
        result.append({
            "id":row[0],
            "employee_name":row[1],
            "attendance_date":str(row[2]),
            "status":row[3]
        })

    cur.close()
    conn.close()

    return jsonify(result)

app.run(host="0.0.0.0", port=5000)