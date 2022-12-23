from rembg import remove
from PIL import Image

input_path = 'AI model/test_images/dog.jpeg'
output_path = 'AI model/test_images/dog-adjusted.png'

# input = Image.open(input_path)
# output=remove(input)
# output.save(output_path)

# Function used to remove background from image
def remove_bg(input):
    return remove(input)

