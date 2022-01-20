// Even Fibonacci numbers

public class p002 {
  int LIMIT = 4_000_000;

  public static void main(String[] args) {
    System.out.println(new p002().solve());
  }

  public Integer solve() {
    double phi = 0.5 * (1 + Math.pow(5, 0.5));
    int fibs = (int) (Math.ceil(Math.log(LIMIT * Math.pow(5, 0.5)) / Math.log(phi)));
    int[] table = new int[fibs];
    int sum = 0;

    for (int i = 1; i < fibs; i += 3) {
      int x = fibonacci(i, table);
      if (x < LIMIT) sum += x;
    }
    return sum;
  }

  public Integer fibonacci(int n, int[] table) {
    if (n == 0) table[0] = 1;
    if (n == 1) table[1] = 2;
    if (table[n] != 0) return table[n];
    table[n] = fibonacci(n - 1, table) + fibonacci(n - 2, table);
    return table[n];
  }
}
