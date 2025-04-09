using System;
using System.Linq;

class GeneticAlgorithm
{
    // Структура для хранения хромосомы (решения)
    public class Chromosome
    {
        public int a, b, c, d;

        public Chromosome(int a, int b, int c, int d)
        {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
        }

        // Фитнес-функция: чем меньше разница между суммой и 30, тем лучше
        public int Fitness()
        {
            int sum = a + 2 * b + 3 * c + 4 * d;
            return Math.Abs(30 - sum); // Чем меньше разница, тем лучше
        }

        // Ожидаемая строка для вывода
        public override string ToString()
        {
            return $"a: {a}, b: {b}, c: {c}, d: {d}";
        }
    }

    // Генерация случайной хромосомы (решения)
    static Chromosome RandomChromosome()
    {
        Random rand = new Random();
        return new Chromosome(rand.Next(1, 10), rand.Next(1, 10), rand.Next(1, 10), rand.Next(1, 10));
    }

    // Оператор селекции (выбираем два лучших решения)
    static Chromosome Selection(Chromosome[] population)
    {
        return population.OrderBy(chrom => chrom.Fitness()).First();
    }

    // Оператор кроссовера (половина информации от одного, половина от другого)
    static Chromosome Crossover(Chromosome parent1, Chromosome parent2)
    {
        Random rand = new Random();
        return new Chromosome(
            rand.Next(1, 10) > 5 ? parent1.a : parent2.a,
            rand.Next(1, 10) > 5 ? parent1.b : parent2.b,
            rand.Next(1, 10) > 5 ? parent1.c : parent2.c,
            rand.Next(1, 10) > 5 ? parent1.d : parent2.d
        );
    }

    // Оператор мутации (случайным образом изменяем одно из значений)
    static void Mutation(ref Chromosome chromosome)
    {
        Random rand = new Random();
        int mutationPoint = rand.Next(1, 5);
        switch (mutationPoint)
        {
            case 1: chromosome.a = rand.Next(1, 10); break;
            case 2: chromosome.b = rand.Next(1, 10); break;
            case 3: chromosome.c = rand.Next(1, 10); break;
            case 4: chromosome.d = rand.Next(1, 10); break;
        }
    }

    // Генерация начальной популяции
    static Chromosome[] InitializePopulation(int populationSize)
    {
        Chromosome[] population = new Chromosome[populationSize];
        for (int i = 0; i < populationSize; i++)
        {
            population[i] = RandomChromosome();
        }
        return population;
    }

    // Основной цикл генетического алгоритма
    static Chromosome RunGeneticAlgorithm(int populationSize, int generations)
    {
        Random rand = new Random();
        Chromosome[] population = InitializePopulation(populationSize);

        for (int generation = 0; generation < generations; generation++)
        {
            // Отбор
            Chromosome parent1 = Selection(population);
            Chromosome parent2 = Selection(population);

            // Кроссовер
            Chromosome offspring = Crossover(parent1, parent2);

            // Мутация
            Mutation(ref offspring);

            // Заменяем худшее решение в популяции новым потомком
            population[Array.IndexOf(population, population.OrderBy(chrom => chrom.Fitness()).Last())] = offspring;

            // Проверяем, не нашли ли мы решение
            if (parent1.Fitness() == 0)
            {
                Console.WriteLine($"Solution found in generation {generation + 1}: {parent1}");
                return parent1;
            }
        }
        return null;
    }

    public static void Main()
    {
        int populationSize = 100; // Размер популяции
        int generations = 1000; // Количество поколений

        Console.WriteLine("Running Genetic Algorithm...");
        Chromosome solution = RunGeneticAlgorithm(populationSize, generations);

        if (solution != null)
        {
            Console.WriteLine($"Found solution: {solution}");
        }
        else
        {
            Console.WriteLine("Solution not found in the given generations.");
        }
    }
}
