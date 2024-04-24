using AutoMapper;
using FluentValidation;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using TripApp.Models;
using TripApp.Repositories;
using TripApp.ViewModels;

namespace TripApp.Services
{
    public class ClientService : IClientService
    {
        private readonly IClientRepository _clientRepository;
        private readonly IMapper _mapper;
        private readonly IValidator<Client> _validator;

        public ClientService(IClientRepository clientRepository, IMapper mapper, IValidator<Client> validator)
        {
            _clientRepository = clientRepository;
            _mapper = mapper;
            _validator = validator;
        }

        public async Task<IEnumerable<ClientListViewModel>> GetAllClientsAsync()
        {
            var clients = await _clientRepository.GetAllAsync();
            return _mapper.Map<IEnumerable<ClientListViewModel>>(clients);
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

                var validationResult = await _validator.ValidateAsync(newClient);

                if (validationResult.IsValid)
                {
                    await _clientRepository.AddAsync(newClient);
                    return newClient;
                }
                else
                {
                    throw new ValidationException(string.Join(",", validationResult.Errors.Select(e => e.ErrorMessage)));
                }
            }

            existingClient.Name = name;
            existingClient.Phone = phone;

            var updateValidationResult = await _validator.ValidateAsync(existingClient);

            if (updateValidationResult.IsValid)
            {
                await _clientRepository.UpdateAsync(existingClient);
                return existingClient;
            }
            else
            {
                throw new ValidationException(string.Join(",", updateValidationResult.Errors.Select(e => e.ErrorMessage)));
            }
        }
    }
}
