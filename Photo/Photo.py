from removebg import remove
from PIL import Image
img = Image.open("C:\\Users\\MY\\Desktop\\Nishant\\Photo\\NK.jpeg")
R = remove(img)
R.save("image.pngnnk")



