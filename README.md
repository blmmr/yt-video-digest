# YT (YouTube) video digest

![App icon](assets/app_icon.png)

Sends a plain-text email digest of all videos posted this week (from Monday to today) by your subscribed channels. Helps you escape YouTube algorithms and watch the videos that matter.

# App setup

## client_secret
`app/client_secret.json` should be a Google OAuth 2.0 client credentials file, which you can download from the GCP Console.
- Go to: https://console.cloud.google.com/apis/credentials
- Create Credentials -> OAuth client ID
- Application type: Desktop app
- name: yt-video-digest, click create
- Click Download JSON — save as `app/client_secret.json`

## .env
~~~
EMAIL_ADDRESS=<YOUR EMAIL ADDRESS>
EMAIL_PASSWORD=<APP PASSWORD IF USING 2FA>
~~~

# Future improvements
- Deploy the app on Cloud run
- Set up CI/CD pipeline (GitHub ations, Terraform)
- Save the variables (such as client_secret) as a GCP secret

