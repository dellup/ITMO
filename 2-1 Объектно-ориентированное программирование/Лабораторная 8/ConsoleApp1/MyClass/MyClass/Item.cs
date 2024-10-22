abstract class Item : IComparable

{
    int IComparable.CompareTo(object obj)
    {
        Item it = (Item)obj;
        if (this.invNumber == it.invNumber) return 0;
        else if (this.invNumber > it.invNumber) return 1;
        else return -1;
    }
    public Item(long invNumber, bool taken)
    {
        this.invNumber = invNumber;
        this.taken = taken;
    }
    public Item()
    {
        this.taken = true;
    }
    protected long invNumber;
    // хранит состояние объекта - взят ли на руки 
    protected bool taken;
    // истина, если этот предмет имеется в библиотеке 
    public bool IsAvailable()
    {
        if (taken == true)
            return true;
        else
            return false;
    }
    // инвентарный номер 
    public long GetInvNumber()
    {
        return invNumber;
    }
    // операция "взять"
    public void Take()
    {
        taken = false;
    }
    // операция "вернуть"
    abstract public void Return();
    public virtual void Show()
    {
        Console.WriteLine("Состояние единицы хранения:\n Инвентарный номер: {0}\n Наличие: {1}", invNumber, taken);
    }
    public void TakeItem()
    {
        if (this.IsAvailable())
            this.Take();
    }
}