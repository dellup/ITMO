using System;

namespace Utils
{
    class Utils
    {
        public static int Greater(int a, int b)
        {
            return a > b ? a : b;
        }
        public static void Swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }
        public static bool Factorial(int n, out int answer)
        {
            int k; // Loop counter 
            int f = 1; // Working value 
            bool ok = true; // True if okay, false if not
            try
            {
                checked // для проверки на арифм переполнение
                {
                    for (k = 2; k <= n; ++k)
                    {
                        f = f * k;
                    }
                }
            }
            catch (Exception)
            {
                f = 0;
                ok = false;
            }
            answer = f;
            return ok;

        }
    }
}
