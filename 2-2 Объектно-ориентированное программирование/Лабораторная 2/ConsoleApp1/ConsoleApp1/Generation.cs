class Generation
{
    public int a, b, c, d;
    public int RealResult;
    private static Random r = new Random();
    private Func<int, int, int, int, int> f;

    public Generation(Func<int, int, int, int, int> func, int a, int b, int c, int d)
    {
        f = func;
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        UpdateResult();
    }

    public static Generation NewGen(Generation parent1, Generation parent2)
    {
        return new Generation(parent1.f,
            Math.Max(1, (parent1.a + parent2.a) / 2 + r.Next(-1, 2)),
            Math.Max(1, (parent1.b + parent2.b) / 2 + r.Next(-1, 2)),
            Math.Max(1, (parent1.c + parent2.c) / 2 + r.Next(-1, 2)),
            Math.Max(1, (parent1.d + parent2.d) / 2 + r.Next(-1, 2)));
    }

    public void Mutate()
    {
        int gene = r.Next(4);
        switch (gene)
        {
            case 0: a = Math.Max(1, a + r.Next(-2, 3)); break;
            case 1: b = Math.Max(1, b + r.Next(-2, 3)); break;
            case 2: c = Math.Max(1, c + r.Next(-2, 3)); break;
            case 3: d = Math.Max(1, d + r.Next(-2, 3)); break;
        }
        UpdateResult();
    }

    private void UpdateResult()
    {
        RealResult = f(a, b, c, d);
    }
}
