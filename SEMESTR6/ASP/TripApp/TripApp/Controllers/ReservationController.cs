using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using TripApp.Data;
using TripApp.ViewModels;

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
        public async Task<IActionResult> Index()
        {
            var reservations = await _context.Reservations
                .Select(reservation => new ReservationViewModel
                {
                    ReservationId = reservation.ReservationId,
                    ReservationDate = reservation.ReservationDate,
                    ClientId = reservation.ClientId,
                    TripId = reservation.TripId
                })
                .ToListAsync();

            return View(reservations);
        }
    }
}