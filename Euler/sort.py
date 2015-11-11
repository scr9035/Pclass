from __future__ import print_function
import string
import sys
from string import maketrans

#test_sentence = 'I may opt for a top yam for Amy, May, and Tommy.'

for line in sys.stdin:
	test_sentence = line

test_sentence = test_sentence.lower().translate(None, string.digits)
test_sentence = test_sentence.translate(None, string.punctuation)

test_sentence = test_sentence.split()

word_sorted_sentence = []
for word in test_sentence:
	word = ''.join(sorted(word))
	word_sorted_sentence.append(word)
	#print(word)

completed_sorted_sentence = set(word_sorted_sentence)
completed_sorted_sentence = list(completed_sorted_sentence)
finished_sentence = ' '.join(sorted(completed_sorted_sentence))


print(finished_sentence)