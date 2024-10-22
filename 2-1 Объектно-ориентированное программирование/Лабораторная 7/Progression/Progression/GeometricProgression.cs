class GeometricProgression : IProgression
{
    private double firstTerm;
    private double ratio;

    public GeometricProgression(double firstTerm, double ratio)
    {
        this.firstTerm = firstTerm;
        this.ratio = ratio;
    }

    public double GetElement(int k)
    {
        return firstTerm * Math.Pow(ratio, k - 1);
    }
}
  