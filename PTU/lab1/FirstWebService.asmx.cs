using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace _2023_24_IDI_sem_5_PTUSWPH_lab_gr_2b
{
    /// <summary>
    /// Summary description for FirstWebService
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class FirstWebService : System.Web.Services.WebService
    {

        [WebMethod]
        public string HelloWorld()
        {
            return "Hello World";
        }

        [WebMethod]
        public double AddDoubles(double a, double b)
        {
            return a + b;
        }

        [WebMethod]
        public double Multiply(double a, double b)
        {
            return a * b;
        }
        ////////////////////////////

        static List<Person> people = new List<Person>()
        {
            new Person(){ Id=1, FirstName = "Jan", LastName="Kowalski"},
            new Person(){ Id=2, FirstName = "Andrzej", LastName="Nowak"},
            new Person(){ Id=3, FirstName = "Józef", LastName="Tkaczuk"},
        };

        [WebMethod]
        public List<Person> GetAllPersons()
        {
            return people;
        }
        [WebMethod]
        public Person GetSinglePerson(int id)
        {
            return people.SingleOrDefault(r => r.Id == id);
        }
        [WebMethod]
        public void Add(Person person)
        {
            person.Id = people.Max(r => r.Id) + 1;
            people.Add(person);
        }

        [WebMethod]
        public void Update(Person person)
        {

            var toUpdate = GetSinglePerson(person.Id);
            toUpdate.FirstName = person.FirstName;
            toUpdate.LastName = person.LastName;

        }

        [WebMethod]
        public void Delete(int id)
        {
            var toDelete = GetSinglePerson(id);
            people.Remove(toDelete);
        }

    }
    public class Person
    {
        public int Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
    }

}
