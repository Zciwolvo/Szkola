using Microsoft.AspNetCore.Mvc;
using System.Linq;
using TripApp.Data;
using TripApp.ViewModels;

namespace TripApp.Controllers
{
    public class ClientController : Controller
    {
        private readonly TripContext _context;

        public ClientController(TripContext context)
        {
            _context = context;
        }

        // GET: Clients
        public IActionResult Index()
        {
            var clientListViewModel = _context.Clients.Select(client => new ClientListViewModel
            {
                ClientId = client.ClientId,
                Name = client.Name,
                Email = client.Email,
                Phone = client.Phone
            });

            return View(clientListViewModel);
        }
    }
}
