import java.util.Scanner;
public class task08
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Give imput");
    int n = sc.nextInt();
    for (int i = 1;i<=n;i++)
    {
      for (int p = i;p<n;p++)
      {
        System.out.print(" ");
      }
      for (int k = 1;k<=i;k++){
        System.out.print(k);}
      System.out.println();
    }
  }
}