using TripApp.Models;
using Microsoft.AspNetCore.Authentication;
using System;
using System.Linq;
using TripApp.Data;
using Microsoft.AspNetCore.Identity;


namespace BikeRentalSystemWeb.Data
{
    public class DbInitializer
    {

        public static void AddRoles(TripContext context)
        {
            if (context.Roles.Any())
            {
                return;
            }

            var Roles = new IdentityRole[]
            {
                new IdentityRole { Name = "Admin", NormalizedName = "ADMIN", Id = "1" },
                new IdentityRole { Name = "Employee", NormalizedName = "EMPLOYEE", Id = "2"},
                new IdentityRole { Name = "Client", NormalizedName = "CLIENT", Id = "3"}
            };

            foreach (IdentityRole r in Roles)
            {
                context.Roles.Add(r);
            }

        }
        public static void AddInitialDestinations(TripContext context)
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


        }
        public static void Initialize(TripContext context)
        {

            AddInitialDestinations(context);
            AddRoles(context);
            context.SaveChanges();

        }
    }
}
