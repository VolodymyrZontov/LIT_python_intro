import requests

from settings import API_URL, API_KEY


def get_info_picture_of_the_day() -> dict:
    params = {"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    return response.json()

def get_image(url: str):
    response = requests.get(url)
    return response.content

def save_image(filename: str, image_obj: bytes):
    with open(filename, "wb") as file:
        file.write(image_obj)


result = get_info_picture_of_the_day()
img_url = result["url"]
img = get_image(img_url)
save_image("nasa.jpg", img)
