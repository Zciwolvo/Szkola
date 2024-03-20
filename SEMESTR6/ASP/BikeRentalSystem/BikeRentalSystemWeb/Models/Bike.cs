namespace BikeRentalSystemWeb.Models
{
    public enum BikeTypeModel { Male, Female, Kids }
    public class Bike
    {

        public int BikeID { get; set; }
        public string Producer { get; set; }
        public string Model { get; set; }
        public int NumberofGears { get; set; }
        public BikeTypeModel BikeType { get; set; }
        public string Color { get; set; }
        public int NumberofBikes { get; set; }
    }
}
