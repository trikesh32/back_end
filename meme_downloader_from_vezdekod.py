import vk
import os
import requests
TOKEN = "vk1.a.hVHXtwj-egep48Cz9hg8cYI_HSUQfKoXLxnZQAQi49O5nDARTJyOoxY77coyPPVCWYX13GfQXBJINX3oAQOcOO5HSPON0w011861Pqvb9jfIyBiD-lYAd8QLBnbz28bXdVfAW0hLIATEYSHSOUdgVWf3nfIb4q186atbUvD0RJoQsDZGf2zrON7_ZLO7-AW6"
if not os.path.exists("./memes"):
    os.mkdir("./memes")
session = vk.AuthSession(access_token=TOKEN)
vk_api = vk.API(session)
data = vk_api.photos.get(v="5.131", owner_id=-197700721, album_id=281940823, extended=1, count=1000)
for i, photo in enumerate(data["items"]):
    with open(f"memes/{i + 1}.jpg", "wb+") as image:
        cont = requests.get(photo["sizes"][-1]["url"]).content
        image.write(cont)
    print(f"Name: {i + 1}.jpg, Likes: {photo['likes']['count']}, Comments: {photo['comments']['count']}, Author: {photo['user_id']}")