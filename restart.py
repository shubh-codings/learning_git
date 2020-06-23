from random import randint

actual = {'TOAC' : 'FIFTH', 'MP' : 'THIRD', 'CG' : 'THIRD', 'SPM' : 'SEVENTH', 'NN' : 'SEVENTH', 'ADV.JAVA' : 'SEVENTH', 'CD' : 'SEVENTH'}
subjects = [ 'TOAC', 'MP', 'CG', 'SPM', 'NN', 'ADV.JAVA', 'CD']
semesters = ['FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH']
guess = {}
for subject in subjects :
	for semester in range(1):
		print(subject, ' : ', semesters[randint(0,7)])
		guess.append(subject, ' : ', semesters[randint(0,7)])


