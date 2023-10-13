class Program
{
    public static void Main(string[] args)
    {
        static int RotateLeft(int value, int count)
        {
            Console.WriteLine(Convert.ToString(value, toBase: 2));
            return (value << count) | (value >> (32 - count));
        }
        int value = Convert.ToInt32(Console.ReadLine());
        int shift = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(Convert.ToString(RotateLeft(value, shift), toBase: 2));
    }
}
