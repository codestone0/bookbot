def word_count(str):
	words = str.split()
	return len(words)

with open("books/frankenstein.txt") as f:
	file_contents = f.read()

print(word_count(file_contents))