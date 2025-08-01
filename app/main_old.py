import logging
from rich.logging import RichHandler
from flask import Flask, request, jsonify
from datetime import datetime
from app.list_channels import list_subscribed_channels

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    handlers=[RichHandler()]
)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_summary():
    logging.info("Summary trigger received")

    try:
       list_subscribed_channels()
       return jsonify({"status": "success", "message": "Summary processed"}), 200


    except Exception as e:
        logging.error(f"Error during summary execution: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
