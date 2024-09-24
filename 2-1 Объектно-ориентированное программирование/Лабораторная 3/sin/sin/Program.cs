using System;

class Program
{
    static void Main()
    {
        double x;
        double x1;
        double x2;
        double y;

        Console.Write("Введите нижнюю границу интервала x1: ");
        x1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Введите верхнюю границу интервала x2: ");
        x2 = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("x      |   sin(x)");
        x = x1;
        do
        {
            y = Math.Sin(x);
            Console.WriteLine($"{x:F2}   |   {y:F4}");
            x += 0.01;
        } while (x <= x2);
    }
}