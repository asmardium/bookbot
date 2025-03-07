def count_words(book_text):
	num_words = len(book_text.split())
	return num_words

def count_characters_dict(book_text):
	num_characters_dict = {}
	book_text_lower = book_text.lower()
	for each_Character in book_text_lower:
		if each_Character in num_characters_dict:
			num_characters_dict[each_Character] = num_characters_dict[each_Character] + 1
		else:
			num_characters_dict[each_Character] = 0 + 1
	#num_characters_dict = dict(sorted(num_characters_dict.items()))
	return num_characters_dict

def sort_on(dict):
	return dict["the_count"]

def count_characters_list(book_text):
	num_characters_dict = {}
	book_text_lower = book_text.lower()
	for each_Character in book_text_lower:
		if each_Character in num_characters_dict:
			num_characters_dict[each_Character] = num_characters_dict[each_Character] + 1
		else:
			num_characters_dict[each_Character] = 0 + 1
	
	num_characters_list = []
	for each_key in num_characters_dict:
		each_value = num_characters_dict[each_key]
		tempDict = {"character":each_key,"the_count":each_value}
		num_characters_list.append(tempDict)
	#print(num_characters_list)
	num_characters_list.sort(reverse=True, key=sort_on)

	#num_characters_dict = dict(sorted(num_characters_dict.items()))
	return num_characters_list