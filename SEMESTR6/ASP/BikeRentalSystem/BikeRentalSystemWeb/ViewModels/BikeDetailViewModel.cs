namespace BikeRentalSystemWeb.ViewModels
{   
    public enum BikeTypeModel { Male, Female, Kids }
    public class BikeDetailViewModel
    {
        public int Id { get; set; }
        public string Producer { get; set; }
        public string Model { get; set; }
        public int NumberofGears { get; set; }
        public BikeTypeModel BikeType { get; set; }
        public string Color { get; set; }
        public int NumberofBikes { get; set; }

    }
}
