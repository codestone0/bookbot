from stats import get_num_words, get_chars_dict, dict_to_sorted_list

def main():
	file_path = 'books/frankenstein.txt'
	file_contents = get_book(file_path)
	word_count = get_num_words(file_contents)
	chars_dict = get_chars_dict(file_contents)
	sorted_list = dict_to_sorted_list(chars_dict)

	print_report(file_path, word_count, sorted_list)
	# print(f"--- Begin report of {file_path} ---")
	# print(f"Found {get_num_words(file_contents)} total words ")
	# print()
	# print_letter_count(file_contents)
	# print("-- End report ---")
	

def get_book(str_path):
	with open(str_path) as f:
		return f.read()

def print_report(file_path, word_count, chars_sorted_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words ")
	print("--------- Character Count -------")
	for item in chars_sorted_list:
		if item[0].isalpha():
			print(f"{item[0]}: {item[1]}")
	print("============= END ===============")

main()