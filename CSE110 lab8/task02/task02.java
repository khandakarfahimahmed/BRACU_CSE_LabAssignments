import java.util.Scanner;
public class task02
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner (System.in);
    System.out.println ("Enter a digit");
    int q = sc.nextInt();
    for (int i = 1;i<=q;i++)
      System.out.print("*");
    System.out.println();
  }
}