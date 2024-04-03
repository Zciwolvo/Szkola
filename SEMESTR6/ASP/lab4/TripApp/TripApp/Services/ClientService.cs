using System;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;

namespace TripApp.Services
{
    public class ClientService : IClientService
    {
        private readonly IClientRepository _clientRepository;

        public ClientService(IClientRepository clientRepository)
        {
            _clientRepository = clientRepository;
        }

        public async Task<Client> GetOrCreateAsync(string name, string email, string phone)
        {
            var existingClient = await _clientRepository.GetByEmailAsync(email);

            if (existingClient == null)
            {
                var newClient = new Client
                {
                    Name = name,
                    Email = email,
                    Phone = phone
                };
                await _clientRepository.AddAsync(newClient);
                return newClient;
            }

            existingClient.Name = name;
            existingClient.Phone = phone;
            await _clientRepository.UpdateAsync(existingClient);

            return existingClient;
        }
    }

}
