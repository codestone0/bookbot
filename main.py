def main():
	file_path = 'books/frankenstein.txt'
	file_contents = get_book(file_path)

	print(f"--- Begin report of {file_path} ---")
	print(f"{word_count(file_contents)} words found in the document")
	print()
	print_letter_count(file_contents)
	print("-- End report ---")
	

def get_book(str_path):
	with open(str_path) as f:
		return f.read()

def word_count(str_book_content):
	words = str_book_content.split()
	return len(words)

def print_letter_count(str_book_content):
	char = {}
	lowered_string = str_book_content.lower()
	for c in lowered_string:
		if c in char:
			char[c] += 1
		else:
			char[c] = 1
	sorted_list = sorted(list(char.items()), key=lambda tup: tup[1], reverse=True)
	
	for item in sorted_list:
		if item[0].isalpha():
			print(f"The {item[0]} character was found {item[1]} times")

	return None
	

main()