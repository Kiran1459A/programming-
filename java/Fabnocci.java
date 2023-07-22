import java.io.*;
class Fabnacci{
    public static void display(int a, int b){
        for(int i=0;i<10;i++){
            int c=a+b;
            a=b;
            b=c;
            System.out.println(c);}
            

    }
   public static void main(String args[]){
        int a,b;
        a=0;
        b=1;
        display(a,b);
        
        }
        
        
    
    
}