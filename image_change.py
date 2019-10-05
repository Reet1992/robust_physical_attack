import matplotlib.pyplot as plt
from PIL import Image,ImageFilter  
#Read image
im = Image.open('result.png')
#Display image  
im.show()

plt.switch_backend('agg')
plt.savefig('final_result.png')
plt.show()


   
from PIL import ImageEnhance  
enh = ImageEnhance.Contrast(im)  
enh.enhance(1.8).show("30% more contrast")
