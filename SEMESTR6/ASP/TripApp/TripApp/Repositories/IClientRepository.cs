using System.Collections.Generic;
using System.Threading.Tasks;
using TripApp.Models;

namespace TripApp.Repositories
{
    public interface IClientRepository
    {
        Task<IEnumerable<Client>> GetAllAsync();
        Task<Client> GetByIdAsync(int id);
        Task<Client> GetByEmailAsync(string email);
        Task AddAsync(Client client);
        Task UpdateAsync(Client client);
        Task RemoveAsync(Client client);
    }
}
