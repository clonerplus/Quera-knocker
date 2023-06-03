import java.util.Arrays;
import java.util.Scanner;

public class PythagoreanNumbers {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int[] sides = new int[3];
		
		for (int i = 0; i < 3; i++) {
			sides[i] = s.nextInt();

		}
		
                s.close();
		Arrays.sort(sides);
		
		if (Math.pow(sides[0], 2) + Math.pow(sides[1], 2) == Math.pow(sides[2], 2)) {
			System.out.println("YES");
			return;
		}
		System.out.println("NO");
		
		}
		
		
		
	

}

