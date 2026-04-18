from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    results = {}
    logs = []

    if request.method == "POST":
        platform = request.form.get("platform")
        budget = request.form.get("budget")
        stores = request.form.getlist("stores")
        components = request.form.getlist("components")

        logs.append(f"Platform: {platform}")
        logs.append(f"Budget: {budget}")
        logs.append(f"Stores: {stores}")
        logs.append(f"Components: {components}")

        results = {
            "CPU": "Ryzen 5 7600",
            "GPU": "RTX 4060"
        }

    return render_template("index.html", results=results, logs=logs)