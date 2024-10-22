class Magazine : Item, IPubs
{
    private String volume = "";
    private int number; 
    private String title = "";
    private int year;
    public Magazine(String volume, int number, String title, int year, long invNumber, bool taken) : base(invNumber, taken)
    {
        this.volume = volume;
        this.number = number;
        this.title = title;
        this.year = year;
    }
    public Magazine()
    { }
    public override void Show()
    {
        Console.WriteLine("\nЖурнал:\n Том: {0}\n Номер: {1}\n Название: {2} \n Год выпуска: {3}", volume, number, title, year);
        base.Show();
    }
    public override void Return()
    {
        taken = true;
    }
    public bool IfSubs { get; set; }
    public void Subs()
    {
        Console.WriteLine("Подписка на журнал \"{0}\": {1}.", title, IfSubs);
    }
}