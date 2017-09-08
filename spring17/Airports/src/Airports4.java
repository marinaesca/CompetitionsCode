import java.util.Scanner;
// Marina Escalante
// airplane speed
/// rounding!
//!!! answer: you had to use a long bc overflow

public class Airports4
{
	public static void main(String[] args)
	{
		Scanner reader = new Scanner(System.in);
		int t = reader.nextInt();
		int[] answers = new int[t];

		for (int i = 0; i < t; i++)
		{
			int n = reader.nextInt(); // num data points
			double total = 0;
			int totalHours = 0;
			for (int j = 0; j < n; j++)
			{
				int mph = reader.nextInt();
				int hours = reader.nextInt();
				total += mph * hours;
				totalHours += hours;
			}

			answers[i] = (int) Math.round(total / totalHours);

		}

		for (int i = 0; i < answers.length; i++)
		{
			System.out.println(answers[i]);
		}
		reader.close();
	}
}
