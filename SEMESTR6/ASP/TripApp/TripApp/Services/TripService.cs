using FluentValidation;
using System.Collections.Generic;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;
using TripApp.ViewModels;

namespace TripApp.Services
{
    public class TripService : ITripService
    {
        private readonly ITripRepository _tripRepository;
        private readonly IValidator<Trip> _validator;

        public TripService(ITripRepository tripRepository, IValidator<Trip> validator)
        {
            _tripRepository = tripRepository;
            _validator = validator;
        }

        public async Task<IEnumerable<Trip>> GetAllTripsAsync()
        {
            return await _tripRepository.GetAllAsync();
        }

        public async Task<Trip> GetTripByIdAsync(int id)
        {
            return await _tripRepository.GetByIdAsync(id);
        }

        public async Task AddTripAsync(Trip trip)
        {
            var validationResult = await _validator.ValidateAsync(trip);

            if (validationResult.IsValid)
            {
                await _tripRepository.AddAsync(trip);
            }
            else
            {
                throw new ValidationException(string.Join(",", validationResult.Errors.Select(e => e.ErrorMessage)));
            }
        }

        public async Task UpdateTripAsync(Trip trip)
        {
            var validationResult = await _validator.ValidateAsync(trip);

            if (validationResult.IsValid)
            {
                await _tripRepository.UpdateAsync(trip);
            }
            else
            {
                throw new ValidationException(string.Join(",", validationResult.Errors.Select(e => e.ErrorMessage)));
            }
        }

        public async Task DeleteTripAsync(int id)
        {
            await _tripRepository.DeleteAsync(id);
        }
    }
}
