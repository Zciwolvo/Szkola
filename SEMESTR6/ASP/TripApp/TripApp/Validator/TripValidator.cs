using System.Configuration;
using TripApp.Models;
using TripApp.ViewModels;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using FluentValidation;

namespace TripApp.Validator 
{
    public class TripValidator : AbstractValidator<Trip>
    {
        public TripValidator()
        {
            RuleFor(x => x.TripDateStart).GreaterThan(DateTime.Now).WithMessage("Reservation Start Date must be greater than current date");
            RuleFor(x => x.TripDateEnd).GreaterThan((x => x.TripDateStart)).WithMessage("Reservation End Date must be greater than reservation start date");
            RuleFor(x => x.Price).NotEmpty().WithMessage("Price can't be empty");
            RuleFor(x => x.Price).GreaterThan(0).WithMessage("Price must be greater than 0");
            RuleFor(x => x.Destination).NotEmpty().WithMessage("Phone is required");
        }
    }
}
