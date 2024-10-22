class Program
{
    static void Main(string[] args)
    {
        Book b1 = new Book();
        Book b2 = new Book("Толстой Л.Н.", "Война и мир", "Наука и жизнь", 1234, 2013, 101, true);
        Book b3 = new Book("Лермонтов М.Ю.", "Мцыри");
        b1.SetBook("Пушкин А.С.", "Капитанская дочка", "Вильямс", 123, 2012);
        b1.Show();
        b2.TakeItem();
        b2.Show();
        b3.Show();
        Console.WriteLine("\n Итоговая стоимость аренды: {0} p.", b1.PriceBook(3) + b2.PriceBook(3));
        
    }
}