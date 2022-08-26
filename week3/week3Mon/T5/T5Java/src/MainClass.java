import java.util.ArrayList;
import java.util.Scanner;

public class MainClass {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        /* b : buy cost */
        ArrayList<Integer> b = new ArrayList<>();
        /* s : sell price */
        ArrayList<Integer> s = new ArrayList<>();
        ArrayList<Integer> m = new ArrayList<>();
        /* f[i][j] implements total cost of a bike aged i in year j */
        int[][] f = new int[1005][1005];
        for (int i = 0; i < n; i++) {
            b.add(sc.nextInt());
        }
        for (int i = 0; i < n; i++) {
            s.add(sc.nextInt());
        }
        for (int i = 0; i < n; i++) {
            m.add(sc.nextInt());
        }
        for (int j = 1; j <= n; j++) {
            for (int i = 1; i <= j; i++) {
                if (i == 1) {
                    if (j == 1) {
                        f[i][j] = b.get(0) + m.get(0);
                    } else {
                        int temp = Integer.MAX_VALUE / 2;
                        for (int k = 2; k < j; k++) {
                            temp = Math.min(temp, f[k][j - 1] - s.get(j - 2) + b.get(j - 1) + m.get(0));
                        }
                        f[i][j] = temp;
                    }
                } else {
                    f[i][j] = f[i - 1][j - 1] + m.get(i - 1);
                }
            }
        }
        int temp = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            temp = Math.min(temp, f[i][n] - s.get(i - 1));
        }
        System.out.println(temp);
        /*for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                System.out.println("f[" + i + "][" + j + "]=" + f[i][j]);
            }
        }*/
    }
}
