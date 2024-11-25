def lognestString(word: str):
	i = 0
	while i < len(word):
		if word.count(word[i]) > 1:
			word = word[:i] + word[i+1:]
			i = 0

		else:
			i += 1

	return word

print(lognestString("pwwekw"))