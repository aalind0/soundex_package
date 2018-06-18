import re
from jellyfish import soundex,metaphone,match_rating_codex

sentic = open("codex.txt", "r").read()
sentic1 = open("concepts+soundex.txt", "r").read()
sentic2 = open("concepts+metaphone.txt", "r").read()
#text = sentic.read().strip().split()
string = input("Enter a string: ")
cdx = match_rating_codex(string)
print(cdx)
sdx = soundex(string)
meta = metaphone(string)

print("Codex Results\n")
for line in sentic.split("\n"):
    #print (line)
    if cdx in line.split(" \t "):
        print (line)
        #if sndx in soundx and len(sndx) == len(soundx):
        #    print(soundx)
print ("Soundex Results\n")

for line in sentic1.split("\n"):
    if sdx in line.split(" \t "):
        print (line)

print("Metaphone Results\n")

for line in sentic2.split("\n"):
    if meta in line.split(" \t "):
        print(line)
# for line in text:
#     if re.search(sndx, line, re.I):
#         print(line)

# while True:
#     if sndx in text:
#         print(text)
