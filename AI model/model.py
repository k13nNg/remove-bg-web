from rembg import remove
from PIL import Image

input_path = 'AI model/test_images/selfie.jpeg'
output_path = 'AI model/test_images/selfie-adjusted.png'

input = Image.open(input_path)
output=remove(input)
output.save(output_path)

