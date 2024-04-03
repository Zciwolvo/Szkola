using TripApp.Models;
using Microsoft.AspNetCore.Authentication;
using System;
using System.Linq;
using TripApp.Data;


namespace BikeRentalSystemWeb.Data
{
    public class DbInitializer
    {
        public static void Initialize(TripContext context)
        {



            if (context.Trips.Any())
            {
                return;
            }


            var trips = new Trip[]
            {
    new Trip { Destination = "Egypt", TripDateStart = DateTime.Now.AddDays(7), TripDateEnd = DateTime.Now.AddDays(14), Price = 1000.00m },
    new Trip { Destination = "Japan", TripDateStart = DateTime.Now.AddMonths(2), TripDateEnd = DateTime.Now.AddMonths(2).AddDays(10), Price = 2500.00m },
    new Trip { Destination = "France", TripDateStart = DateTime.Now.AddMonths(4), TripDateEnd = DateTime.Now.AddMonths(4).AddDays(7), Price = 1800.00m },
    new Trip { Destination = "Australia", TripDateStart = DateTime.Now.AddMonths(6), TripDateEnd = DateTime.Now.AddMonths(6).AddDays(21), Price = 3000.00m }
            };

            foreach (Trip t in trips)
            {
                context.Trips.Add(t);
            }
            context.SaveChanges();
        }
    }
}
