using System;

class LeapYearDeterminant
{
    static void Main(string[] args)
    {
        Console.WriteLine("Введите год, который хотите проверить на високосность: ");
        int year = int.Parse(Console.ReadLine());
        if (year % 4 == 0 && year % 100 != 0)
        {
            Console.WriteLine("YES");
        } else if (year % 400 == 0)
        {
            Console.WriteLine("YES");
        } else
        {
            Console.WriteLine("NO");
        }
    }

}