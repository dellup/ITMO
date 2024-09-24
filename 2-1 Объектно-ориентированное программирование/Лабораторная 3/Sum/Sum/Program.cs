using System;
class Sum
{
    static void Main(string[] args)
    {
        Console.WriteLine("Введите k: ");
        int k = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите m: ");
        int m = int.Parse(Console.ReadLine());
        int s = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i > k && i < m) continue;
            s += i;
        }
        Console.WriteLine("Сумма по заданным параметрам: {0}", s);
    }
}