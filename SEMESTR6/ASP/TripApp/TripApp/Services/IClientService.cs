using System.Collections.Generic;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.ViewModels;

namespace TripApp.Services
{
    public interface IClientService
    {
        Task<Client> GetOrCreateAsync(string name, string email, string phone);
        Task<IEnumerable<ClientListViewModel>> GetAllClientsAsync();
    }

}
