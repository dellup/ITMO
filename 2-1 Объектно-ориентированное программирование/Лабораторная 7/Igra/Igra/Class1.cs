class IgralnayaKost
{
    Random r;
    public IgralnayaKost()
    {
        r = new Random();
    }
    public int random()
    {
        int res = r.Next(6) + 1;
        return res;
    }
}