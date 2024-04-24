using AutoMapper;
using TripApp.Models;
using TripApp.ViewModels;

namespace TripApp.AutoMapper
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Trip, TripSummaryViewModel>();
            CreateMap<Client, ClientListViewModel>();
        }
    }
}
