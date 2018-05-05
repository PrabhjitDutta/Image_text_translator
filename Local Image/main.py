import pytesseract
import requests
from PIL import Image


def main():

    address = input("Enter the address of the image file: ")
    image = Image.open(address)

    text = pytesseract.image_to_string(image)

    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    API_KEY = 'Your Yandex API key'

    params = {'key': API_KEY, 'text': text, 'lang': 'en'}

    r2 = requests.get(URL, params=params)
    result = r2.json()
    print(result['text'][0])


if __name__ == '__main__':
    main()
