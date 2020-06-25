from random import randint


#trying to built a guessing game in which a random guess is match with an actual answer to see if it is correct
#in this i m trying to use random number generated through random module
#here actual is the correct answer which will be matched with the response that we will generate using randint function
#subjects and list are two list from which a random guess can be generated


actual = {'TOAC' : 'FIFTH', 'MP' : 'THIRD', 'CG' : 'THIRD', 'SPM' : 'SEVENTH', 'NN' : 'SEVENTH', 'ADV.JAVA' : 'SEVENTH', 'CD' : 'SEVENTH'}
subjects = [ 'TOAC', 'MP', 'CG', 'SPM', 'NN', 'ADV.JAVA', 'CD']
semesters = ['FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH']
#created an empty dictionary
guess = {}

# using iteration and random  created a random dictionary
for subject in subjects :
	for i in range(1):
		#randint(a,b ) gives a random integer between a nd b 
		a = semesters[randint(0,7)]
		#print(subject , ' : ', a )
		guess[subject] = a

#created a count variable to count the number of correct gueses

count = 0
for i in guess.items():
	for j in actual.items():
		if i == j:
			count+=1	
	

print('Correct answers')
print(actual)
print("Guessed answers")
print (guess)
print("You have made " + str(count) +" correct guess/guesses")
		


