using BikeRentalSystemWeb.Data;
using FluentValidation;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore; // Ensure this is the correct namespace
using TripApp.Data;
using TripApp.Models;
using TripApp.Repositories;
using TripApp.Services;
using TripApp.Validator;
using TripApp.ViewModels;
using AutoMapper;
using Microsoft.Extensions.DependencyInjection;
using TripApp.AutoMapper;
using Microsoft.AspNetCore.Identity;

namespace TripApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            builder.Services.AddDbContext<TripContext>(options =>
                options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultContext")));

            builder.Services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = true)
                .AddRoles<IdentityRole>()
                .AddEntityFrameworkStores<TripContext>();

            builder.Services.AddScoped<IReservationRepository, ReservationRepository>();
            builder.Services.AddScoped<IClientRepository, ClientRepository>();
            builder.Services.AddScoped<ITripRepository, TripRepository>();

            builder.Services.AddScoped<IReservationService, ReservationService>();
            builder.Services.AddScoped<IClientService, ClientService>();
            builder.Services.AddScoped<ITripService, TripService>();
            builder.Services.AddScoped<IAdminService, AdminService>();

            builder.Services.AddScoped<IValidator<Client>, ClientValidator>();
            builder.Services.AddScoped<IValidator<Trip>, TripValidator>();
            builder.Services.AddScoped<IValidator<Reservation>, ReservationValidator>();

            builder.Services.AddAutoMapper(options =>
            {
                options.AddProfile<MappingProfile>();
            });

            builder.Services.AddControllersWithViews();

            var app = builder.Build();

            using (var scope = app.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                var context = services.GetRequiredService<TripContext>();
                DbInitializer.Initialize(context);
            }

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthentication();
            app.UseAuthorization();
            app.MapRazorPages();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");

            app.MapControllerRoute(
                name: "trip",
                pattern: "Trip/{action=Index}/{id?}",
                defaults: new { controller = "Trip" });

            app.MapControllerRoute(
                name: "reservations",
                pattern: "Reservations",
                defaults: new { controller = "Reservation", action = "Index" });

            app.MapControllerRoute(
                name: "clients",
                pattern: "Clients",
                defaults: new { controller = "Client", action = "Index" });

            app.MapControllerRoute(
                name: "admin",
                pattern: "Admin",
                defaults: new { controller = "Admin", action = "Index" }
            );

            app.Run();
        }
    }
}
