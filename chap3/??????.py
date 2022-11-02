from requests import get

web = (
    "google.com",
    "naver.com",
    "twitter.com",
    "facebook.com",
)
results = {}

for web in web:
    if not web.startswith("https://"):
      web = f"https://{web}"
      response = get(web)
      if response.status_code == 200:
        results[web] = "OK"
      else:
        results[web] = "not OK"

print(results)


#앞에서 배운것과 같은 코드를 사용하였고 원래는 requests를 이용해서 vscode를 활용해서 하려 했으나 pip 과정에서 계속 막혀서 그냥 repl.it에서 나머지 코드를 작성했다
#솔직히 코드를 작성 했지만 이해 안되는것 투성이라 다시 복습이 필요하다
