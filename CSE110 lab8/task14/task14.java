import java.util.Scanner;
public class task14
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter row");
    int h = sc.nextInt();
    System.out.println("Enter collumn");
    int w = sc.nextInt();
    for (int i = 0; i < h; i++) 
    { 
      System.out.println(); 
      for (int j = 0; j < w; j++) 
      { 
        if (i == 0 || i == h-1 || 
            j== 0 || j == w-1) 
          System.out.print("*"); 
        else
          System.out.print(" "); 
      } 
    }
  }
}
