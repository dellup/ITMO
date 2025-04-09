using System;
using System.Collections.Generic;

public class TreeNode
{
    public char Value { get; set; }
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }

    public TreeNode(char value)
    {
        Value = value;
        Left = null;
        Right = null;
    }
}



