class RabinKarp
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        string t = Console.ReadLine();

        int p = 31;
        int n = s.Length;
        int m = t.Length;

        int[] p_pow = new int[m];
        p_pow[0] = 1;
        for (int i = 1; i < m; i++)
        {
            p_pow[i] = p_pow[i - 1] * p;
        }

        int[] hashes = new int[m];
        for (int i = 0; i < m; i++)
        {
            hashes[i] = (s[i] - 'a' + 1) * p_pow[i];
            if (i != 0)
            {
                hashes[i] += hashes[i - 1];
            }
        }

        int s_hash = 0;
        for (int i = 0; i < n; i++)
        {
            s_hash += (s[i] - 'a' + 1) * p_pow[i];
        }

        int cur_h;
        for (int i = 0; (i + n - 1) < m; i++)
        {
            cur_h = hashes[i + n - 1];
            if (i != 0)
            {
                cur_h -= hashes[i - 1];
            }
            if (cur_h == s_hash * p_pow[i])
            {
                Console.WriteLine(i);
            }
        }

    }
}