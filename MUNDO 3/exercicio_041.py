import requests
try:
    site = requests.get("https://www.cursoemvideo.com/")
except:
    print("deu merda")
else:
    print("deu certo acessei o curso em video")
    