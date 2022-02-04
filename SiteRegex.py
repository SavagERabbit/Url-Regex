from pathlib import Path
import re, pyperclip
import os
'''
Trova tutti i link presenti nella pyperclip
'''
currPath = Path.cwd()


def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


# Driver Code
text = str(pyperclip.paste())
matches = Find(text)
#print("Urls: ", Find(text))
pyperclip.copy('\n'.join(matches))
res = str(pyperclip.paste())
print('copied to clipboard')
#print('\n'.join(matches))
try:
    with open(currPath / 'res.txt', 'w') as newFile:
        print('file created.')
        newFile.write(res)
except FileNotFoundError:
    print('the dir does not exists.')
