/*
Name:Broady Rivet
Date:1-28-22
Course:330 002
Quarter:W22
Assignment:a5
*/

intsum(Filename,Filename2):- 
	see(Filename),
	tell(Filename2),
	/*get reads the actual value instead of the ascii*/
	get(X),
	process(X,0,R),
	write(R),
	nl,
	seen,
	told.
	
process(-1,R,R).

process(X,Y,R):- 
	X \= -1,
	/*-48 converts back to the ascii value*/
	Y2 is Y+X-48,
	get(X2),
	process(X2,Y2,R).