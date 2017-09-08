import java.util.Scanner;

// Marina Escalante
// seat numbers
//!!! answer: you had to use a long bc overflow

public class Airports0
{
	public static void main(String[] args)
	{
		Scanner reader = new Scanner(System.in);
		int t = reader.nextInt();
		int[] answers = new int[t];

		for (int i = 0; i < t; i++)
		{
			String temp = reader.next();
			temp = temp.substring(0, temp.length() - 1); // remove letter on end
			int seat = Integer.parseInt(temp);
			answers[i] = seat * 6;
		}

		for (int i = 0; i < answers.length; i++)
		{
			System.out.println(answers[i]);
		}
		reader.close();
	}
}
