using Microsoft.AspNetCore.Mvc;
using System.Linq;
using TripApp.Data;

namespace TripApp.Controllers
{
    public class ReservationController : Controller
    {
        private readonly TripContext _context;

        public ReservationController(TripContext context)
        {
            _context = context;
        }

        // GET: Reservations
        public IActionResult Index()
        {
            var reservations = _context.Reservations.ToList();
            return View(reservations);
        }
    }
}
