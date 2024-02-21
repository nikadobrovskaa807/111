from PIL import Image #инициализация библиотеки
from PIL import Image
img = Image.open('gtqpf;111.jpg')
img.show() #открыть изображение

from PIL import Image
img = Image.open('gtqpf;111.jpg')
print(img.format) #просмотр формата изображения. Выведет 'JPEG'
print(img.mode) #просмотр типа цветового пространства. Выведет 'RGB'
print(img.size) #просмотр размера изображения. Выведет (568, 305)
print(img.filename) #просмотр имени файла. Выведет 'test.jpg'
r, g, b = img.split()
histogram = img.histogram()
print(histogram) #просмотр значений RGB изображения. Выведет 1750, 255, 267, 237, 276, 299…

from PIL import Image
img = Image.open('gtqpf;111.jpg') #методы для кропа (обрезки) изображений
cropped = img.crop((0, 0, 50, 80))
cropped.save('cropped_gtqpf;111.jpg')
img = Image.open('cropped_gtqpf;111.jpg')
img.show()

from PIL import Image
img = Image.open('cropped_gtqpf;111.jpg')
rotated = img.rotate(180) #поворот изображения
rotated.save('rotated_gtqpf;111.jpg')
img = Image.open('rotated_gtqpf;111.jpg')
img.show()

from PIL import Image
img = Image.open('cropped_gtqpf;111.jpg')
img.save('cropped_gtqpf;111_png.png', 'png') #конвертация в png

from PIL import Image
img = Image.open('cropped_gtqpf;111.jpg')
img = img.resize((170, 100), Image.ANTIALIAS) #изменение размера изображения
img.save('cropped_gtqpf;111.jpg')
img = Image.open('cropped_gtqpf;111_text.jpg')
img.show()

from PIL import Image, ImageDraw, ImageFont
img = Image.open('cropped_gtqpf;111.jpg')
font = ImageFont.truetype("arial.ttf", size=30) #текст
idraw = ImageDraw.Draw(img)
idraw.text((25, 25), 'gtqpf;111 gtqpf;111 gtqpf;111', font=font)
img.save('cropped_gtqpf;111_text.jpg')
img = Image.open('cropped_gtqpf;111_text.jpg')
img.show()

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'black')
img.save('crop.jpg') #создание пустого изображения
img = Image.open('crop.jpg')
img.show()

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'black')
idraw = ImageDraw.Draw(img)
idraw.rectangle((0, 0, 100, 100), fill='white') #создание белого прямоугольника
img.save('crop.jpg')
img = Image.open('crop.jpg')
img.show()
