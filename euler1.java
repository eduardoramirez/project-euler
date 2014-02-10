public class euler1
{
  public static int calcSum(int n, int m, int hi)
  {
    int sum = 0;

    for(int i = 0; i < hi; i++)
    {
      if(i % n == 0 || i % m == 0)
        sum += i;
    }

    return sum;
  }

  public static void main(String[] args)
  {
    System.out.println(calcSum(3,5,1000));
  }
}
