import java.util.Scanner;


public class lengthAndSumOfNumbers {
	public static String highestNumMaker(int Length, int sum) {
		String firstDigits = "", fullDigits;
		for(int i = 0; i < sum/9; i++) {// adding 9 as many as we can to the first digits
			firstDigits += "9";
		}
		if (Length != firstDigits.length()) {// if first digits ate not already at full length
			firstDigits += Integer.toString(sum%9);
		}
		
		fullDigits  = firstDigits;
		
		int remDigits = Length - firstDigits.length();
		
		for (int i = 0; i < remDigits; i++) {// adding as many as "0"s to the end of the number
			fullDigits += "0";
		}
		
		return fullDigits;
		
	}
	/*
	 * This function calculates the very first number that has a sum "s" and the length "m"
	 */
	public static String lowestNumMaker(int Length, int sum) {
		String lastDigits = Integer.toString(sum%9);// first adds the remaining of devision by 9 to the last digits
		
		for(int i = 0; i < sum/9; i++) {// then adds as many as possible "9"s to the end of the last digits
			lastDigits += "9";
		}


		String fullDigits = "";
		if (Length - lastDigits.length()-1 >= 0) {// if there is room for a 1 at first digit spot
			fullDigits += "1";
		}
		for (int i = 0; i < Length - lastDigits.length()-1; i++) {// adding as many "0"s as possible after 1
			fullDigits += "0";
		}
		
		
		if (Length - lastDigits.length()-1 < 0) {// if there is no 1 at the end of last digits
			String updatedFirstDigitOfLast = 
					Integer.toString(Integer.parseInt(lastDigits.substring(0, 1)) + 1);// adds one to the first digit that we subtracted when calling the function

			fullDigits = 
					updatedFirstDigitOfLast + lastDigits.substring(1, lastDigits.length());

		} else
			fullDigits += lastDigits;// no need for any addition we have 1 at the first 
		
		return fullDigits;
	}

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int m, s;
		m = a.nextInt();// 1 ≤ m ≤ 100
		s = a.nextInt();// 0 ≤ s ≤ 900
		a.close();
		
		if (m == 1 && s == 0) {
			System.out.println("0 0");
			return;
		}
		
		if (s > m*9 || s == 0) {
			System.out.println("-1 -1");
		
		} else {
			System.out.print(lowestNumMaker(m, s-1) + " ");
			System.out.println(highestNumMaker(m, s));
		
		}
	}

}
