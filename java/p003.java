// Largest prime factor

public class p003 {
  long NUMBER = 600_851_475_143L;

  public static void main(String[] args) {
    System.out.println(new p003().solve());
  }

  public long solve() {
    long x = NUMBER;
    long i = 2;
    while (i < x) {
      if (x % i == 0) x /= i;
      else i++;
    }
    return i;
  }
}
