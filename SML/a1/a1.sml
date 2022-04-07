(*
	Broady Rivet
	12/14/21
	CSC 330 002
	Winter 2021-22
	Assignment #1
					*)
					
fun apply(func, []) = [] | apply(func, x::xs) = [func(x)]@apply(func, xs);

apply(fn x=>x*x, [1,2,3,4,5]);
apply(str, [#"a", #"b", #"c"]);