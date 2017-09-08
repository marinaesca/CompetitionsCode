import java.util.Scanner;

// Marina Escalante
// overbooked
// !!! answer: you had to use a long bc overflow

public class Airports1
{
	public static void main(String[] args)
	{
		Scanner reader = new Scanner(System.in);
		int t = reader.nextInt();
		int[] answers = new int[t];

		for (int i = 0; i < t; i++)
		{
			int n = reader.nextInt(); // num passengers
			int m = reader.nextInt(); // max
			int b = n - m; // bribes

			// array of bribes
			// read in each passenger asking
			// check lower than inside that array

			int[] bribes = new int[b];
			for (int j = 0; j < b; j++) // fill up with first people
			{
				bribes[j] = reader.nextInt();
			}

			for (int j = 0; j < m; j++) // read in other passengers
			{
				int passenger = reader.nextInt();
				int k = 0;
				while (k < b)
				{
					if (passenger < bribes[k])
					{
						bribes[k] = passenger;
						k = b;
					}
					k++;
				}
			}

			int sum = 0;
			for (int j = 0; j < b; j++)
			{
				sum += bribes[j];
			}
			answers[i] = sum;

		}

		for (int i = 0; i < answers.length; i++)
		{
			System.out.println(answers[i]);
		}
		reader.close();
	}
}
