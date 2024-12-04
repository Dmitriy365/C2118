
import cv2
from PIL import Image

image_dog_path = 'dog.jpg'
dog_face_handler = cv2.CascadeClassifier('haarcascade_frontaldog_extended.xml')

image_dog = cv2.imread(image_dog_path)

dog_face_coordinates = dog_face_handler.detectMultiScale(image_dog)

for (x, y, w, h) in dog_face_coordinates:
    cv2.rectangle(image_dog, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow('Dog', image_dog)

dog = Image.open(image_dog_path)
dog_glasses = Image.open('dog_glasses.png')

dog = dog.convert('RGB')
dog_glasses = dog_glasses.convert('RGB')

(x, y, w, h) = dog_face_coordinates[0]
dog_glasses = dog_glasses.resize((w, int(h/3)))

dog.paste(dog_glasses, (x, int(y + h/4)))
dog.save('dog_with_glasses.jpeg')

dog_with_glasses = cv2.imread('dog_with_glasses.jpeg')
cv2.imshow('Dog with sunglasses', dog_with_glasses)

cv2.waitKey()

