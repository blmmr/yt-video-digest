import logging
from rich.logging import RichHandler
from flask import Flask, request, jsonify

from list_channels import list_subscribed_channels
from get_videos import get_videos
from email_auth import send_email
from send_email import generate_digest


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
        youtube, channels = list_subscribed_channels()
        channels_videos = {}

        for ch in channels:
            videos = get_videos(youtube, ch["channelId"])
            if videos:
                channels_videos[ch["title"]] = videos

        digest = generate_digest(channels_videos)
        send_email("Weekly YouTube Video Digest", digest)

        return jsonify({"status": "success", "message": "Summary processed"}), 200

    except Exception as e:
        logging.error(f"Error during summary execution: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
