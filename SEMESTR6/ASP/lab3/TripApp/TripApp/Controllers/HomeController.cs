using BikeRentalSystemWeb.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Diagnostics;
using TripApp.Data;
using TripApp.Models;

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
            var trips = await _context.Trips.ToListAsync();
            return View(trips);
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}