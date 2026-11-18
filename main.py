import keyboard
from time import sleep
from PIL import Image
import os
import pyautogui
import shutil

class DownloadBook:

    def __init__(self, left, right, up, down, pages):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.pages = pages

    def make_screenshots(self):
        sleep(10) # Время ожидания перед запуском
        for i in range(self.pages):
            a = ''
            if i <= 9: a = '0'
            pyautogui.screenshot(region=[self.left, self.up, self.right-self.left, self.down-self.up], imageFilename=f'./temp/scr_{a}{i}.png')

            keyboard.press_and_release("down")
            sleep(1) # Отвечает за время между созданием скриншотов

    @staticmethod
    def convert_images_to_pdf():
        files = os.listdir('./temp')
        images = []
        for i in range(len(files)):
            now_image = Image.open(f'./temp/{files[i]}')
            images.append(now_image)

        first_image = Image.open(f'./temp/{files[0]}')
        first_image.save('./book.pdf', save_all=True, append_images=images[1:])

        first_image.close()
        for closes in range(len(files)):
            images[closes].close()

    @staticmethod
    def clear_images():
        shutil.rmtree('./temp')
        os.mkdir('./temp')



left = 584 # Координата левой стороны страницы (x)
right = 1320 # Координата правой стороны страницы (x)
up = 33 # Координата верхней стороны страницы (y)
down = 1074 # Координата нижней стороны страницы (y)
pages = 34 # Количество страниц в документе

book = DownloadBook(left, right, up, down, pages) # "Создание" книги
book.make_screenshots() # Создание скриншотов
book.convert_images_to_pdf() # Сборка всех скриншотов в 1 файл book.pdf
book.clear_images() # Удаление скриншотов из папки


