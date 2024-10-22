class Program
{
    static void Main(string[] args)
    {
        Triangle triangle = new Triangle(17, 22, 12);
        triangle.show();
        Console.WriteLine(triangle.perimeter());
        Console.WriteLine(triangle.square());
        Console.WriteLine("Треугольник существует? \n{0}", triangle.isTrinalge());
    }
}