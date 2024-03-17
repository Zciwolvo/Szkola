using BikeRentalSystemWeb.Models;
using BikeRentalSystemWeb.ViewModels;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace BikeRentalSystemWeb.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private IEnumerable<BikeDetailViewModel> _bikes = new List<BikeDetailViewModel>
        {
            new BikeDetailViewModel
            {
                Id = 1,
                Producer = "Giant",
                Model = "TCR56-1",
                Color = "Black",
                BikeType = BikeTypeModel.Male,
                NumberofBikes = 1,
                NumberofGears = 24
            },

            new BikeDetailViewModel
            {
                Id = 2,
                Producer = "Trek",
                Model = "Emonda ALR 5",
                Color = "Red",
                BikeType = BikeTypeModel.Male,
                NumberofBikes = 1,
                NumberofGears = 22
            },

            new BikeDetailViewModel
            {
                Id = 3,
                Producer = "Specialized",
                Model = "Sirrus X 3.0",
                Color = "Blue",
                BikeType = BikeTypeModel.Female,
                NumberofBikes = 1,
                NumberofGears = 27
            },

            new BikeDetailViewModel
            {
                Id = 4,
                Producer = "Cannondale",
                Model = "Trail 8",
                Color = "Green",
                BikeType = BikeTypeModel.Male,
                NumberofBikes = 1,
                NumberofGears = 21
            },

            new BikeDetailViewModel
            {
                Id = 5,
                Producer = "Scott",
                Model = "Sub Cross 30 Men",
                Color = "Grey",
                BikeType = BikeTypeModel.Male,
                NumberofBikes = 1,
                NumberofGears = 27
            },
            new BikeDetailViewModel
            {
                Id = 6,
                Producer = "Cervélo",
                Model = "R-Series R5 Disc",
                Color = "Black/Red",
                BikeType = BikeTypeModel.Male,
                NumberofBikes = 1,
                NumberofGears = 22
            },

        };


        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View(_bikes);
        }

        public IActionResult Detail(int id)
        {
            var bike = _bikes.FirstOrDefault(x => x.Id == id);
            return View(bike);

        }


        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}