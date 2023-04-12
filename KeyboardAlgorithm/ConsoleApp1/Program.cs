using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace msi2
{
    internal class GeneticKeyboardFrequency
    {
        static Random random = new Random();
        static char[] chars = "abcdefghijklmnopqrstuvwxyz".ToCharArray();
        static int size = 100, charactersLength = chars.Length;
        static Dictionary<char, double> letterFrequency = CreateDict();
        static double[][] KeyDistances;


        static void Main(string[] args)
        {
            KeyDistances = CalculateKeyDistances();

            int[][] population = GeneratePopulation();

            double[] fitness = GetFitness(population);
            int[][] newPopulation = new int[size][];

            for (int i = 0; i < size; i++)
            {
                int[] parent1 = SelectParent(population, fitness);
                int[] parent2 = SelectParent(population, fitness);

                int[] child = Crossover(parent1, parent2);

                newPopulation[i] = child;
            }

            int bestIndex = Array.IndexOf(fitness, fitness.Min());
            int[] bestSet = population[bestIndex];
            Console.WriteLine("Best randomized keyboard layout" + ": "
                            + string.Join("", bestSet.Select(x => chars[x])) + "\nfitness: " + fitness[bestIndex]);

            population = newPopulation;
        }

        static double[][] CalculateKeyDistances()
        {
            string[] QWERTY = new string[]
            {
        "1234567890-=",
        "qwertyuiop[]",
        "asdfghjkl;'",
        "zxcvbnm,./"
            };

            int[] keyCoordsX = new int[charactersLength];
            int[] keyCoordsY = new int[charactersLength];

            for (int i = 0; i < QWERTY.Length; i++)
            {
                for (int j = 0; j < QWERTY[i].Length; j++)
                {
                    int index = QWERTY[i][j] - 'a';

                    if (index >= 0 && index < charactersLength)
                    {
                        keyCoordsX[index] = j;
                        keyCoordsY[index] = i;
                    }
                }
            }

            double[][] distances = new double[charactersLength][];

            for (int i = 0; i < charactersLength; i++)
            {
                distances[i] = new double[charactersLength];

                for (int j = 0; j < charactersLength; j++)
                {
                    distances[i][j] = Math.Sqrt(Math.Pow(keyCoordsX[i] - keyCoordsX[j], 2) + Math.Pow(keyCoordsY[i] - keyCoordsY[j], 2));
                }
            }

            return distances;
        }

        static int[][] GeneratePopulation()
        {
            int[][] population = new int[size][];

            for (int i = 0; i < size; i++)
            {
                population[i] = Enumerable.Range(0, charactersLength).OrderBy(x => random.Next()).ToArray();
            }

            return population;
        }

        static double[] GetFitness(int[][] population)
        {
            double[] fitness = new double[size];

            for (int s = 0; s < size; s++)
            {
                double totalEffort = 0;
                int[] pop = population[s];
                for (int i = 0; i < charactersLength; i++)
                {
                    
                    for (int j = 0; j < charactersLength; j++)
                    {
                        totalEffort += letterFrequency[chars[i]] * letterFrequency[chars[j]] * KeyDistances[pop[i]][pop[j]];
                    }
                }
                fitness[s] = Math.Round(totalEffort/10000, 2);
            }

            return fitness;
        }

        static int[] SelectParent(int[][] population, double[] fitness)
        {
            int[] contestant1 = population[random.Next(size)];
            int[] contestant2 = population[random.Next(size)];

            if (fitness[Array.IndexOf(population, contestant1)] <= fitness[Array.IndexOf(population, contestant2)])
            {
                return contestant1;
            }
            else
            {
                return contestant2;
            }
        }

        static int[] Crossover(int[] parent1, int[] parent2)
        {
            int point1 = random.Next(1, charactersLength - 2);
            int point2 = random.Next(point1, charactersLength - 1);

            int[] child = new int[charactersLength];

            for (int i = point1; i < point2; i++)
            {
                child[i] = parent1[i];
            }

            int index = 0;
            for (int i = 0; i < charactersLength; i++)
            {
                if (!child.Contains(parent2[i]))
                {
                    if (index == point1)
                    {
                        index = point2;
                    }

                    child[index++] = parent2[i];
                }
            }

            return child;
        }


        public static Dictionary<char, double> CreateDict()
        {
            var letterFrequency = new Dictionary<char, double>();
            letterFrequency.Add('a', 8.2);
            letterFrequency.Add('b', 1.5);
            letterFrequency.Add('c', 2.8);
            letterFrequency.Add('d', 4.3);
            letterFrequency.Add('e', 13);
            letterFrequency.Add('f', 2.2);
            letterFrequency.Add('g', 2);
            letterFrequency.Add('h', 6.1);
            letterFrequency.Add('i', 7);
            letterFrequency.Add('j', 0.15);
            letterFrequency.Add('k', 0.77);
            letterFrequency.Add('l', 4);
            letterFrequency.Add('m', 2.4);
            letterFrequency.Add('n', 6.7);
            letterFrequency.Add('o', 7.5);
            letterFrequency.Add('p', 1.9);
            letterFrequency.Add('q', 0.095);
            letterFrequency.Add('r', 6);
            letterFrequency.Add('s', 6.3);
            letterFrequency.Add('t', 9.1);
            letterFrequency.Add('u', 2.8);
            letterFrequency.Add('v', 0.98);
            letterFrequency.Add('w', 2.4);
            letterFrequency.Add('x', 0.15);
            letterFrequency.Add('y', 2);
            letterFrequency.Add('z', 0.074);
            return letterFrequency;
        }
    }
}
