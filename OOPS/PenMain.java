package OOPS;
//main class to demonstrate the Pen class functionality
public class PenMain {
    public static void main(String[] args) {
        Pen pen1 = new Pen();
        pen1.colour = "Red";
        pen1.type = "Gel";
        Pen pen2 = new Pen();
        pen2.colour = "Black";
        pen2.type = "Ballpoint";

        pen1.write();
        pen2.write();
    }
}
    

 