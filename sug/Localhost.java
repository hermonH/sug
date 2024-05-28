import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;
public class Localhost {
    public static void main(String[] args) {
        try {
            System.out.println("ENTER SEVER NAME");
            Scanner sc = new Scanner(System.in);
            String host=sc.next();
            System.out.println(InetAddress.getLocalHost());
            System.out.println(InetAddress.getByName(host));
            sc.close();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }  
}
