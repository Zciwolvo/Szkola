using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Services;

namespace TripApp.Controllers
{
    [Authorize]
    public class ClientReservationController : Controller
    {
        private readonly IClientService _clientService;
        private readonly IReservationService _reservationService;

        public ClientReservationController(IClientService clientService, IReservationService reservationService)
        {
            _clientService = clientService;
            _reservationService = reservationService;
        }

        // GET: ClientReservation/Create?tripId=5
        public IActionResult Create(int tripId)
        {
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
                var newClient = await _clientService.GetOrCreateAsync(client.Name, client.Email, client.Phone);
                await _reservationService.CreateReservationAsync(newClient, tripId);
                return RedirectToAction(nameof(Index), "Home");
            }
            return View(client);
        }
    }
}
