(*
	Broady Rivet
	12/20/21
	CSC 330 0002
	Winter 2021-2022
	Assignment 3
*)
fun fsum(fileName) =
	let
		val file = TextIO.openIn(fileName)
		fun makeList(file) = if TextIO.endOfStream(file) then [] (*helper function that string -> it option list by reading a called file*)
			else Int.fromString(Option.valOf(TextIO.inputLine(file)))::makeList(file)
		fun sum ([]) = 0 (*recursive sum function to add all integers read together*)
			| sum(SOME(x)::xs) = x + sum(xs)
			| sum(NONE::xs) = sum(xs)
	in 
		sum(makeList(file))(*calls the newly read integers int the sum fution*)
	end;

(*use "a3.sml"; fsum("input.txt")*)