using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.Linq;
using System.Threading.Tasks;
using TripApp.Data;
using TripApp.Models;

namespace TripApp.Controllers
{
    public class ClientReservationController : Controller
    {
        private readonly TripContext _context;

        public ClientReservationController(TripContext context)
        {
            _context = context;
        }

        // GET: ClientReservation/Create?tripId=5
        public IActionResult Create(int tripId)
        {
            // Pass tripId to the view
            ViewBag.TripId = tripId;
            return View();
        }

        // POST: ClientReservation/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Name,Email,Phone")] Client client, int tripId)
        {
            if (ModelState.IsValid)
            {
                // Check if the client already exists
                var existingClient = await _context.Clients.FirstOrDefaultAsync(c => c.Name == client.Name && c.Email == client.Email);

                if (existingClient == null)
                {
                    _context.Add(client);
                    await _context.SaveChangesAsync();
                }
                else
                {
                    // Assign existing client ID
                    client.ClientId = existingClient.ClientId;
                }

                // Create reservation
                var reservation = new Reservation
                {
                    ClientId = client.ClientId,
                    ReservationDate = DateTime.Now,
                    TripId = tripId
                };

                _context.Add(reservation);
                await _context.SaveChangesAsync();

                return RedirectToAction(nameof(Index), "Home");
            }
            return View(client);
        }
    }
}
