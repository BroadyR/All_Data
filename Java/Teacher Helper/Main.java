//was walked through the code for main.java by classmate
import java.util.Scanner;

public class Main {
    // Method to evaluate value of a postfix expression
    static String evaluatePostfix(String exp)
    {
        //create a stack
        Stack stack = new Stack();

        // Scan all characters one by one
        for(int i = 0; i < exp.length(); i++)
        {
            char c = exp.charAt(i);

            if(c == ' '){
                continue;
            }
                // If the scanned character is an operand
                // (number here),extract the number
                // Push it to the stack.
            else if(Character.isDigit(c)) {
                //push the number in stack
                stack.Push(String.valueOf(c));
            }

            // If the scanned character is an operator, pop two
            // elements from stack apply the operator
            else
            {
                int val1 =  Integer.valueOf(stack.Pop());
                int val2 = Integer.valueOf(stack.Pop());

                switch(c)
                {
                    case '+':
                        stack.Push(String.valueOf(val2+val1));
                        break;

                    case '-':
                        stack.Push(String.valueOf(val2-val1));
                        break;

                    case '/':
                        stack.Push(String.valueOf(val2/val1));
                        break;

                    case '*':
                        stack.Push(String.valueOf(val2*val1));
                        break;
                }
            }
        }
        return stack.Pop();
    }
    public static void main(String[] args) {
       Stack a1 = new Stack();
       Stack a2 = new Stack();
       Queue c = new Queue();
       System.out.println("Enter the equation(This only supports A,B,C,D,E,F):");
       Scanner userinput1 = new Scanner(System.in);
       String inputequation = userinput1.nextLine();
       String split = "";
       String[] equation = inputequation.split(split);
       int x;
       for (x = 0; x < equation.length; x++) {
            switch (equation[x]) {
                case "A":
                    Node b1 = new Node();
                    b1.setData(equation[x]);
                   c.enqueue(equation[x]);
                    break;
                case "B":
                    Node b2 = new Node();
                    b2.setData(equation[x]);
                    c.enqueue(equation[x]);
                    break;
                case "C":
                    Node b3 = new Node();
                    b3.setData(equation[x]);
                    c.enqueue(equation[x]);
                    break;
                case "D":
                    Node b4 = new Node();
                    b4.setData(equation[x]);
                    c.enqueue(equation[x]);
                    break;
                case "E":
                    Node b5 = new Node();
                    b5.setData(equation[x]);
                    c.enqueue(equation[x]);
                    break;
                case "F":
                    Node b6 = new Node();
                    b6.setData(equation[x]);
                    c.enqueue(equation[x]);
                    break;

                case "+":
                    if(a2.Peek() == null){
                        a2.Push(equation[x]);
                    }
                    else if (a2.Peek().equals("+") | a2.Peek().equals("-")|a2.Peek().equals("(")) {
                        a2.Push(equation[x]);
                    } else if (a2.Peek().equals("/") | a2.Peek().equals("*")) {
                        while (a2.Peek() != null&&((a2.Peek().equalsIgnoreCase("/") | a2.Peek().equalsIgnoreCase("*"))) ){c.enqueue( a2.Pop());}
                        a2.Push(equation[x]);

                    }
                break;

                case "(":
                    a2.Push(equation[x]);
                    break;

                case ")":
                    while(!a2.Peek().equals("(")){
                        c.enqueue(a2.Pop());
                    }
                    a2.Pop();
                    break;

                case "-":
                    if(a2.Peek() == null){
                        a2.Push(equation[x]);
                    }
                    else if (a2.Peek().equals("+") | a2.Peek().equals("-")|a2.Peek().equals("(")) {
                        a2.Push(equation[x]);
                    } else if (a2.Peek().equals("/") | a2.Peek().equals("*")) {
                        while (a2.Peek() != null&&((a2.Peek().equalsIgnoreCase("/") | a2.Peek().equalsIgnoreCase("*"))) ){c.enqueue( a2.Pop());}
                        a2.Push(equation[x]);

                    }
                    break;


                case "*":
                    Node b9 = new Node();
                    b9.setData(equation[x]);
                    if(a2.Peek() == null){
                        a2.Push(equation[x]);}
                    else if (a2.Peek().equals("+") | a2.Peek().equals("-")| a2.Peek().equals("/") | a2.Peek().equals("*")|a2.Peek().equals("(")) {
                        a2.Push(equation[x]);
                    }
                    break;

                case "/":
                    Node b10 = new Node();
                    b10.setData(equation[x]);
                    if(a2.Peek() == null){
                        a2.Push(equation[x]); }
                    else if (a2.Peek().equals("+") | a2.Peek().equals("-")|a2.Peek().equals("/") | a2.Peek().equals("*")|a2.Peek().equals("(")) {
                        a2.Push(equation[x]);
                    }
                    break;

                default:
                    while (a2.Peek() != null) {
                        a1.Push(a2.Pop());
                    }
            }

        }
        while(a2.Peek() !=null){
            c.enqueue(a2.Pop());
        }
        int queueLength = c.GetSize();
        String[] postFix =new String[queueLength];
       for(int i = 0; i< (queueLength); i++) {
            postFix[i] = c.DeQueue();
        }
       for(int i = 0; i< queueLength; i++) {
        switch(postFix[i]){
            case"A":
                System.out.println("What does 'A' equal?");
                String inputequation2 = userinput1.nextLine();
                postFix[i] = inputequation2;
                break;
            case"B":
                System.out.println("What does 'B' equal?");
                String inputequation3 = userinput1.nextLine();
                postFix[i] = inputequation3;
                break;
            case"C":
                System.out.println("What does 'C' equal?");
                String inputequation4 = userinput1.nextLine();
                postFix[i] = inputequation4;
                break;
            case"D":
                System.out.println("What does 'D' equal?");
                String inputequation5 = userinput1.nextLine();
                postFix[i] = inputequation5;
                break;
            case"E":
                System.out.println("What does 'E' equal?");
                String inputequation6 = userinput1.nextLine();
                postFix[i] = inputequation6;
                break;
            case"F":
                System.out.println("What does 'F' equal?");
                String inputequation7 = userinput1.nextLine();
                postFix[i] = inputequation7;
                break;
        }
       }
        String Equation= "";
       for (int i = 0; i< queueLength; i++){
           Equation += postFix[i];
       }
       System.out.println(Equation);
       System.out.println(evaluatePostfix(Equation));
    }
}
