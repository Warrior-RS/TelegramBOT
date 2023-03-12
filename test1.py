from rembg import remove
from PIL import Image

input_path = 'C:/news/2022-10-22.png'
output_path = 'C:/news/2022-10-22up.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
