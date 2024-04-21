using System.Configuration;
using TripApp.Models;
using TripApp.ViewModels;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using FluentValidation;

namespace TripApp.Validator
{
    public class ReservationValidator : AbstractValidator<Reservation>
    {
        public ReservationValidator() 
        {
            RuleFor(x => x.ClientId).NotEmpty().WithMessage("Client ID cannot be empty");
            RuleFor(x => x.ReservationDate).GreaterThan(DateTime.Now).WithMessage("Reservation Start Date must be greater than current date");
            RuleFor(x => x.TripId).NotEmpty().WithMessage("Trip ID cannot be empty");
        }
    }
}
