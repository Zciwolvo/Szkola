using BikeRentalSystemWeb.Data; // Assuming this namespace is correct (might not be used anymore)
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore; // Might not be needed anymore
using System.Diagnostics;
using TripApp.Data; // Might not be needed anymore
using TripApp.Models;
using TripApp.Repositories;
using TripApp.Services;
using TripApp.ViewModels;

namespace TripApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly ITripService _tripService;

        public HomeController(ILogger<HomeController> logger, ITripService tripService)
        {
            _logger = logger;
            _tripService = tripService;
        }

        public async Task<IActionResult> Index()
        {
            // Get trips using the TripService
            var trips = await _tripService.GetAllTripsAsync();

            // Convert to TripSummaryViewModel if needed
            var tripSummaries = trips.Select(trip => new TripSummaryViewModel
            {
                TripId = trip.TripId,
                Destination = trip.Destination,
                TripDateStart = trip.TripDateStart,
                TripDateEnd = trip.TripDateEnd,
                Price = trip.Price
            }).ToList();

            return View(tripSummaries);
        }
    }
}
