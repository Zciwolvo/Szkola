using Microsoft.AspNetCore.Mvc;
using System;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;

namespace TripApp.Controllers
{
    public class ClientReservationController : Controller
    {
        private readonly IClientRepository _clientRepository;
        private readonly IReservationRepository _reservationRepository;

        public ClientReservationController(IClientRepository clientRepository, IReservationRepository reservationRepository)
        {
            _clientRepository = clientRepository;
            _reservationRepository = reservationRepository;
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
                // Check if the client already exists by email
                var existingClient = await _clientRepository.GetByEmailAsync(client.Email);

                if (existingClient == null)
                {
                    // If the client does not exist, add the new client
                    await _clientRepository.AddAsync(client);
                }
                else
                {
                    // If the client exists, update the client's data
                    existingClient.Name = client.Name;
                    existingClient.Phone = client.Phone;
                    await _clientRepository.UpdateAsync(existingClient);
                }

                // Get the client ID
                var clientId = existingClient?.ClientId ?? client.ClientId;

                // Create reservation
                var reservation = new Reservation
                {
                    ClientId = clientId,
                    ReservationDate = DateTime.Now,
                    TripId = tripId
                };

                await _reservationRepository.AddAsync(reservation);

                return RedirectToAction(nameof(Index), "Home");
            }
            return View(client);
        }
    }
}
