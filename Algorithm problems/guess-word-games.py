import random

def main():
	#assign the words
	words = ['book','bread','car','motor','clothe','foot','hand','eyes','blue','red']
	score = 0

	#keep asking new question until no more words to ask
	while len(words) != 0:
		# get 1 word by random from array 'words'
		randomIndex = random.randint(0,len(words)-1)
		ans = words[randomIndex]

		# shuffle the string arrangement
		listAns = list(ans)
		random.shuffle(listAns)
		question = ''.join(listAns)
		
		# start asking question
		print(f"guess word: {question}")
		userAns = input("ans: ")

		# keep asking user answer until the user input the right answer
		while userAns != ans:
			print("WRONG! try again")
			userAns = input("ans: ")

		score +=1
		print(f"RIGHT! your points : {score}")

		# remove the words that has been became a question
		words.remove(ans)

	#game is ended, no more words
	print("Congrats! You Have Finish The game!!!")

if __name__ == "__main__":
	main()
