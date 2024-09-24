using System;

class DivideIt
{
    static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("Please enter the perimeter of the triangle: ");
            string temp = Console.ReadLine();
            int perimeter = Int32.Parse(temp);
            double a = perimeter / 3;
            double halfOfPerimeter = perimeter / 2;
            double square = Math.Sqrt(halfOfPerimeter * (halfOfPerimeter - a) * (halfOfPerimeter - a) * (halfOfPerimeter - a));
            Console.WriteLine("Сторона {0}; Площадь {1:F2}", a, square);
        }
        catch (FormatException e)
        {
            Console.WriteLine("An format exception was thrown: {0}", e.Message);
        }
        catch (Exception e)
        {
            Console.WriteLine("An exception was thrown: {0}", e.Message);
        }
    }
}