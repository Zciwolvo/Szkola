<style>
h1, h4 {
    border-bottom: 0;
    display:flex;
    flex-direction: column;
    align-items: center;
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
<h1>LABORATORIUM CYBERBEZPIECZEŃSTWO</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>25.11.2024</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Rok studiów:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>4</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Semestr:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>7</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Grupa studencka:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>2</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Grupa laboratoryjna:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>2B</Rtext>
        </rectangle>
    </div>
</centerer>

&nbsp;

&nbsp;

<row>
    <b>Ćwiczenie nr.</b>
    <rectangle>
        <Rtext>4</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Licencje oprogramowania komputerowego

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Sprawozdanie na temat zabezpieczeń CAPTCHA i Google reCAPTCHA

### 1. Wprowadzenie

Licencja oprogramowania to umowa określająca zasady korzystania z programu komputerowego. Jest zawierana pomiędzy właścicielem praw autorskich do oprogramowania a użytkownikiem. W praktyce użytkownicy najczęściej spotykają się z licencjami typu **EULA (End User License Agreement)**, które szczegółowo określają ograniczenia dotyczące użytkowania oprogramowania. Ograniczenia te mogą dotyczyć m.in. liczby urządzeń, na których można zainstalować program, czy rodzaju użytkowania (komercyjne/domowe).

Rodzaje licencji różnią się pod względem możliwości i ograniczeń. Wśród najczęściej spotykanych typów można wyróżnić:

- **Freeware**: Oprogramowanie darmowe, ale najczęściej zamknięte źródłowo.
- **Shareware**: Programy udostępniane bezpłatnie na określony czas lub z ograniczoną funkcjonalnością.
- **Adware**: Oprogramowanie finansowane przez reklamy.
- **Trialware**: Programy dostępne w pełnej funkcjonalności przez ograniczony czas.
- **Demoware**: Oprogramowanie o ograniczonej funkcjonalności lub dostępne w wersji próbnej.

Każda licencja definiuje także sposoby zabezpieczeń, często korzystając z algorytmów szyfrujących, takich jak szyfr Cezara czy szyfr Vigenère'a.

### 2. Cel i realizacja zadania

Zadanie polegało na zaprojektowaniu systemu licencyjnego dla oprogramowania w modelu **Demoware**. Kluczowe wymagania obejmowały:

1. Ograniczenie funkcjonalności programu – w tym przypadku możliwość otwierania plików o rozmiarze nieprzekraczającym 100 KB.
2. Implementację algorytmu szyfrowania i deszyfrowania klucza licencji przy użyciu szyfru Cezara.

### 3. Rozwiązanie

W celu realizacji zadania zaimplementowano aplikację internetową w oparciu o framework Flask. Kluczowe funkcjonalności obejmowały:

- **Mechanizm szyfrowania klucza licencji**: Wykorzystano szyfr Cezara do szyfrowania i deszyfrowania klucza licencyjnego. Klucz „UnlockKey123” umożliwiał zniesienie ograniczeń rozmiaru pliku.
- **Ograniczenie funkcjonalności**: Użytkownicy z podstawową wersją licencji mogli otwierać pliki o rozmiarze do 100 KB. Próba otwarcia większego pliku kończyła się komunikatem o błędzie.
- **Elastyczność rozmiaru plików**: Po wprowadzeniu poprawnego klucza licencji limit rozmiaru pliku był zwiększany do 10 MB.

Kod realizujący zadanie zawierał zabezpieczenia przed nieautoryzowanym dostępem oraz możliwość dynamicznej zmiany parametrów w zależności od podanego klucza.

### 4. Wykorzystane algorytmy szyfrujące

- **Szyfr Cezara**: Każda litera klucza była przesuwana o 3 pozycje w alfabecie. W przypadku deszyfrowania kierunek przesunięcia był odwrotny. Algorytm ten, mimo prostoty, pozwolił na skuteczne zarządzanie kluczem licencji.

### 5. Wnioski

Zrealizowane zadanie pozwoliło na praktyczne wykorzystanie wiedzy o licencjonowaniu oprogramowania oraz implementacji systemów zabezpieczeń. Wprowadzone ograniczenia funkcjonalności w wersji **Demoware** spełniały wymagania zadania, a zastosowanie szyfru Cezara umożliwiło sprawne zarządzanie kluczami licencyjnymi.

Rozwiązanie to może być rozbudowane w przyszłości, np. o bardziej zaawansowane algorytmy szyfrujące czy dodatkowe typy licencji, co pozwoli na zwiększenie bezpieczeństwa i elastyczności systemu.
