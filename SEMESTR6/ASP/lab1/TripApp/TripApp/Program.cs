using BikeRentalSystemWeb.Data;
using Microsoft.AspNetCore.Authentication;
using Microsoft.EntityFrameworkCore;
using TripApp.Data;

namespace TripApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            builder.Services.AddDbContext<TripContext>(options =>
            options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultContext")));


            // Add services to the container.
            builder.Services.AddControllersWithViews();

            var app = builder.Build();

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

            app.UseAuthorization();

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

            app.Run();
        }
    }
}