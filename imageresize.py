from PIL import Image

image = Image.open('bg2.jpeg')
image = image.resize((1028,671))
image.save('bg2_new.jpeg')
print("New_image_size",image.size)
image.show()
