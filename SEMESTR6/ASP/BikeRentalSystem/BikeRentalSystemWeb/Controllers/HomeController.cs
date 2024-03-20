using BikeRentalSystemWeb.Data;
using BikeRentalSystemWeb.Models;
using BikeRentalSystemWeb.ViewModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;

namespace BikeRentalSystemWeb.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly BikeContext _context;

        public HomeController(ILogger<HomeController> logger, BikeContext context)
        {
            _logger = logger;
            _context = context;
            _context.Database.EnsureCreated();
            DbInitializer_.Initialize(context);
        }

        public async Task<IActionResult> Index()
        {
            var bikes = await _context.Bikes.ToListAsync();
            return View(bikes);
        }

        public async Task<IActionResult> Detail(int id)
        {
            var bike = await _context.Bikes.FirstOrDefaultAsync(x => x.BikeID == id);
            if (bike == null)
            {
                return NotFound();
            }
            return View(bike);
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
