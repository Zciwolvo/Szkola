using BikeRentalSystemWeb.Models;
using System;
using System.Linq;


namespace BikeRentalSystemWeb.Data
{
    public class DbInitializer_
    {
        public static void Initialize(BikeContext context)
        {
            context.Database.EnsureCreated();


            if (context.Bikes.Any())
            {
                return;  
            }

            var bikes = new Bike[]
            {
                new Bike { Producer = "Giant", Model = "TCR56-1", Color = "Black", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 24 },
                new Bike { Producer = "Trek", Model = "FX3", Color = "Blue", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 21 },
                new Bike { Producer = "Specialized", Model = "Sirrus X 4.0", Color = "Red", BikeType = BikeTypeModel.Kids, NumberofBikes = 1, NumberofGears = 18 },
                new Bike { Producer = "Cannondale", Model = "Synapse", Color = "White", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 22 },
                new Bike { Producer = "Giant", Model = "Reign 29", Color = "Green", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 20 },
                new Bike { Producer = "Trek", Model = "Marlin 7", Color = "Orange", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 18 },
                new Bike { Producer = "Specialized", Model = "Rockhopper", Color = "Yellow", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 24 },
                new Bike { Producer = "Cannondale", Model = "Trail 5", Color = "Purple", BikeType = BikeTypeModel.Female, NumberofBikes = 1, NumberofGears = 21 },
                new Bike { Producer = "Giant", Model = "Trance X 29", Color = "Blue", BikeType = BikeTypeModel.Male, NumberofBikes = 1, NumberofGears = 22 },
                new Bike { Producer = "Trek", Model = "Domane", Color = "Black", BikeType = BikeTypeModel.Female, NumberofBikes = 1, NumberofGears = 20 }


            };
            foreach (Bike b in bikes)
            {
                context.Bikes.Add(b);
            }
            context.SaveChanges();
        }
    }
}
