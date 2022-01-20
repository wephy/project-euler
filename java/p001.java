// Multiples of 3 and 5

public class p001 {
  int LIMIT = 1000;

  public static void main(String[] args) {
    System.out.println(new p001().solve());
  }

  public Integer solve() {
    int sum = 0;
    for (int i = 0; i < LIMIT; i++) {
      if (i % 3 == 0 || i % 5 == 0) sum += i;
    }
    return sum;
  }
}
