# Zrozumienie wymagań

1. Nazwa obiektu: Klinika medyczna "HealthCare Plus"
2. Liczba pracowników: 15
3. Liczba urządzeń: 25 (w tym komputery lekarzy i sprzęt medyczny)
4. Usługi sieciowe: Przechowywanie i udostępnianie historii medycznych pacjentów oraz wyników badań.

# Wybór topologii sieci

Rozważmy najpierw nasze możliwości

## Topologia Gwiazdy:
### Zalety:

- Wydajność: Topologia gwiazdy zapewnia dobre osiągi, ponieważ każde urządzenie ma osobne połączenie z głównym switchem. To oznacza, że pasmo komunikacyjne jest dostępne dla każdego urządzenia, co minimalizuje opóźnienia i zapewnia niskie czasy odpowiedzi.

- Łatwość zarządzania: Ze względu na centralny punkt (główny switch), zarządzanie siecią jest proste. Diagnostyka, monitorowanie i konserwacja stają się znacznie bardziej intuicyjne.

- Redundancja: Topologia gwiazdy umożliwia łatwe wprowadzenie redundancji. Poprzez dodanie dodatkowych łączy lub switchy o możliwościach High Availability, można zminimalizować ryzyko przestojów.

### Wady:

- Ilość kabli: Konieczność połączenia każdego urządzenia bezpośrednio z głównym switchem oznacza, że potrzebne jest więcej kabli niż w innych topologiach. To może wiązać się z kosztami i problemami z zarządzaniem przewodami.

## Topologia Magistrali:

### Zalety:

- Kosztoszczędność: Topologia magistrali jest kosztoszczędna, ponieważ wymaga tylko jednego wspólnego kabla i prostego switcha centralnego. To może być atrakcyjne dla budżetów o ograniczonych zasobach.

### Wady:

- Brak redundancji: Jest to topologia podatna na awarie, ponieważ jedna uszkodzona linia główna może unieruchomić całą sieć. Brak redundancji wpływa na niezawodność i dostępność.

## Topologia Pierścienia:

### Zalety:

- Redundancja: Topologia pierścienia ma wbudowaną redundancję. W przypadku awarii jednego odcinka, dane nadal mogą krążyć w drugim kierunku, co zwiększa niezawodność sieci.

- Wydajność: Podobnie jak w topologii gwiazdy, każde urządzenie ma oddzielne połączenia, co wpływa na wydajność i minimalizuje opóźnienia.

### Wady:

- Skomplikowane zarządzanie: Zarządzanie siecią pierścienia może być bardziej skomplikowane niż w przypadku topologii gwiazdy, zwłaszcza w większych sieciach. Diagnozowanie problemów w pierścieniu może być trudniejsze.

## Wnioski

Dla kliniki medycznej "HealthCare Plus", najlepszym wyborem może być topologia gwiazdy. Jest to stabilne rozwiązanie, które zapewnia prosty dostęp do zarządzania siecią oraz pozwala na łatwe rozszerzenie sieci w przyszłości. Ponadto, można rozważyć wykorzystanie switchy z funkcją redundancji (np. stosowane w technologii High Availability), aby zapewnić niezawodność w przypadku awarii.

# Wybór Sprzętu sieciowego

### *Główny switch:* 

Centralnym urządzeniem w topologii gwiazdy będzie główny switch. Musi być to switch o odpowiedniej pojemności, który może obsłużyć wszystkie urządzenia w sieci, w tym 25 urządzeń. Wybierzmy model switcha o co najmniej 24 portach Ethernet 1 Gb/s, aby mieć zapas na przyszłe rozbudowy.

Przykładowy model: Cisco Catalyst 2960X-24PS-L lub odpowiednik innej renomowanej marki.

### *Router:* 

Chociaż topologia gwiazdy nie wymaga routera do przesyłania danych między podsieciami (ponieważ wszystkie urządzenia są podłączone bezpośrednio do switcha), warto rozważyć urządzenie z funkcjami zabezpieczeń, takie jak firewall i VPN, aby chronić poufność danych medycznych.

Przykładowy model: Cisco 2901 lub podobny.

### *Access Point (AP): *

Jeśli klinika potrzebuje dostępu do sieci bezprzewodowej dla swojego personelu lub pacjentów, należy uwzględnić access point. Wybierzmy model AP o dobrej przepustowości i obszarze działania, aby zapewnić odpowiednie pokrycie.

Przykładowy model: Ubiquiti UniFi AP-AC Pro lub równoważny model innej marki.

### *Przełączniki PoE:* 

W związku z wykorzystywaniem sprzętu medycznego, które może wymagać zasilania przez Ethernet (Power over Ethernet, PoE), warto rozważyć używanie przełączników PoE w celu zasilania tych urządzeń. Wymaga to również, aby główny switch obsługiwał PoE, lub możemy zainstalować osobny przełącznik PoE.

Przykładowy model: Cisco Catalyst 2960X-24PS-L (obsługuje PoE) lub odpowiednik innej marki.