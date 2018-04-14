
from textblob_de import TextBlobDE as TextBlob

texts = [
    'Warum bin ich so fröhlich?',
    'Warum bin ich nicht fröhlich?',
    'Er ist auch manchmal traurig']

for text in texts:
    polarity = TextBlob(text).polarity
    print('polarity of "{}": {}'.format(text, polarity))
