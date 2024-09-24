using System;

public struct Distance
{
    public double foot;
    public double inch;
}
class Program
{
    static void Main(string[] args)
    {
        try
        {
            Distance distance1;
            Distance distance2;
            Distance distance3;
            Console.WriteLine("Write foot count of the first distance: ");
            distance1.foot = double.Parse(Console.ReadLine());
            Console.WriteLine("Write inch count of the first distance: ");
            distance1.inch = double.Parse(Console.ReadLine());
            Console.WriteLine("Write foot count of the second distance: ");
            distance2.foot = double.Parse(Console.ReadLine());
            Console.WriteLine("Write inch count of the second distance: ");
            distance2.inch = double.Parse(Console.ReadLine());
            distance3.foot = distance1.foot + distance2.foot + ((int)(distance1.inch + distance2.inch)) / 12;
            distance3.inch = (distance1.inch + distance2.inch) % 12;
            Console.WriteLine("Sum of the distances is {0:F3}' - {1}\"", distance3.foot, distance3.inch);
        }
        catch (Exception e) 
        {
            Console.WriteLine(e.StackTrace);
        }

        
    }
}