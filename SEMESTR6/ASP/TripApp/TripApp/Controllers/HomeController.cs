using AutoMapper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Services;
using TripApp.ViewModels;

namespace TripApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly ITripService _tripService;
        private readonly IMapper _mapper;

        public HomeController(ILogger<HomeController> logger, ITripService tripService, IMapper mapper)
        {
            _logger = logger;
            _tripService = tripService;
            _mapper = mapper;
        }

        public async Task<IActionResult> Index()
        {
            var trips = await _tripService.GetAllTripsAsync();

            var tripSummaries = _mapper.Map<List<TripSummaryViewModel>>(trips);

            return View(tripSummaries);
        }
    }
}
