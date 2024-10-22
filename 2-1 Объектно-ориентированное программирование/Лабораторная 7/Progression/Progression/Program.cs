
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Введите номер элемента прогрессии:");
        int k = int.Parse(Console.ReadLine());

        // Арифметическая прогрессия (первый элемент = 2, разность = 3)
        IProgression arithmeticProgression = new ArithmeticProgression(2, 3);
        Console.WriteLine($"Aрифметическая прогрессия: {arithmeticProgression.GetElement(k)}");

        // Геометрическая прогрессия (первый элемент = 2, знаменатель = 3)
        IProgression geometricProgression = new GeometricProgression(2, 3);
        Console.WriteLine($"Геометрическая прогрессия: {geometricProgression.GetElement(k)}");
    }
}
