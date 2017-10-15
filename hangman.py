import os
import functions
import pickle

#ASK PLAYER'S NAME
name = str(input("Enter player's name :")).lower()

while name.isalpha() is False:
	name = str(input("Please, letters only, this is no arcade game :"))

#CHECK IF USER IS NEW
functions.new_user(name, functions.all_saved_scores)

scores_pickled = open("scores", "rb")
functions.all_saved_scores = pickle.load(scores_pickled)
scores_pickled.close()

print("\nThe current scores are", functions.all_saved_scores)

#NO LETTER HAS BEEN FOUND YET
for letter in functions.word:
	functions.letters_status[letter] = False

#START GAME
while functions.should_keep_going(functions.tries, functions.remaining_letters) is True:
	functions.check_word_progress(functions.letter, functions.word, functions.letters_status)

#UPDATE PLAYER'S SCORE
functions.all_saved_scores[name] += functions.tries
print("\nThe scores are now", functions.all_saved_scores)

#SAVE NEW SCORE IN FILE
scores_pickled = open("scores", "wb")
pickle.dump(functions.all_saved_scores, scores_pickled)
scores_pickled.close()