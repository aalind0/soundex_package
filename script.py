import re
from jellyfish import soundex,metaphone

sentic = open("concepts+soundex.txt", "r").read()
#text = sentic.read().strip().split()
string = input("Enter a string: ")
sndx = soundex(string)
print(sndx)


for line in sentic.split("\n"):
    #print (line)
    if sndx in line.split(" \t "):
        print (line)
        #if sndx in soundx and len(sndx) == len(soundx):
        #    print(soundx)

# for line in text:
#     if re.search(sndx, line, re.I):
#         print(line)

# while True:
#     if sndx in text:
#         print(text)
