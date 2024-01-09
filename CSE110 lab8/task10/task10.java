import java.util.Scanner;
public class task10
{
  public static void main (String [] args)
  {
    Scanner sc = new Scanner (System.in);
    System.out.println("ENter Quantity");
    int q = sc.nextInt();
    int star = 1;
    for (int i = 1;i<=q;i++)
    {
      for (int p =1;p<=q-i;p++)
      {
        System.out.print(" ");
      }
      for (int k = 1; k<=star;k++)
      {
        System.out.print(k);
      }
      star+=2;
      System.out.println();
    }
  }
}