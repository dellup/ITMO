using System;

class Target
{
    static void Main(string[] args)
    {
        Random random = new Random();
        int centerX = random.Next(-10, 11);
        int centerY = random.Next(-10, 11);
        int score = 0;
        bool isEven = random.Next(0, 2) == 0;

        while (true)
        {
            Console.Write("Введите координаты x и y (или 'exit' для выхода): ");
            string input = Console.ReadLine();
            if (input.Equals("exit", StringComparison.OrdinalIgnoreCase)) break;

            string[] parts = input.Split(' ');
            if (parts.Length != 2 || !int.TryParse(parts[0], out int x) || !int.TryParse(parts[1], out int y))
            {
                Console.WriteLine("Некорректный ввод. Попробуйте снова.");
                continue;
            }

            // Добавляем случайное смещение от -1 до 1
            x += random.Next(-1, 2);
            y += random.Next(-1, 2);

            double distance = Math.Sqrt(Math.Pow(x - centerX, 2) + Math.Pow(y - centerY, 2));
            if (isEven)
            {
                if (distance <= 3) score += 10;
                else if (distance <= 6) score += 5;
            }
            else
            {
                if (distance <= 3) score += 10;
                else if (distance <= 6) score += 5;
                else if (distance <= 10) score += 1;
            }

            Console.WriteLine($"Текущий счет: {score}");
        }

        Console.WriteLine($"Игра окончена. Общий счет: {score}");
    }
}
