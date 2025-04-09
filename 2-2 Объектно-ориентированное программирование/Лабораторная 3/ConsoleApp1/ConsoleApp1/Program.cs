class Program
{
    static void Main(string[] args)
    {
        BinaryTree tree = new BinaryTree();

        tree.CreateTree1();
        tree.DirectTraversal();
        tree.ReverseTraversal(); 
        tree.EndTraversal();

        Console.WriteLine();

        List<char> expressionValues = new List<char>()
        {
            '/',        
            '*',       
            '+', '2', '.', '.', '3', '.', '.',  
            '-', '7', '.', '.', '4', '.', '.', 
            '3', '.', '.'                       
        };

        try
        {
            tree.BuildTree(expressionValues);
            int result = tree.CalculateExpression();
            string postfix = tree.GetPostfixExpression();

            Console.WriteLine("Конечный порядок");
            Console.WriteLine($"{postfix} Выражение равно {result}");
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine(ex.Message);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка: " + ex.Message);
        }
    }
}