from datetime import datetime

def get_day_suffix(day):
    if 11 <= day <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

def format_date(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    suffix = get_day_suffix(dt.day)
    return dt.strftime(f"%B {dt.day}{suffix}, %A")

def generate_digest(channels_videos):
    digest = ""
    for channel, videos in channels_videos.items():
        digest += f"{channel}\n" + "-" * len(channel) + "\n"
        for video in videos:
            title = video['title']
            url = video['url']
            formatted_date = format_date(video['publishedAt'])
            digest += f"- {title}\n  {url}\n  ({formatted_date})\n"
        digest += "\n"
    return digest
