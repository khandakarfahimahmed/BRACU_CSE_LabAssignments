import java.util.Scanner;
public class task24 
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter number");
    int n = sc.nextInt();
    for (int i = 1;i<=n;i++)
    {
      System.out.print(i);
    }
    for (int i=n-1;i>=1;i--)
    {
      System.out.print(i);
    }
  }
}
