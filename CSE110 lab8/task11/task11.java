import java.util.Scanner;
public class task11
{
  public static void main (String [] args)
  {
    Scanner sc = new Scanner (System.in);
    System.out.println("ENter Quantity");
    int q = sc.nextInt();
    for (int i = 1;i<=q;i++)
    { int temp = 0;
      for (int j=1;j<=q-i;j++)
      {
        System.out.print(" ");
        temp = j;
      }
      for ( int k = temp+1;k<=q;k++)
      {
        System.out.print(k);
      }
      System.out.println();
    }
  }
}