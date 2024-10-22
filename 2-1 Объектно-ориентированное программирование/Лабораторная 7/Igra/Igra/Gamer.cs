class Gamer
{
    string Name;
    IgralnayaKost seans;
    public Gamer(string name)
    {
        Name = name;
        seans = new IgralnayaKost();
    }
    public int SeansGame()
    {
        return seans.random();
    }
    public override string ToString()
    {
        return Name;
    }
}