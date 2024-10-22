class Program
{
    static void Main(string[] args)
    {
        Point p1 = new Point();
        p1.Show();
        Point p2 = new Point(12, 13);
        p2.Show();
        Line line = new Line(p1, p2);
        line.Show();
        double dtr = line.DlinL();
        Console.WriteLine("Длина отрезка " + dtr);
    }
}