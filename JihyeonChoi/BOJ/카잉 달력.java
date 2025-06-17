import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int M = sc.nextInt();
            int N = sc.nextInt();
            int x = sc.nextInt();
            int y = sc.nextInt();

            boolean found = false;
            int year = x;

            while (year <= M * N) {
                if ((year - 1) % N + 1 == y) {
                    found = true;
                    System.out.println(year);
                    break;
                }
                year += M;
            }

            if (!found) {
                System.out.println(-1);
            }
        }
    }
}
