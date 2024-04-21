using FluentValidation;
using System;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;

namespace TripApp.Services
{
    public class ClientService : IClientService
    {
        private readonly IClientRepository _clientRepository;
        private readonly IValidator<Client> _validator;

        public ClientService(IClientRepository clientRepository, IValidator<Client> validator) // Inject validator
        {
            _clientRepository = clientRepository;
            _validator = validator;
        }

        public async Task<IEnumerable<Client>> GetAllClientsAsync()
        {
            return await _clientRepository.GetAllAsync();
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

                // Validate the Client model before adding it (assuming Option 1)
                var validationResult = await _validator.ValidateAsync(newClient);

                if (validationResult.IsValid)
                {
                    await _clientRepository.AddAsync(newClient);
                    return newClient;
                }
                else
                {
                    // Handle validation errors (throw exception, log errors etc.)
                    throw new ValidationException(string.Join(",", validationResult.Errors.Select(e => e.ErrorMessage)));
                }
            }

            existingClient.Name = name;
            existingClient.Phone = phone;

            // Validate the Client model before updating it (assuming Option 1)
            var updateValidationResult = await _validator.ValidateAsync(existingClient);

            if (updateValidationResult.IsValid)
            {
                await _clientRepository.UpdateAsync(existingClient);
                return existingClient;
            }
            else
            {
                // Handle validation errors (throw exception, log errors etc.)
                throw new ValidationException(string.Join(",", updateValidationResult.Errors.Select(e => e.ErrorMessage)));
            }
        }
    }

}
