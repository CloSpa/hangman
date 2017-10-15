import random

#NUMBER OF ROUNDS
tries = 8

letters_status = {}

words_list=["magic", "fish", "wine", "whisky", "couch", "mojito",
	"humus", "turtle", "music", "laptop"]

all_saved_scores = {}

word = random.choice(words_list)
printed_word = word
remaining_letters = len(word)