(* 
	Broady Rivet
	12/14/21
	CSC 330 002
	Winter 2021-22
	Project 1
*)

(*This function is to retrieve the file and name it as a string to read*)
fun parse(fName) = 
	let
		val file = TextIO.openIn(fName)
		fun currentChar() = TextIO.input1(file)
		fun nextChar() = TextIO.lookahead(file)
		
		(* function that checks if character is a digit and returns bool*)
		fun isDigit(SOME a) = 
			if ord(a) >= 48 andalso ord(a) <= 57 then true
			else false
		|isDigit(NONE) = false
		
		(* checks current character then checks if next character is also a digit *)
		fun multiDig(SOME a) = 
			if isDigit(nextChar())
				(*valof takes a option -> a*)
				then Option.valOf(SOME a)::multiDig(currentChar())
			else Option.valOf(SOME a)::[] (*base case*)
		| multiDig(NONE) = []
		
		(* checks if the current charcater is ~ then returns a bool *)
		fun isTild(SOME a) = 
			if ord(a) = 126 
				then true
			else false
		|isTild(NONE) = false
		
		(*This function is a recursive function that goes through the list and checks if the
			is a digit, ~, or neither. converts Char list to string to int optin to int to be put into an int list*)
		fun parser(SOME Char) =
			if isDigit(SOME Char) orelse isTild(SOME Char)
				then
					if isTild(SOME Char) andalso not(isDigit(nextChar()))
						then parser(currentChar())
						(*implode char list -> string*)
					else Option.valOf(Int.fromString(implode(multiDig(SOME Char))))::parser(currentChar())
			else 
				parser(currentChar())
		| parser(NONE) = []
	in
		(* main function call to begin the parser function *)
		parser(currentChar())
	end;

