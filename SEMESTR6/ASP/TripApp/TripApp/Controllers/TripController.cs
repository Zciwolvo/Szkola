using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Services;

namespace TripApp.Controllers
{
    [Authorize(Roles = "Employee, Admin")]
    public class TripController : Controller
    {
        private readonly ITripService _tripService;

        public TripController(ITripService tripService)
        {
            _tripService = tripService;
        }

        // GET: Trip
        public async Task<IActionResult> Index()
        {
            var trips = await _tripService.GetAllTripsAsync();
            return View(trips);
        }

        // GET: Trip/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Trip/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Destination,TripDateStart,TripDateEnd,Price")] Trip trip)
        {
            if (ModelState.IsValid)
            {
                await _tripService.AddTripAsync(trip);
                return RedirectToAction(nameof(Index));
            }
            return View(trip);
        }

        // GET: Trip/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var trip = await _tripService.GetTripByIdAsync(id.Value);
            if (trip == null)
            {
                return NotFound();
            }
            return View(trip);
        }

        // POST: Trip/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("TripId,Destination,TripDateStart,TripDateEnd,Price")] Trip trip)
        {
            if (id != trip.TripId)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    await _tripService.UpdateTripAsync(trip);
                }
                catch (KeyNotFoundException)
                {
                    return NotFound();
                }
                return RedirectToAction(nameof(Index));
            }
            return View(trip);
        }

        // GET: Trip/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var trip = await _tripService.GetTripByIdAsync(id.Value);
            if (trip == null)
            {
                return NotFound();
            }

            return View(trip);
        }

        // POST: Trip/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            try
            {
                await _tripService.DeleteTripAsync(id);
                return RedirectToAction(nameof(Index));
            }
            catch (KeyNotFoundException)
            {
                return NotFound();
            }
        }
    }
}
