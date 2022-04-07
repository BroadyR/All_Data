/*
Name:Broady Rivet
Date:2-14-22
Course:330 002
Quarter:W22
Project 2
*/
/*Find the distance between two coordinates on a 3d plane*/
dist((X1,Y1,Z1),(X2,Y2,Z2),Result):-
	sqrt(((X2-X1)*(X2-X1))+((Y2-Y1)*(Y2-Y1))+((Z2-Z1)*(Z2-Z1)), Y),
	Result is Y.

/*Find the length, a.k.a the magnitude, of the given vector*/
vecLength((X,Y,Z),Result):-
	sqrt((X*X)+(Y*Y)+(Z*Z),S),
	Result is S.

/*Find the unit vector of the given vector by dividing the coordinates by the vector magnitude*/
vecNorm((X,Y,Z),R):-
	vecLength((X,Y,Z),S),
	V is S,
	X2 is X/V,
	Y2 is Y/V,
	Z2 is Z/V,
	R = vec(X2, Y2, Z2).
	
/*Find the dot product of two vectors*/
vecDot((X1,Y1,Z1),(X2,Y2,Z2),Result):-
	D = ((X1*X2)+(Y1*Y2)+(Z1*Z2)),
	Result is D.

/*Find the angle between two given vectors and give it in radians.
	Do this by dividing the dot product over the product of both vectors' magnitudes. */
vecAngle((X1,Y1,Z1),(X2,Y2,Z2),Result):-
	vecDot((X1,Y1,Z1),(X2,Y2,Z2),Result1),
	vecLength((X1,Y1,Z1),Result2),
	vecLength((X2,Y2,Z2),Result3),
	N is Result1,
	D is Result2*Result3,
	Result is acos(N/D).
	
/*Check if the given vectors have a right angle in between themselves and if so then give true */
areOrthog((X1,Y1,Z1),(X2,Y2,Z2)):-
	vecAngle((X1,Y1,Z1),(X2,Y2,Z2),Result),
	Result=1.5707963267948966.

/*Find the cross product of two given vertices*/
vecCross((X1,Y1,Z1),(X2,Y2,Z2),Result):-
	X3 is Y1*Z2-Z1*Y2,
	Y3 is X2*Z1-Z2*X1,
	Z3 is X1*Y2-Y1*X2,
	Result=(X3,Y3,Z3).
	
/*Find the Vector projection of the first given vertex onto the second given vertex.
  Do this by taking the quotient of the dot product of both given vertexes and the squared magnitude 
  of the second vertex and multiplying that by each coordinate of the second vertex.*/
vecProj((X1,Y1,Z1),(X2,Y2,Z2),Result):-
	vecDot((X1,Y1,Z1),(X2,Y2,Z2),D),
	vecLength((X2,Y2,Z2),M),
	M1 is M*M,
	P is D/M1,
	X3 is X2*P,
	Y3 is Y2*P,
	Z3 is Z2*P,
	Result=(X3,Y3,Z3). 

/*Find the given distance from a point given on a 3D plane to a point on the same plane but that
  also on a vertex on the same plane.
  To do this create a new vertex between the two points and find the cross product of that.
  Find the magnitude of the cross product and the original vertex and divide the two for the answer.*/
distPointLine((X,Y,Z),(X1,Y1,Z1),(X2,Y2,Z2),Result):-
	X3 is X-X2,
	Y3 is Y-Y2,
	Z3 is Z-Z2,
	vecCross((X1,Y1,Z1),(X3,Y3,Z3),C),
	vecLength(C,M1),
	vecLength((X1,Y1,Z1),M2),
	Result is M1/M2.

/*Find the distance of a point that is not on a plane that contains a given point and vertex.
  This is done the same way as if the dot was in the plane but instead of the cross product you
  replace it with the dot product and only use the magnitude of the original given vertex.*/
distPointPlane((X,Y,Z),(X1,Y1,Z1),(X2,Y2,Z2),Result):-
	X3 is X-X2,
	Y3 is Y-Y2,
	Z3 is Z-Z2,
	vecDot((X1,Y1,Z1),(X3,Y3,Z3),D),
	vecLength((X1,Y1,Z1),M),
	Result is D/M.