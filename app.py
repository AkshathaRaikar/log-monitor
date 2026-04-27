from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "logs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def analyze_logs(filepath):
    error_keywords = ["ERROR", "FAILED", "EXCEPTION", "CRITICAL"]

    results = []
    error_count = 0

    with open(filepath, "r") as file:
        lines = file.readlines()

    for line in lines:
        clean_line = line.strip()

        if any(keyword in clean_line for keyword in error_keywords):
            error_count += 1
            results.append(("ERROR", clean_line))
        else:
            results.append(("INFO", clean_line))

    anomaly = error_count > 3

    return results, error_count, anomaly


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error_count = 0
    anomaly = False

    if request.method == "POST":
        file = request.files["logfile"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        results, error_count, anomaly = analyze_logs(filepath)

    return render_template(
        "index.html",
        results=results,
        error_count=error_count,
        anomaly=anomaly
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)