from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as plt
from PIL import Image
import numpy as np

#Content-related
text = open('Economics.txt','r').read()
stopwords = set(STOPWORDS)


#Appearence-related
custom_mask = np.array(Image.open('cloud.png'))
wc = WordCloud(background_color='white',stopwords=stopwords,mask = custom_mask,contour_width=3,contour_color='black')

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func=image_colors)

wc.to_file('ecowc.png')
