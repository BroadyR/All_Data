/*
NAME(S): Broady Rivet
DATE: 1-24-22
COURSE: 330 002
QUARTER: W22
ASSIGNMENT: a4

*/

inv(
	item(bread),
	price(0.90),
	quantity(50)
).

inv(
	item(milk),
	price(2.50),
	quantity(30)
).

inv(
	item(cheese),
	price(1.50),
	quantity(80)
).

inv(
	item(chips),
	price(1.00),
	quantity(50)
).

inv(
	item(apples),
	price(0.30),
	quantity(100)
).

/* Add your predicates below here */

getPrice(Item,Price):- inv(item(Item),price(Price),_).

getQuantity(Item,Quantity):- inv(item(Item),_,quantity(Quantity)).

higherPrice(Item1,Item2):- getPrice(Item1,A), getPrice(Item2,B), A>B.

computeGross(Item,Gross):- getPrice(Item,A), getQuantity(Item,B), Gross is A*B.

higherGross(Item1,Item2):- computeGross(Item1,A), computeGross(Item2,B), A>B.
