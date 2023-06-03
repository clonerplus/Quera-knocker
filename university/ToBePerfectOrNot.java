import java.util.Scanner;

public class ToBePerfectOrNot {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int input = s.nextInt(), itraitor = 1, count = 0;
		
		while (itraitor <= input / 2) {
			if (input % itraitor == 0)
				count += itraitor;
			itraitor += 1;
			
			
		}
		if (count == input) {
			System.out.println("YES");
			return;
		}
		
		System.out.println("NO");
	}

}

