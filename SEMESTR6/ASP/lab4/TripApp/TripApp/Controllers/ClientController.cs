using Microsoft.AspNetCore.Mvc;
using System.Linq;
using TripApp.Data;

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
            var clients = _context.Clients.ToList();
            return View(clients);
        }
    }
}
