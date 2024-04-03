using System.Collections.Generic;
using System.Threading.Tasks;
using TripApp.Models;

namespace TripApp.Repositories
{
    public interface ITripRepository
    {
        Task<IEnumerable<Trip>> GetAllAsync();
        Task<Trip> GetByIdAsync(int id);
        Task AddAsync(Trip trip);
        Task UpdateAsync(Trip trip);
        Task DeleteAsync(int id);
        bool Exists(int id);
    }
}
