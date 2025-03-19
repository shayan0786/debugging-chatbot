from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/debug", methods=["POST"])
def debug_code():
    try:
        data = request.get_json()
        code = data.get("code", "")

        if not code.strip():
            return jsonify({"fixes": ["❌ Error: No code provided!"], "corrected": "N/A"})

        # Example of generating multiple fixes
        fixes = [
            code.replace("sum = ", "result = "),  # Fix variable naming issue
            code.replace("print", "print()"),  # Fix missing parentheses in print
            code.replace("int x", "x = 0")  # Fix incorrect initialization (fake example)
        ]

        # Generating corrected code (Mock fix)
        corrected_code = code.replace("sum = ", "result = ")

        return jsonify({"fixes": fixes, "corrected": corrected_code})

    except Exception as e:
        print("🔥 Error:", traceback.format_exc())
        return jsonify({"fixes": ["❌ An error occurred while debugging!"], "corrected": "N/A"})

if __name__ == "__main__":
    app.run(debug=True)
