using System;

class Program
{

    static void Main(string[] args)
    {
        Console.Write("n = ");
        int n = int.Parse(Console.ReadLine());
        // while: 
        Console.Write("\nwhile: \t\t");
        int i = 1;
        while (i <= n)
        {
            Console.Write(" " + i);
            i += 2;
        }
        // do while:
        Console.Write("\ndo while: \t");
        i = 1;
        do
        {
            Console.Write(" " + i);
            i += 2;
        }
        while (i <= n);
        // for:
        Console.Write("\nFor: \t\t");
        for (i = 1; i <= n; i += 2)
        {
            Console.Write(" " + i);
        }
        Console.WriteLine();
        int[] MyArray;
        int m = int.Parse(Console.ReadLine());
        MyArray = new int[m];
        for (int j = 0; i < MyArray.Length; ++j)
        {
            Console.Write("a[{0}]=", j);
            MyArray[j] = int.Parse(Console.ReadLine());
        }
        foreach (int x in MyArray) Console.Write("{0} ", x);


    }
}