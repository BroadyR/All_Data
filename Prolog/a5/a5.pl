/*
Name:Broady Rivet
Date:1-28-22
Course:330 002
Quarter:W22
Assignment:a5
*/
/*
piecewise input is 1 then output is 3
*/
myfun(0, 3).
/*
piecewise input is 2 then output is 4
*/
myfun(1, 7).
/*
otherwise, commense the piecewise function
*/
myfun(N,Result):-
	integer(N),
	N > 1,
	X1 is N-1,
	X2 is N-2,
	myfun(X1, Result1),
	myfun(X2, Result2),
	Result is Result1 + Result2.
/*
is the first and second argument the same? If so print only one
*/
fill(X,X,[X]).
/*
else add 1 to the head and continue until you reach the tail
*/
fill(X,Y,[X|Xs]):- 
	X2 is X+1, 
	X2 =< Y, 
	fill(X2,Y,Xs).
	