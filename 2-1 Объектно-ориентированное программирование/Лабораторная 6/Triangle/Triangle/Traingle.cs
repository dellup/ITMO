class Triangle
{
    private double a;
    private double b;
    private double c;
    public Triangle(double a, double b, double c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public void show()
    {
        Console.WriteLine("Стороны треугольника: {0}; {1}; {2}", a, b, c);
    }
    public double perimeter()
    {
        return a + b + c;
    }
    public double square()
    {
        double halfOfPerimeter = perimeter() / 2;
        return Math.Sqrt(halfOfPerimeter * (halfOfPerimeter - a)*(halfOfPerimeter - b)*(halfOfPerimeter - c));
    }
    public bool isTrinalge()
    {
        return (a < b + c) && (b < a + c) && (c < a + b);
    }
}