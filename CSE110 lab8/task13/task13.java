import java.util.Scanner;
public class task13
{
  public static void main (String [] args)
  {
    Scanner sc = new Scanner (System.in);
    System.out.println("ENter Quantity");
    int q = sc.nextInt();
    int star = 1,l = q;
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
      System.out.println();}
      for(int z=q-1;z>=1;z--)
     {
         for(int j=z;j<q;j++)
         {
             System.out.print(" ");
         }
         for(int j=1;j<=(2*z-1);j++)
         {
             System.out.print(j);
         }
         System.out.println("");
     } 
    }
  }

    