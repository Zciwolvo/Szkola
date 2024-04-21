using FluentValidation;
using System;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;

namespace TripApp.Services
{

    public class ReservationService : IReservationService
    {
        private readonly IReservationRepository _reservationRepository;
        private readonly IValidator<Reservation> _validator;

        public ReservationService(IReservationRepository reservationRepository, IValidator<Reservation> validator)
        {
            _reservationRepository = reservationRepository;
            _validator = validator;
        }

        public async Task CreateReservationAsync(Client client, int tripId)
        {
            var reservation = new Reservation
            {
                ClientId = client.ClientId,
                ReservationDate = DateTime.Now,
                TripId = tripId
            };

            var validationResult = await _validator.ValidateAsync(reservation);

            if (validationResult.IsValid)
            {
                await _reservationRepository.AddAsync(reservation);
            }
            else
            {
                throw new ValidationException(string.Join(",", validationResult.Errors.Select(e => e.ErrorMessage)));
            }
        }


    }
}
