using System;
using System.ComponentModel;

namespace task4
{
    internal class Operation
    {
        public static double squareOfTriangle(double a, double b, double c)
        {
            return squareOfTriangleHelper(a, b, c);
        }

        public static double squareOfTriangle(double a)
        {
            return squareOfTriangleHelper(a, a, a);
        }

        public static double squareOfTriangleHelper(double a, double b, double c)
        {
            try
            {
                if (!isTriangle(a, b, c))
                {
                    throw new TriangleException();
                }
                double perimeter = a + b + c;
                double halfOfPerimeter = perimeter / 2;
                double square = Math.Sqrt(halfOfPerimeter * (halfOfPerimeter - a) * (halfOfPerimeter - a) * (halfOfPerimeter - a));
                return square;
            }
            catch (TriangleException e)
            {
                Console.WriteLine(e.Message);
                return 0;
            }
            catch (FormatException e)
            {
                Console.WriteLine("An format exception was thrown: {0}", e.Message);
                return 0;
            }
            catch (Exception e)
            {
                Console.WriteLine("An exception was thrown: {0}", e.Message);
                return 0;

            }
        }



        private static bool isTriangle(double a, double b, double c)
        {
            return (a < (b + c)) && (b < (a + c)) && (c < (a + b));
        }

        public class TriangleException : Exception
        {
            public TriangleException() : base("A triangle does not exist.")
            {
            }
        }
    }
}
