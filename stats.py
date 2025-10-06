def get_num_words(str_book_content):
	words = str_book_content.split()
	return len(words)

def get_chars_dict(text):
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	return chars
	
def dict_to_sorted_list(chars_dict):
	sorted_list = sorted(list(chars_dict.items()), key=lambda tup: tup[1], reverse=True)
	return sorted_list


# def sort_on(d):
# 	return d["num"]

# def print_letter_count(str_book_content):
# 	char = {}
# 	lowered_string = str_book_content.lower()
# 	for c in lowered_string:
# 		if c in char:
# 			char[c] += 1
# 		else:
# 			char[c] = 1
# 	sorted_list = sorted(list(char.items()), key=lambda tup: tup[1], reverse=True)
	
# 	for item in sorted_list:
# 		if item[0].isalpha():
# 			print(f"The {item[0]} character was found {item[1]} times")

# 	return None