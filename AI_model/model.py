from rembg import remove
from PIL import Image

input_path = 'AI_model/test_images/dog.jpeg'
output_path = 'AI_model/test_images/dog-adjusted.png'

input = Image.open(input_path)
# print(type(input))
output=remove(input)
print(type(output))
output.show()
# output.save(output_path)

# Function used to remove background from image
# def remove_bg(input):
#     return remove(input)

