#!/usr/bin/env python3

import random

wrds = ["brass", "basin", "bolos", "brain", "brink", "boink", "brick", "blobs", "blade", "brush", "basil", "break", "bleak", "beard"]
print (wrds)

random.shuffle(wrds)
word = wrds[1]
print("The starting letter is " + word[0])
i = 10
while i > 0:
	guess = input("GUESS: ")
	if not guess:
		i -= 1
		print("You wasted a guess!")
	elif len(guess) != 5:
		print("0, 1, 2, 3, 4 that's how we count to 5!")
	elif guess[0].lower() != 'b':
		print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	elif guess != word:
		i -= 1
		print("Good Try! You have %d guesses left" % (i))
	else:
		print("Good Job! You are one with the Source")
		break
