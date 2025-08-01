import os
import google_auth_oauthlib.flow
import googleapiclient.discovery

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def list_subscribed_channels():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)

    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.subscriptions().list(
        part="snippet,contentDetails",
        mine=True,
        maxResults=50
    )
    response = request.execute()

    channels = []
    for item in response.get("items", []):
        channels.append({
            "channelId": item["snippet"]["resourceId"]["channelId"],
            "title": item["snippet"]["title"]
        })
    return youtube, channels
