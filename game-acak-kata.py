import random

def main():
	#assign the words
	words = ['buku','roti','mobil','motor','baju','kaki','tangan','mata','biru','merah']
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
		print(f"Tebak kata: {question}")
		userAns = input("Jawab: ")

		# keep asking user answer until the user input the right answer
		while userAns != ans:
			print("SALAH! Silakan coba lagi")
			userAns = input("Jawab: ")

		score +=1
		print(f"BENAR point anda : {score}")

		# remove the words that has been became a question
		words.remove(ans)

	#game is ended, no more words
	print("Yey anda telah menyelesaikan game!!!")

if __name__ == "__main__":
	main()
