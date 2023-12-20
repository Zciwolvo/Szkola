#include <iostream>
#include <iomanip>
#include <chrono>

int main() 
{
    const int n = 1024; // rozmiar tablicy
    double* tab = new double[n]; // tworzenie obietu w pamięci dla tablicy dynamicznej
    for (int i = 0; i < n; ++i) tab[i] = 0.1; //wypełnianie tablicy
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    double s1 = 0.0;
    double s2 = 0.0;
    double s3 = 0.0;
    double s4 = 0.0;
    double s5 = 0.0;
    double s6 = 0.0;
    double s7 = 0.0;
    double s8 = 0.0;
    double s9 = 0.0;
    double s10 = 0.0;
    double s11 = 0.0;
    double s12 = 0.0;
    double s13 = 0.0;
    double s14 = 0.0;
    double s15 = 0.0;
    double s16 = 0.0;

    for (int t = 0; t < n * n; ++t) 
    {
        for (int i = 0; i < n; ++i) 
        {
            switch (t % 16) {
                case 0:
                    s1 += tab[i];
                    break;
                case 1:
                    s2 += tab[i];
                    break;
                case 2:
                    s3 += tab[i];
                    break;
                case 3:
                    s4 += tab[i];
                    break;
                case 4:
                    s5 += tab[i];
                    break;
                case 5:
                    s6 += tab[i];
                    break;
                case 6:
                    s7 += tab[i];
                    break;
                case 7:
                    s8 += tab[i];
                    break;
            }
        }
    }

    // Sumowanie wyniku końcowego z obu buforów
    double final_sum = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8;

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << std::fixed;
    std::cout << "s1 = " << s1 << std::endl;
    std::cout << "s2 = " << s2 << std::endl;
    std::cout << "s3 = " << s3 << std::endl;
    std::cout << "s4 = " << s4 << std::endl;
    std::cout << "s5 = " << s5 << std::endl;
    std::cout << "s6 = " << s6 << std::endl;
    std::cout << "s7 = " << s7 << std::endl;
    std::cout << "s8 = " << s8 << std::endl;
    std::cout << "s9 = " << s9 << std::endl;
    std::cout << "s10 = " << s10 << std::endl;
    std::cout << "s11 = " << s11 << std::endl;
    std::cout << "s12 = " << s12 << std::endl;
    std::cout << "s13 = " << s13 << std::endl;
    std::cout << "s14 = " << s14 << std::endl;
    std::cout << "s15 = " << s15 << std::endl;
    std::cout << "s16 = " << s16 << std::endl;
    std::cout << "1. suma = " << std::setprecision(30) << final_sum << " ";
    std::cout << "Czas wykonania = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
    delete[] tab; //kasowanie tablicy
    return 0;
}
