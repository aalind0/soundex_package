from jellyfish import soundex,metaphone

sn = open("senticnet5.txt","r")
lb = open("concept+metaphone.txt", "r+")
for line in sn:
	sndx = []
	metaphn = []
	concept = (line.split('\t')[0])
	words = concept.split('_')
	for i in range(len(words)):
		sndx.append(soundex(words[i]))
		metaphn.append(metaphone(words[i]))
	print (concept,'\t','_'.join(metaphn))
