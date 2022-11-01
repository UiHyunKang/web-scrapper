web = (
    "google.com",
    "naver.com",
    "twitter.com",
    "facebook.com",
)

for web in web:
    if not web.startswith("https://"):
      web = f"https://{web}"
    print(web)
