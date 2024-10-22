class Book : Item
{
    private String author;  
    private String title;  
    private String publisher; 
    private int pages;   
    private int year;   
    private static double price = 9;
    private bool returnStr;
    public Book(String author, String title, String publisher, int pages, int year)
    {
        this.author = author;
        this.title = title;
        this.publisher = publisher;
        this.pages = pages;
        this.year = year;
    }
    public Book() { }
    public Book(String author, String title)
    {
        this.author = author;
        this.title = title;
    }
    public Book(String author, String title, String publisher, int pages, int year, long invNumber, bool taken) : base(invNumber, taken)
    {
        this.author = author;
        this.title = title;
        this.publisher = publisher;
        this.pages = pages;
        this.year = year;
    }
    static Book() 
    {
        price = 10;
    }
    public override void Return()
    {
        returnStr = true;
    }
    public void SetBook(String author, String title, String publisher, int pages, int year)
    {
        this.author = author;
        this.title = title;
        this.publisher = publisher;
        this.pages = pages;
        this.year = year;
    }
    public static void SetPrice(double price)
    {
        Book.price = price;
    }
    public override void Show()
    {
        Console.WriteLine("\nКнига:\n Автор: {0}\n Hазвание: {1}\n Год издания: {2}\n {3} стр.\n Стоимость аренды: {4}", author, title, year, pages, Book.price);
        base.Show();

    }
    public double PriceBook(int s)
    {
        double cust = s * price;
        return cust;
    }
}
    