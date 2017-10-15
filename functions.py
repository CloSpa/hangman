from data import *
import pickle
letter = "1"

def new_user(name, all_saved_scores):
	scores_pickled = open("scores", "ab")
	pickle.dump(all_saved_scores, scores_pickled)
	scores_pickled.close()

	scores_pickled = open("scores", "rb")
	all_saved_scores = pickle.load(scores_pickled)

	#CREATE NEW PLAYER
	if name not in all_saved_scores:
		all_saved_scores[name] = 0
	
	scores_pickled.close()

	scores_pickled = open("scores", "wb")
	pickle.dump(all_saved_scores, scores_pickled)
	scores_pickled.close()

def should_keep_going(tries, remaining_letters):
	if tries < 1:
		print("\nYou should have guessed :", word)
		print("\nYou loose. I'm sure you did your best though. Sad.")
		return False
	if remaining_letters < 1:
		print("Congrats, you've made it! Now go eat a piece of cake, you deserve it, gorgeous.")
		return False			
	return True
	
def check_word_progress(letter, word, letters_status):
	global tries
	global remaining_letters
	print("You have", tries, "rounds left and", remaining_letters, "letters left to find")

	#ASK FOR LETTER
	letter = input("\nPick a letter : ").lower()
	while letter.isalpha() is False or len(letter) != 1:
		letter = input("Please pick an actual letter, and only one :")

	#COMPARE LETTER TO WORD
	if letter in word:
		if letters_status[letter] == True:
			print("\nYou've already entered this letter, dummy.\nThus, you still deserve to loose a round.\nDummy.")
		if letters_status[letter] == False:
			remaining_letters -= word.count(letter)
			letters_status[letter] = True

	#UPDATE NUMBER OF ROUNDS
	tries -= 1
	
	#UPDATE WORD
	printed_word = word
	word_update(printed_word, letters_status)

def word_update(printed_word, letters_status):
		for key, value in letters_status.items():
			if value is False:
				printed_word = printed_word.replace(key, "*")
		print("\n")
		print(printed_word)