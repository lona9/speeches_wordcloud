import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from wordcloud import WordCloud
from stop_words import get_stop_words
import numpy as np
from PIL import Image

stop_words = get_stop_words('spanish')
additional_words = ["personas", "toda", "año", "millones", "vacunación", "vacunar", "día", "hoy", "mil"]
stop_words.extend(additional_words)
file = open("piñera.txt", encoding="utf8")
line = file.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt', 'a')
        appendFile.write(" " + r)
        appendFile.close()
with open('filteredtext.txt', 'r', encoding="latin-1") as txt_file:
    filteredtext = txt_file.read()


mask = np.array(Image.open('dinosaur.png'))
wordcloudd = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black',
                    colormap='bwr', collocations=False,
                         stopwords=stop_words,mask=mask).generate(filteredtext)
# Display image
plt.figure(figsize=(40, 30))
plt.axis("off")
wordcloudd.to_file("piñera.png")