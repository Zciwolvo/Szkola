using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Linq;
using TripApp.Data;
using TripApp.Services;
using TripApp.ViewModels;

namespace TripApp.Controllers
{
    [Authorize(Roles = "Employee,Admin")]
    public class ClientController : Controller
    {
        private readonly IClientService _clientService;

        public ClientController(IClientService clientService)
        {
            _clientService = clientService;
        }

        // GET: Clients
        public async Task<IActionResult> Index()
        {
            var clientListViewModel = await _clientService.GetAllClientsAsync();

            return View(clientListViewModel);
        }
    }
}
