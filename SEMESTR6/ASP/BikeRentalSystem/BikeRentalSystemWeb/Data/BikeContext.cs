using BikeRentalSystemWeb.Models;
using Microsoft.EntityFrameworkCore;



namespace BikeRentalSystemWeb.Data
{
    public class BikeContext : DbContext
    {
        public BikeContext(DbContextOptions<BikeContext> options) : base(options)
        {
        }

        public DbSet<Bike> Bikes { get; set; }


        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Bike>().ToTable("Bike");
        }
    }
}
