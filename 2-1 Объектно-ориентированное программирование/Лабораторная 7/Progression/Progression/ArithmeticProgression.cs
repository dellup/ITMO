class ArithmeticProgression : IProgression
{
    private double firstTerm;
    private double difference;

    public ArithmeticProgression(double firstTerm, double difference)
    {
        this.firstTerm = firstTerm;
        this.difference = difference;
    }

    public double GetElement(int k)
    {
        return firstTerm + difference*(k-1);
    }
}