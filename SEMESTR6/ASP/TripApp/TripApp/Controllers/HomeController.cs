using BikeRentalSystemWeb.Data; // Assuming this namespace is correct
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Diagnostics;
using TripApp.Data;
using TripApp.ViewModels;

namespace TripApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        private readonly TripContext _context;

        public HomeController(ILogger<HomeController> logger, TripContext context)
        {
            _logger = logger;
            _context = context;
            _context.Database.EnsureCreated();
            DbInitializer.Initialize(context);
        }

        public async Task<IActionResult> Index()
        {
            var trips = await _context.Trips
                .Select(trip => new TripSummaryViewModel
                {
                    TripId = trip.TripId,
                    Destination = trip.Destination,
                    TripDateStart = trip.TripDateStart,
                    TripDateEnd = trip.TripDateEnd,
                    Price = trip.Price
                })
                .ToListAsync();

            return View(trips);
        }

    }
}