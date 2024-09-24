using System;
using task4;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Введите 1, если хотите найти площадь равностороннего треугольника, и 2, если треугольник неравносторонний: ");
        try
        {
            int choise = int.Parse(Console.ReadLine());
            if (choise == 1)
            {
                Console.WriteLine("Введите сторону треугольника, чтобы узнать его площадь: ");
                double a = double.Parse(Console.ReadLine());
                double square = Operation.squareOfTriangle(a);
                if (square != 0.0) Console.WriteLine("Площадь равностороннего треугольника со стороной {0} равна {1}", a, Operation.squareOfTriangle(a));
            } else if (choise == 2)
            {
                Console.WriteLine("Введите 3 стороны треугольника в одну строку через пробел, чтобы узнать его площадь: ");
                string[] str  = Console.ReadLine().Split(" ");
                double a = double.Parse(str[0]);
                double b = double.Parse(str[1]);
                double c = double.Parse(str[2]);
                double square = Operation.squareOfTriangle(a, b, c);
                if (square != 0.0) Console.WriteLine("Площадь треугольника со сторонами {0}; {1}; {2}; равна {3}", a, b, c, square);
            } else
            {
                throw new Exception("Неверный ввод. Пробуйте еще");
            }
        } catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}