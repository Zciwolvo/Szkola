using System.Collections.Generic;
using System.Threading.Tasks;
using TripApp.Models;

namespace TripApp.Services
{
    public interface IReservationService
    {
        Task CreateReservationAsync(Client client, int tripId);
    }
}
