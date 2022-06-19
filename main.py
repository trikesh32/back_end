import vk
import pprint
import os
import requests
import csv
from meme_viwer import show_image
TOKEN = "vk1.a.hVHXtwj-egep48Cz9hg8cYI_HSUQfKoXLxnZQAQi49O5nDARTJyOoxY77coyPPVCWYX13GfQXBJINX3oAQOcOO5HSPON0w011861Pqvb9jfIyBiD-lYAd8QLBnbz28bXdVfAW0hLIATEYSHSOUdgVWf3nfIb4q186atbUvD0RJoQsDZGf2zrON7_ZLO7-AW6"
# os.mkdir('./memes')
# session = vk.AuthSession(access_token=TOKEN)
# vk_api = vk.API(session)
# pprint.pprint(vk_api.photos.get(v="5.131", owner_id=-88245281, album_id=271694981, exteneded=True, count=1000))
s = open("meme.jpg", "wb+")
data = requests.get("https://sun5-4.userapi.com/impg/c858524/v858524153/13c77d/m72jEw_sC9I.jpg?size=713x800&quality=96&sign=ae61255ebd0dd570ff9756fd96bfc3ac&c_uniq_tag=4cZaDQQ1ELi_cVVnPYJLVY57FaefEFa3v9UXhxeMfQI&type=album")
s.write(data.content)
show_image("meme.jpg")
