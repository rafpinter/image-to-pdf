# import img2pdf
from PIL import Image
import sys

# getting argv
img_filepath = sys.argv[1]

# file extension
img_extension = img_filepath.split('.')[-1]

# replacing image extension
pdf_filename = img_filepath.replace(img_extension, 'pdf')

# opening image
image = Image.open(img_filepath)
 
# converting 
pdf_bytes = image.convert('RGB')

# saving pdf
pdf_bytes.save(pdf_filename)
  
# output
print("Successfully made pdf file")