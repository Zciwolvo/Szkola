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
<h1>Uniwersytet Bielsko-Bialski</h1>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<h1 style="text-align: center;"><b>LABORATORIUM</b></h1>
<h1 style="text-align:center"><b>Programowanie dla Internetu w technologii ASP.NET</b></h1>

&nbsp;

&nbsp;

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 1</b></h3>
<h2 style="text-align:center; border: none;">Layout, lista, szczegóły</h2>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

GRUPA: 2B / SEMESTR: 6 / ROK: 3

Igor Gawłowicz / 59096

<div style="page-break-after: always;"></div>

### Tworzenie Aplikacji ASP.NET:

1. **Stworzenie nowego projektu**: W ramach procesu tworzenia aplikacji ASP.NET wybierana jest odpowiednia szablonowa struktura projektu, w tym przypadku jest to "ASP.NET Core Web Application" dla najnowszej wersji ASP.NET Core.

2. **Struktura folderów**:

   - **Controllers**: W folderze tym znajdują się kontrolery, które obsługują żądania HTTP i decydują, które widoki mają zostać wyrenderowane.

   - **Models**: Folder ten zawiera modele danych aplikacji, reprezentujące encje lub obiekty używane przez aplikację.

   - **ViewModels**: Tutaj umieszcza się widoki modeli, które są używane do przekazywania danych z kontrolerów do widoków, co pomaga w separacji logiki biznesowej od warstwy prezentacji.

   - **Views**: W tym folderze znajdują się pliki widoków, które renderują interfejs użytkownika. Mogą one być napisane w języku HTML z dodatkami ASP.NET, takimi jak Razor.

### Struktura Bazowej Strony (Layout):

1. **Nagłówek (Header)**:

   - Logo: Logo aplikacji umieszczone jest w lewym górnym rogu nagłówka.

   - Nawigacja: Tworzony jest pasek nawigacyjny z linkami do różnych części aplikacji, przyjmujący formę menu pionowego lub poziomego w zależności od preferencji i stylu projektu.

2. **Główna Sekcja (Main Section)**:

   - Treść główna: W tej części layoutu umieszczana jest główna treść strony, takie jak lista artykułów, formularz wyszukiwania czy inne dane aplikacji.

3. **Stopka Strony (Footer)**:

   - Informacje o aplikacji: W stopce strony umieszcza się informacje o autorze, wersji aplikacji, latach działalności itp.

   - Linki pomocnicze: Stopka może zawierać linki do stron informacyjnych, regulaminu, polityki prywatności itp.

   - Dane kontaktowe: Można również umieścić dane kontaktowe, takie jak adres e-mail lub numer telefonu do wsparcia technicznego.

### Przebieg ćwiczenia

W ramach ćwiczenia napisaliśmy prostą stronę główną prezentującą wypożyczalnie rowerów, wykorzystaliśmy do tego prosty html i style napisane w css.

Z racji że korzystamy z technologii ASP.NET nie będziemy ograniczać się htmlem i cssem, dlatego następnym krokiem było stworzenie dynamicznej listy obiektów, gdzie każdy z nich ma swój odnośnik do dedykowanej strony przedstawiającej informacje na temat każdego z rowerów.

```cs
        <ul>
            @foreach (var item in Model)
            {
                <li>
                    <a asp-controller="Home" asp-action="Detail" asp-route-id="@item.Id">@item.Producer - @item.Model</a>
                </li>
            }
        </ul>
```

Przedstawiona została lista jednak, nie mamy jeszcze żadnej funkcji, która obsłuży te odnośniki.

Aby rozwiązać ten problem przejdziemy do pliku `HomeController.cs` i napiszemy kontroler obsługujący operacje `Detail`

```cs
        public IActionResult Detail(int id)
        {
            var bike = _bikes.FirstOrDefault(x => x.Id == id);
            return View(bike);

        }
```

Poza tym potrzebujemy także widoku, który będzie wyświetlany przy wywołaniu tego kontrolera, dlatego w folderze `Views/Home` stworzymy sobie nowy plik `Detail.cshtml`

```cs
@using BikeRentalSystemWeb.ViewModels;
@model BikeDetailViewModel



<ul>
    <li>
        <p>Model: @Model.Model</p>
    </li>
    <li>
        <p>Producent: @Model.Producer</p>
    </li>
    <li>
        <p>Kolor: @Model.Color</p>
    </li>
    <li>
        <p>Liczba biegów: @Model.NumberofGears</p>
    </li>
    <li>
        <p>Typ roweru: @Model.BikeType</p>
    </li>
    <li>
        <p>Ilość: @Model.NumberofBikes</p>
    </li>
</ul>

```

W ten sposób wszystko zacznie nam działać w oczekiwany sposób:

- Strona główna wygląda tak jak ją napisaliśmy

![homepage](image.png)

- Szczegóły także wyświetlają się poprawnie

![Detail](image-1.png)

### Wnioski

ASP.NET to technologia opracowana przez Microsoft, która umożliwia budowanie dynamicznych aplikacji internetowych i serwisów sieciowych. Dzięki ASP.NET programiści mogą tworzyć aplikacje webowe, które są skalowalne, wydajne i bezpieczne. Ta platforma oferuje szeroki zakres narzędzi do projektowania interfejsu użytkownika, zarządzania danymi oraz obsługi żądań HTTP. Pozwala również na integrację z różnymi bazami danych i serwisami zewnętrznymi. W rezultacie ASP.NET stanowi wszechstronne narzędzie do tworzenia zaawansowanych aplikacji internetowych dla różnych dziedzin, w tym e-commerce, zarządzania zasobami ludzkimi, systemów informatycznych dla firm i wiele innych.
