using System;

namespace Utils
{
    class Program
    {
        static void Main(string[] args)
        {
            int x;
            int y;
            

            Console.WriteLine("Введите первое число:");
            x = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите второе число:");
            y = int.Parse(Console.ReadLine());
            int greater = Utils.Greater(x, y);
            Console.WriteLine("Большим из чисел {0} и {1} является {2}", x , y , greater);
            Console.WriteLine("До swap: \t" + x + " " + y);
            Utils.Swap(ref x, ref y);
            Console.WriteLine("После swap: \t" + x + " " + y);

            int f;
            bool ok;
            Console.WriteLine("Number for factorial:");
            x = int.Parse(Console.ReadLine());
            // Test the factorial function 
            ok = Utils.Factorial(x, out f);
            // Output factorial results 
            if (ok)
                Console.WriteLine("Factorial(" + x + ") = " + f);
            else
                Console.WriteLine("Cannot compute this factorial");
        }
    }
}
