import re
import itertools


def remove_duplicate(string):
	count = 0
	search = re.compile(r' [^a-z]').search
	if not bool(search(string)) == True:
		for i in range(0,len(string)):
			if string[i+ 1: i+ 2] == string[i:i+1]:
				count +=1
		return (''.join(ch for ch, _ in itertools.groupby(string)), count)