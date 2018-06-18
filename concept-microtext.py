from jellyfish import soundex,metaphone,match_rating_codex

sn = open("senticnet5.txt","r")
for line in sn:
	sndx = []
	metaphn = []
	codex = []
	concept = (line.split('\t')[0])
	words = concept.split('_')
	for i in range(len(words)):
		sndx.append(soundex(words[i]))
		metaphn.append(metaphone(words[i]))
		codex.append(match_rating_codex(words[i]))
	print (concept,'\t','_'.join(metaphn))
