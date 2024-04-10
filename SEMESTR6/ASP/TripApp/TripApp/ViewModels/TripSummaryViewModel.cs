namespace TripApp.ViewModels
{
    public class TripSummaryViewModel
    {
        public int TripId { get; set; }
        public string Destination { get; set; }
        public DateTime TripDateStart { get; set; }
        public DateTime TripDateEnd { get; set; }
        public decimal Price { get; set; }
    }
}
