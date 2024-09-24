using System;

class Program
{
    static void Main()
    {
        int a, b, temp;
        Console.Write("Введите значение a: ");
        a = Convert.ToInt32(Console.ReadLine());
        Console.Write("Введите значение b: ");
        b = Convert.ToInt32(Console.ReadLine());
        temp = a;
        while (temp != b)
        {
            a = temp;
            if (a < b)
            {
                temp = a;
                a = b;
                b = temp;
            }
            temp = a - b;
            a = b;
        }
        Console.WriteLine($"НОД: {b}");
    }
}