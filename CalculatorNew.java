import java.util.Scanner;
public class CalculatorNew {
     public static void main(String[] args){
            Scanner in = new Scanner(System.in);
            //Take input from user
    
            while (true) { 
                //Take operator as input
                char op = in.next().trim().charAt(0);
                if(op=='+' || op=='-' || op=='*'|| op=='/' || op=='%'){
                    // Input two numbers
                    int num1 = in.nextInt();
                    int num2 = in.nextInt();
                    
                    if(op=='+'){
                        System.out.println(num1+num2);
                    }
                    if(op=='-'){
                        System.out.println(num1-num2);
                    }
                    if(op=='*'){
                        System.out.println(num1*num2);
                    }
                    if(op=='/'){
                        if(num2 != 0){
                            System.out.println(num1/num2);
                        }   
                    }
                    if(op=='%'){
                        System.out.println(num1%num2);
                    }
                    else if(op=='X' || op=='x'){
                        break;
                    }
                    else{
                        System.out.println("invalid operation");
                    }
    
                    
    
                }
            }
            
        }

    
}
