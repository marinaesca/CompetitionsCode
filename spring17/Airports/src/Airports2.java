import java.util.Scanner;
// Marina Escalante
// flight nums
// how do I convert to binary

public class Airports2
{
	public static void main(String[] args)
	{
		Scanner reader = new Scanner(System.in);
		int t = reader.nextInt();
		int[] answers = new int[t];

		for (int i = 0; i < t; i++)
		{
			int total = 0;
			int n = reader.nextInt();
			for (int j = 0; j < n; j++)
			{
				int temp = reader.nextInt();
				// turn into binary
				String binary = "" + temp;
				int ones = 0;
				for (int k = 0; k < binary.length(); k++)
				{
					if (binary.charAt(k) == '1')
					{
						ones++;
					}
				}
				if (ones % 2 == 1)
				{
					total++;
				}
			}
			answers[i] = total;
		}

		for (int i = 0; i < answers.length; i++)
		{
			System.out.println(answers[i]);
		}
		reader.close();
	}
}
