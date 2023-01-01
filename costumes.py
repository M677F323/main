import sys 
from PIL import Image
#Image
images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
#pil lib opening closing takes care of all


images[0].save(
    "costume.gif",save_all = true, append_images=[images[1]],duration =200, loop =0
)