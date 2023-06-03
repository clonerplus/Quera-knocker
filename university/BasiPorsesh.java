import java.util.Scanner;
public class BasiPorsesh {
	public static void xor(long[] nums, long[] inst) {
		long result;
		long[] lastResults = new long[inst.length];
		for (int i = 0; i < inst.length; i++) {
			if (lastResults[(int)inst[i]-1] != 0) {
				System.out.println(lastResults[(int)inst[i]-1]);
				continue;
			}
			result = 0;
			for (int j = 0; j < inst[i]; j++) {
				result += nums[j] ^ (inst[i] - j - 1);
			}
			System.out.println(result);
			lastResults[(int)inst[i]-1] = result;
		}
	}

	public static void main(String[] args) {long n, q, num;
    Scanner print = new Scanner(System.in);
    n = print.nextLong();
    q = print.nextLong();
    long[] nums = new long[(int) n];// numbers
    long[] inst = new long[(int) q];// instructions
    
    for (int i = 0; i < n; i++) {
        num = print.nextInt();
        nums[i] = num;
    }
    for (int i = 0; i < q; i++) {
        num = print.nextInt();
        inst[i] = num;
    }
    print.close();
    xor(nums, inst);
}

}

