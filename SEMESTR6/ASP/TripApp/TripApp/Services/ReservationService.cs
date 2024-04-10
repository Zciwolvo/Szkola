using System;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;

namespace TripApp.Services
{

    public class ReservationService : IReservationService
    {
        private readonly IReservationRepository _reservationRepository;

        public ReservationService(IReservationRepository reservationRepository)
        {
            _reservationRepository = reservationRepository;
        }

        public async Task CreateReservationAsync(Client client, int tripId)
        {
            var reservation = new Reservation
            {
                ClientId = client.ClientId,
                ReservationDate = DateTime.Now,
                TripId = tripId
            };
            await _reservationRepository.AddAsync(reservation);
        }
    }
}
