
import java.io.*;
import java.net.*;
public class SWServer{
	ServerSocket reciever;
	Socket connection=null;
	ObjectOutputStream out;
	ObjectInputStream in;
	String packet,ack,data="";
	int i=0,sequence=0;
	SWServer(){}
	public void run(){
		try{
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			reciever = new ServerSocket(2005,10);
			System.out.println("waiting for connection...");
			connection=reciever.accept();
			sequence=0;
			System.out.println("Connection established   :");
			out=new ObjectOutputStream(connection.getOutputStream());
			out.flush();
			in=new ObjectInputStream(connection.getInputStream());
			out.writeObject("connected    .");

			do{
				try{
					packet=(String)in.readObject();
					if(Integer.valueOf(packet.substring(0,1))==sequence){
						data+=packet.substring(1);
						sequence=(sequence==0)?1:0;
						System.out.println("\n\nreceiver         >"+packet);
					}
					else
					{
						System.out.println("\n\nreceiver         >"+packet +"   duplicate data");
					}if(i<3){
						out.writeObject(String.valueOf(sequence));i++;
					}else{
						out.writeObject(String.valueOf((sequence+1)%2));
						i=0;
					}
				} catch(Exception e){}
			}while(!packet.equals("end"));
			System.out.println("Data recived="+data);
			out.writeObject("connection ended    .");
		}catch(Exception e){}
		finally{
			try{in.close();
				out.close();
				reciever.close();
			}
			catch(Exception e){}
		}
	}

	public static void main(String args[]){
		SWServer s=new SWServer();
		while(true){
			s.run();
		}
	}
}
