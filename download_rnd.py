import requests
import os


def fetch_dog_image_url():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    response.raise_for_status()
    data = response.json()
    return data['message']


# Функция для скачивания и сохранения изображений собак
def download_random_dog_images(image_count):
    for i in range(image_count):
        try:
            # Получаем URL случайного изображения собаки
            img_url = fetch_dog_image_url()
            # Скачиваем изображение
            response = requests.get(img_url)
            response.raise_for_status()
            # Сохраняем изображение в файл
            img_name = f"{i+1}.jpg"
            with open(f'uniq/{img_name}', 'wb') as file:
                file.write(response.content)
            print(f"Изображение {img_name} успешно скачано.")
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')

