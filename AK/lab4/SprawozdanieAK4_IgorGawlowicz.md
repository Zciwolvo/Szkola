<style>
h1, h4, h2 {
    border-bottom: 0;
    display:flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
      }
      
centerer{
    display: grid;
    grid-template-columns: 6fr 1fr 4fr;
    grid-template-rows: 1fr;

}
rectangle{
    border: 1px solid black;
    margin: 0px 50px 0px 50px;
    width: 200px;
    height: 4em;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
}
Ltext{
    margin: auto auto auto 0;
    font-weight: bold;
    margin-left: 4em
}
Rtext{
    margin: auto;
}

row {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center; 
}
 </style>

<p align="center">
  <img src="./ubblogo.png" alt="ubb logo"/>
</p>

<h3 style="text-align:center"><b>Wydział budowy maszyn i informatyki</b></h3>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<h2 style="text-align:center; border: none;"><b>Architektura komputerów</b></h2>
<h3 style="text-align:center; border: none;">(Laboratorium №4)</h3>

**Temat ćwiczenia:  Praca potokowa procesorów**

Data wykonania ćwiczenia: 20.12.2023

&nbsp;

&nbsp;

Igor Gawłowicz

<div style="page-break-after: always;"></div>

1. Wprowadzenie
Praca potokowa procesorów to technika zwiększania wydajności procesorów poprzez
równoczesne wykonanie wielu instrukcji w różnych fazach procesu wykonawczego.
Procesory wykonują wiele operacji na danych, takie jak pobieranie danych z pamięci,
dekodowanie instrukcji, wykonanie operacji arytmetycznych itp. Praca potokowa polega
na podzieleniu tych operacji na kilka etapów i równoczesnym przetwarzaniu różnych
instrukcji w różnych etapach.

Główne etapy potoku w procesorze to:
- Pobieranie instrukcji: W tym etapie procesor pobiera instrukcje z pamięci programu.
- Dekodowanie instrukcji: Procesor dekoduje pobrane instrukcje, rozumiejąc jakie operacje należy wykonać.
- Wykonywanie operacji: Procesor wykonuje właściwe operacje, takie jak operacje arytmetyczne, logiczne itp.
- Dostęp do pamięci: Jeśli instrukcje wymagają dostępu do pamięci, procesor odczytuje lub zapisuje dane w pamięci.
- Zapis wyników: Wyniki operacji są zapisywane w odpowiednich rejestrach lub pamięci.
  
Dzięki pracy potokowej, różne instrukcje mogą być równocześnie w różnych fazach
procesu wykonawczego, co pozwala na zwiększenie wydajności procesora. Praca
potokowa umożliwia również zmniejszenie czasu wykonywania pojedynczej instrukcji,
co przyspiesza ogólny czas wykonywania programu.
Niemniej jednak praca potokowa może napotykać na pewne wyzwania, takie jak
zależności między instrukcjami, które mogą powodować opóźnienia, oraz zagadnienia
związane z równoważeniem obciążenia potoku, aby zapewnić równomierne
wykorzystanie wszystkich etapów.

2. Zadanie do zrealizowania:
    2.1. Przeanalizuj poniższy kod pod kątem wykorzystania potoków. Zaproponuj
    modyfikacje kodu w celu lepszego wykorzystania potoków poprzez rozpisanie
    najbardziej wewnętrznej części pętli for:

```cpp
// Wersja v1 programu z jednym buforem „s1”
#include <iostream>
#include <iomanip>
#include <chrono>

int main() 
{
    const int n = 1024; // rozmiar tablicy
    double* tab = new double[n]; // tworzenie obietu w pamięci dla tablicy dynamicznej
    for (int i = 0; i < n; ++i) tab[i] = 0.0625; //wypełnianie tablicy
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    double s1 = 0.0; //bufor dla sumy wszystkich elementów tablicy
    //poniższy fragment należy zmienić
    for (int t = 0; t < n * n; ++t) 
    {
        for (int i = 0; i < n; ++i) 
        {
            s1 += tab[i];
        }
    }
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << std::fixed;
    std::cout << "1. suma = " << std::setprecision(30) << s1 << " ";
    std::cout << "Czas wykonania = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
    delete[] tab; //kasowanie tablicy
    return 0;
}
```

Początkowo program zwraca nam taki wynik

```bash
suma = 67108864.000000000000000000000000000000 Czas wykonania = 4727504[µs]
```

z użyciem 2 buforów dla tymczasowych wyników pośrednich s1 i s2;

```cpp
#include <iostream>
#include <iomanip>
#include <chrono>

int main() 
{
    const int n = 1024; // rozmiar tablicy
    double* tab = new double[n]; // tworzenie obietu w pamięci dla tablicy dynamicznej
    for (int i = 0; i < n; ++i) tab[i] = 0.0625; //wypełnianie tablicy
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    double s1 = 0.0; // bufor pierwszy
    double s2 = 0.0; // bufor drugi

    for (int t = 0; t < n * n; ++t) 
    {
        for (int i = 0; i < n; ++i) 
        {
            if (t % 2 == 0) {
                s1 += tab[i];
            } else {
                s2 += tab[i];
            }
        }
    }

    // Sumowanie wyniku końcowego z obu buforów
    double final_sum = s1 + s2;

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << std::fixed;
    std::cout << "s1 = " << s1;
    std::cout << "s2 = " << s2 << std::endl;
    std::cout << "1. suma = " << std::setprecision(30) << final_sum << " ";
    std::cout << "Czas wykonania = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
    delete[] tab; //kasowanie tablicy
    return 0;
}
```

Wynik

```bash
s1 = 33554432.000000s2 = 33554432.000000
1. suma = 67108864.000000000000000000000000000000 Czas wykonania = 4993724[µs]
```

Zasada przy następnych będzie taka sama więc przejdę od razu do tabeli z wynikami

```bash
s1 = 16777216.000000
s2 = 16777216.000000
s3 = 16777216.000000
s4 = 16777216.000000
1. suma = 67108864.000000000000000000000000000000 Czas wykonania = 5235796[µs]
```

```bash
s1 = 8388608.000000
s2 = 8388608.000000
s3 = 8388608.000000
s4 = 8388608.000000
s5 = 8388608.000000
s6 = 8388608.000000
s7 = 8388608.000000
s8 = 8388608.000000
1. suma = 67108864.000000000000000000000000000000 Czas wykonania = 4508928[µs]
```

```bash
s1 = 4194304.000000
s2 = 4194304.000000
s3 = 4194304.000000
s4 = 4194304.000000
s5 = 4194304.000000
s6 = 4194304.000000
s7 = 4194304.000000
s8 = 4194304.000000
s9 = 4194304.000000
s10 = 4194304.000000
s11 = 4194304.000000
s12 = 4194304.000000
s13 = 4194304.000000
s14 = 4194304.000000
s15 = 4194304.000000
s16 = 4194304.000000
1. suma = 67108864.000000000000000000000000000000 Czas wykonania = 5315598[µs]
```

| Wersja kodu | Liczba buforów | Czas programu |
| --- | --- | --- |
| v1 | 1 | 4.727 |
| v2 | 2 | 4.993 |
| v3 | 4 | 5.235 |
| v4 | 8 | 4.508 |
| v5 | 16 | 5.315 |

2.2 

| Wersja kodu | Liczba buforów | Suma wszystkich elementów |
| --- | --- | --- |
| v1 | 1 | 107374180.705882295966148376464843750000 |
| v2 | 2 | 107374183.411764696240425109863281250000 |
| v3 | 4 | 107374182.823529407382011413574218750000 |
| v4 | 8 | 107374182.147058829665184020996093750000 |
| v5 | 16 | 107374182.294117674231529235839843750000 |