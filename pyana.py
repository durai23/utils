import sys
#anagram detection using dicts
def anornot(w1,w2):
	w1dict={}
	w2dict={}
	for i in range(0,len(w1)):
		w1dict[w1[i]]=nchrinwrd(w1[i],w1)
	for i in range(0,len(w2)):
		w2dict[w2[i]]=nchrinwrd(w2[i],w2)
	if (len(w1dict)!=len(w2dict)):
		return False
	else:
		kyz=w1dict.keys()
		for i in range(0,len(kyz)):
			if (w1dict[kyz[i]]!=w2dict[kyz[i]]):
				return False
	return True

def nchrinwrd(chr,wrd):
	count=0
	for i in range(0,len(wrd)):
		if chr==wrd[i]:
			count+=1
	return count

print anornot(sys.argv[1],sys.argv[2])
# if(anornot(sys.argv[1],sys.argv[2])):
# 	print 'anagrams'
# else:
# 	print 'not anagrams'