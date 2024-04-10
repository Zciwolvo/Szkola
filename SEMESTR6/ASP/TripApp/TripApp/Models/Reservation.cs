namespace TripApp.Models
{
    public class Reservation
    {
        public int ReservationId { get; set; }
        public int ClientId { get; set; }
        public Client Client { get; set; }
        public DateTime ReservationDate { get; set; }
        public int TripId { get; set; }
        public Trip Trip { get; set; }
    }
}
