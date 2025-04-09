public class BinaryTree
{
    private TreeNode root;

    public BinaryTree()
    {
        root = null;
    }

    public void CreateTree1()
    {
        root = new TreeNode('a');
        root.Left = new TreeNode('b');
        root.Left.Left = new TreeNode('d');
        root.Left.Right = new TreeNode('e');
        root.Right = new TreeNode('c');
        root.Right.Right = new TreeNode('f');
    }

    public void DirectTraversal()
    {
        Console.Write("Обход дерева в прямом порядке: ");
        DirectTraversalHelper(root);
        Console.WriteLine();
    }

    private void DirectTraversalHelper(TreeNode node)
    {
        if (node == null) return;
        Console.Write(node.Value + " ");
        DirectTraversalHelper(node.Left);
        DirectTraversalHelper(node.Right);
    }

    public void ReverseTraversal()
    {
        Console.Write("Обход дерева в обратном порядке: ");
        ReverseTraversalHelper(root);
        Console.WriteLine();
    }

    private void ReverseTraversalHelper(TreeNode node)
    {
        if (node == null) return;
        ReverseTraversalHelper(node.Left);
        Console.Write(node.Value + " ");
        ReverseTraversalHelper(node.Right);
    }

    public void EndTraversal()
    {
        Console.Write("Обход дерева в концевом порядке: ");
        EndHelper(root);
        Console.WriteLine();
    }

    private void EndHelper(TreeNode node)
    {
        if (node == null) return;
        EndHelper(node.Left);
        EndHelper(node.Right);
        Console.Write(node.Value + " ");
    }

    public void BuildTree(List<char> values)
    {
        int index = 0;
        root = BuildTreeHelper(values, ref index);

        if (index < values.Count && values[index] != '.')
        {
            throw new ArgumentException("Ошибка: лишние символы в выражении.");
        }

        if (root == null)
        {
            throw new ArgumentException("Ошибка: дерево не было построено корректно.");
        }
    }

    private TreeNode BuildTreeHelper(List<char> values, ref int index)
    {
        if (index >= values.Count || values[index] == '.')
        {
            index++;
            return null;
        }

        TreeNode node = new TreeNode(values[index]);
        index++;

        node.Left = BuildTreeHelper(values, ref index);
        node.Right = BuildTreeHelper(values, ref index);

        return node;
    }

    public int CalculateExpression()
    {
        if (root == null)
        {
            throw new ArgumentException("Ошибка: дерево не построено.");
        }
        return CalculateExpressionHelper(root);
    }

    private int CalculateExpressionHelper(TreeNode node)
    {
        if (node == null)
        {
            throw new ArgumentException("Некорректное дерево выражений.");
        }

        if (char.IsDigit(node.Value))
        {
            return int.Parse(node.Value.ToString());
        }

        int leftValue = CalculateExpressionHelper(node.Left);
        int rightValue = CalculateExpressionHelper(node.Right);


        switch (node.Value)
        {
            case '+': return leftValue + rightValue;
            case '-': return leftValue - rightValue;
            case '*': return leftValue * rightValue;
            case '/': return leftValue / rightValue;
            default: throw new ArgumentException($"Неизвестный оператор: {node.Value}");
        }
    }

    public string GetPostfixExpression()
    {
        if (root == null)
        {
            throw new ArgumentException("Ошибка: дерево не построено.");
        }
        return GetPostfixExpressionHelper(root).Trim();
    }

    private string GetPostfixExpressionHelper(TreeNode node)
    {
        if (node == null)
        {
            return "";
        }

        if (char.IsDigit(node.Value))
        {
            return node.Value.ToString() + " ";
        }

        string left = GetPostfixExpressionHelper(node.Left);
        string right = GetPostfixExpressionHelper(node.Right);
        return left + right + node.Value + " ";
    }
}