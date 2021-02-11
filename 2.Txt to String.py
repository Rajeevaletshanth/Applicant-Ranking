#Text to String (utf-8)

import os
from chardet import detect

# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

from_codec = get_encoding_type('Resume.txt')

#Resume convertion
try:
    with open('Resume.txt', 'r', encoding=from_codec) as f, open('ResumeStr.txt', 'w', encoding='utf-8') as e:
        text = f.read() # for small files, for big use chunks
        e.write(text)

except UnicodeDecodeError:
    print('Decode Error')
except UnicodeEncodeError:
    print('Encode Error')

