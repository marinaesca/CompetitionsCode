import java.util.Arrays;
import java.util.Scanner;
// Marina Escalante
// airport codes

public class Airports3
{
	public static void main(String[] args)
	{
		Scanner reader = new Scanner(System.in);
		int t = reader.nextInt();
		String[] answers = new String[t];

		for (int i = 0; i < t; i++)
		{
			int n = reader.nextInt(); // the priority amount
			String[] pri = new String[n];
			read(pri, reader);
			Arrays.sort(pri); // alphabetize

			int m = reader.nextInt(); // the total amount
			String[] total = new String[m];
			read(total, reader);
			Arrays.sort(total);

			// read in pri, fill in
			String ans = "";

			for (int j = 0; j < pri.length; j++)
			{
				String p = pri[j];
				for (int j2 = 0; j2 < total.length; j2++)
				{
					if (p.equals(total[j2]))
					{
						ans += total[j2] + "\n";
						total[j2] = "";
					}
				}
			}

			for (int j = 0; j < total.length; j++)
			{
				if (!total[j].equals(""))
				{
					ans += total[j] + "\n";
				}
			}

			answers[i] = ans;

		}

		for (int i = 0; i < answers.length; i++)
		{
			System.out.print(answers[i]);
		}
		reader.close();
	}

	public static void read(String[] list, Scanner reader)
	{
		for (int i = 0; i < list.length; i++)
		{
			list[i] = reader.next();
		}
	}
}
