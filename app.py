
from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)

# ตั้งค่าบันทึกข้อมูลลงไฟล์ log.txt
logging.basicConfig(
    filename="/app/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

HTML = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>Flask Docker Homework</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f2f5;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            max-width: 500px;
            margin: auto;
        }
        input {
            padding: 12px;
            width: 80%;
            margin: 15px;
        }
        button {
            padding: 12px 25px;
            background: #1877f2;
            color: white;
            border: none;
            cursor: pointer;
        }
        .result {
            color: green;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Flask Docker Homework</h2>
        <p>กรุณากรอกข้อความของคุณ</p>

        <form method="POST" action="/submit">
            <input type="text" name="message"
                   placeholder="พิมพ์ข้อความที่นี่" required>
            <br>
            <button type="submit">ส่งข้อมูล</button>
        </form>

        {% if message %}
        <div class="result">
            <h3>ได้รับข้อความแล้ว!</h3>
            <p>{{ message }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/submit", methods=["POST"])
def submit():
    message = request.form.get("message", "").strip()

    if not message:
        return "กรุณากรอกข้อความ", 400

    logging.info("Received message: %s", message)

    return render_template_string(
        HTML,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
