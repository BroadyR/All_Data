(*
	Broady Rivet
	12/16/21
	CSC 330-002
	Winter 2021-22
	Assignment 2
*)

fun optconcat [] = ""
	| optconcat((SOME x)::xs) = str(x) ^ optconcat(xs)
	| optconcat(NONE::xs) = optconcat(xs);

optconcat([SOME #"b",NONE,SOME #"o",SOME #"o",NONE]);
optconcat([NONE,NONE]);