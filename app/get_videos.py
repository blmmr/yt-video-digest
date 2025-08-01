from datetime import datetime, timedelta, timezone


def get_monday():
    today = datetime.now(timezone.utc)
    monday = today - timedelta(days=today.weekday())
    return monday

def get_videos(youtube, channel_id):
    monday = get_monday()
    published_after = monday.isoformat("T") + "Z"

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        publishedAfter=published_after,
        type="video",
        order="date",
        maxResults=50
    )
    response = request.execute()
    videos = []
    for item in response.get("items", []):
        videos.append({
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "publishedAt": item["snippet"]["publishedAt"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })
    return videos
