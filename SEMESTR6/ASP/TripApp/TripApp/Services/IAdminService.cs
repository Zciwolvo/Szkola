using Microsoft.AspNetCore.Identity;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

public interface IAdminService
{
    Task<List<IdentityUser>> GetAllUsersAsync();
    Task<List<string>> GetAllRolesAsync();
    Task UpdateUserRoleAsync(string userId, string newRole);
}
