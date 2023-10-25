using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleClient_NETFramework
{
    internal class Program
    {
        static void Main(string[] args)
        {
            TestWebService.FirstWebService firstWebService = new TestWebService.FirstWebService();

            firstWebService.Add(new TestWebService.Person() { FirstName = "Zenon", LastName = "Płaski" });
            firstWebService.Add(new TestWebService.Person() { FirstName = "Zenon", LastName = "Wklęsły" });

            var persons= firstWebService.GetAllPersons();

            foreach (var person in persons)
            {
                Console.WriteLine($"{person.Id} {person.FirstName} {person.LastName}");
            }

            Console.ReadLine();
        }
    }
}
