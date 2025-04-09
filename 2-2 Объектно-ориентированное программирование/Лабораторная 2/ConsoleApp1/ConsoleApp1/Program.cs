using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    public static int res = 30;
    public static Func<int, int, int, int, int> f = (a, b, c, d) => a + 2 * b + 3 * c + 4 * d;
    public static Random r = new Random();
    
    static void Main(string[] args)
    {
        List<Generation> generations = new List<Generation>();
        for (int i = 0; i < 5; i++)
        {
            generations.Add(new Generation(f, r.Next(1, 10), r.Next(1, 10), r.Next(1, 10), r.Next(1, 10)));
        }
        int maxIterations = 1000;
        for (int i = 0; i < maxIterations; i++)
        {
            Console.WriteLine("Итерация " + (i + 1));
            foreach (var item in generations)
            {
                Console.WriteLine($"a = {item.a}, b = {item.b}, c = {item.c}, d = {item.d}, f(a,b,c,d) = {item.RealResult}");
            }
            Console.WriteLine("---");

            var best = generations.OrderBy(g => Math.Abs(g.RealResult - res)).ToList();

            if (best[0].RealResult == res)
            {
                Solution(best[0]);
                return;
            }
            generations.Clear();
            generations.Add(Generation.NewGen(best[0], best[1]));
            generations.Add(Generation.NewGen(best[1], best[0]));
            generations.Add(Generation.NewGen(best[0], best[2]));
            generations.Add(Generation.NewGen(best[2], best[0]));
            generations.Add(Generation.NewGen(best[1], best[2]));

            if (r.NextDouble() < 0.2)
            {
                generations[r.Next(0, generations.Count)].Mutate();
            }
        }
        Console.WriteLine("Не удалось найти решение за " + maxIterations + " итераций.");
    }
    public static void Solution(Generation g)
    {
        Console.WriteLine("Решение найдено:");
        Console.WriteLine($"a = {g.a}, b = {g.b}, c = {g.c}, d = {g.d}");
    }
}

