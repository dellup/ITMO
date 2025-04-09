using System;
using System.Collections.Generic;
using static System.Runtime.InteropServices.JavaScript.JSType;

class Program
{
    static int HashString(string s, int p, int mod)
    {
        int[] p_pow = new int[p];
        p_pow[0] = 1;
        for (int i = 1; i < p; i++)
        {
            p_pow[i] = p_pow[i - 1] * p;
        }

        int hash = 0;
        for (int i = 0; i < s.Length; i++)
        {
            hash = (hash + (s[i] * p_pow[i])) % mod;
        }
        return hash;
    }

    static void Main()
    {
        Console.WriteLine("Введите число строк: ");
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine("Введодите строки: ");
        List<string> strings = new List<string>();
        for (int i = 0; i < n; i++)
        {
            strings.Add(Console.ReadLine());
        }

        int p = 31;
        int mod = 1000000007;

        Dictionary<int, List<string>> hashGroups = new Dictionary<int, List<string>>();

        foreach (var str in strings)
        {
            int hash = HashString(str, p, mod);

            if (!hashGroups.ContainsKey(hash))
            {
                hashGroups[hash] = new List<string>();
            }
            hashGroups[hash].Add(str);
        }

        Console.WriteLine("Группы одинаковых строк:");
        foreach (var group in hashGroups.Values)
        {
            if (group.Count > 1)
            {
                Console.WriteLine("Группа:");
                foreach (var str in group)
                {
                    Console.WriteLine(str);
                }
            }
        }
    }
}
