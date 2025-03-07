from stats import count_words
from stats import count_characters_dict
from stats import count_characters_list
import sys

#Checking whether script was called properly
if len(sys.argv) == 1:
	print("ERROR: no book specified. To run this program, pass in arguments in the format 'books/[bookname].txt'")
	sys.exit()
	
#Defining functions

def get_book_text(file_path):
	with open(file_path) as opened_book:
		book_contents = opened_book.read()
		return book_contents

def main(input_path):
	book_text = get_book_text(input_path)
	num_words = count_words(book_text)
	print(f"{num_words} words found in the document")
	num_characters_dict = count_characters_dict(book_text)
	#print(num_characters_dict)
	num_characters_list = count_characters_list(book_text)
	
	#prettyprint
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {input_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for each_minidict in num_characters_list:
		if each_minidict["character"].isalpha() == True:
			temp_key = each_minidict["character"]
			temp_count = each_minidict["the_count"]
			print(f"{temp_key}: {temp_count}")
		else:
			pass
	print("============= END ===============")
	print("")


#Running script
input_book_list = sys.argv[1:]
for each_book in input_book_list:
	main(each_book)

