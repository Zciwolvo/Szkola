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
<h1>LABORATORIUM PROJEKTOWANIE I OBSŁUGA SIECI KOMPUTEROWYCH I</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>03.01.2024</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Rok studiów:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>3</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Semestr:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>5</Rtext>
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
        <Rtext>12</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Pakiet Tracer - Konfiguracja WPA2 Enterprise WLAN na WLC

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Pakiet Tracer - Konfiguracja WPA2 Enterprise WLAN na WLC

### Część 1: Utworzenie nowej sieci LAN

#### Krok 1: Utwórz nowy interfejs VLAN
1. Zalogowaliśmy się do interfejsu zarządzania WLC za pomocą przeglądarki.
2. Dodaliśmy nowy interfejs VLAN o nazwie WLAN-5 z ID VLAN 5. Skonfigurowaliśmy go z adresem IP 192.168.5.254, maską podsieci 255.255.255.0, bramką domyślną 192.168.5.1 oraz serwerem DHCP 192.168.5.1.

#### Krok 2: Skonfiguruj WLC do korzystania z serwera RADIUS
1. Skonfigurowaliśmy adres serwera RADIUS na WLC (IP: 172.31.1.254) oraz współdzielony sekret (Cisco123).

#### Krok 3: Utwórz nową sieć LAN
1. Stworzyliśmy nową sieć WLAN o nazwie "Pracownicy Piętra 2" z SSID SSID-5, korzystając z interfejsu VLAN utworzonego wcześniej (WLAN-5).
2. Włączyliśmy funkcjonalność sieci WLAN i skonfigurowaliśmy FlexConnect Local Switching i FlexConnect Local Auth.

#### Krok 4: Skonfiguruj zabezpieczenia WLAN
1. Zamiast WPA2-PSK, skonfigurowaliśmy nową sieć WLAN do korzystania z WPA2-Enterprise.
2. Skonfigurowaliśmy serwer RADIUS jako autoryzację dla użytkowników sieci.

### Część 2: Skonfiguruj zakres DHCP i SNMP

#### Krok 1: Skonfiguruj zakres DHCP
1. Skonfigurowaliśmy zakres DHCP na WLC dla zarządzania siecią przewodową, ustalając pulę adresów od 192.168.200.240 do 192.168.200.249.

#### Krok 2: Skonfiguruj SNMP
1. Skonfigurowaliśmy serwer SNMP z adresem IP 172.31.1.254 i community stringiem "WLAN_SNMP".

### Część 3: Podłącz hosty do sieci

#### Krok 1: Skonfiguruj hosta do podłączenia do sieci przedsiębiorstwa
1. Skonfigurowaliśmy profil WLAN w aplikacji Wireless Host dla sieci WPA2-Enterprise.
2. Zalogowaliśmy się z nazwą użytkownika "user1" i hasłem "User1Pass".

#### Krok 2: Testuj łączność
1. Host otrzymał adres IP z sieci 192.168.5.0/24.
2. Pomyślnie przeprowadziliśmy pingowanie bramy domyślnej, przełącznika SW1 i serwera RADIUS, co potwierdziło pełną łączność w topologii.

### Pytania refleksyjne

1. Serwer RADIUS uwierzytelnia zarówno WLC, jak i hosta bezprzewodowego. Jest to konieczne w celu ochrony tabel użytkowników i haseł przed nieautoryzowanymi urządzeniami.
   
2. WPA2-Enterprise jest bardziej zaawansowane od WPA2-PSK, ponieważ umożliwia zarządzanie wieloma unikalnymi kontami użytkowników, audyt działań użytkowników oraz łatwe dodawanie i usuwanie użytkowników w miarę zmian w przedsiębiorstwie. Jest bardziej bezpieczne, ponieważ każdy użytkownik ma własną nazwę użytkownika i hasło, co utrudnia niepowołany dostęp do sieci. Dodatkowo, zmiana hasła nie wymaga informowania wszystkich użytkowników, co zmniejsza ryzyko jego wykradzenia.

## Packet Tracer - Rozwiązywanie problemów z siecią WLAN

### Część 1: Rozwiązywanie problemów sieci

#### Krok 1: Testuj łączność
1. Przeprowadziliśmy test łączności między różnymi hostami bezprzewodowymi a serwerem sieciowym za pomocą zarówno adresów IP, jak i adresów URL www.netacad.pt.
2. Zarejestrowaliśmy hosty, które nie mogły uzyskać dostępu do serwera WWW w tabeli w kroku 2.

#### Krok 2: Badanie problemów i rejestracja wyników
1. Dokonaliśmy badania problemów z łącznością dla każdego hosta. Problemy mogą dotyczyć konfiguracji hosta lub innych komponentów sieci bezprzewodowej.
2. Uzupełniliśmy tabelę z wynikami:

| Urządzenie          | Sieć          | Problem                                                        | Rozwiązanie                                             |
|---------------------|---------------|----------------------------------------------------------------|---------------------------------------------------------|
| Smartphone, Tablet PC, Laptop | Domowa  | Brak dostępu do serwera za pomocą adresu URL. Błędna konfiguracja adresu DNS na serwerze DHCP routera. | Zmiana adresu statycznego na serwerze DHCP routera na 10.100.100.254 |
| Tablet PC           | Domowa  | Klient skonfigurowany jako statyczny.                          | Powinien być ustawiony na DHCP.                          |
| Router bezprzewodowy | Domowa  | Interfejs internetowy jest ustawiony jako statyczny.           | Ustawienie interfejsu internetowego na DHCP.             |
| WLC                 | Przedsiębiorstwo | WLAN Wireless VLAN 20 nie jest włączony.                       | Włączenie WLAN i zastosowanie zmian.                     |
| Laptop 2            | Przedsiębiorstwo | Laptop 2 nie łączy się z Wireless VLAN 20. Błędna nazwa użytkownika w profilu klienta. | Zmiana nazwy użytkownika na "user2".                     |
| WLC                 | Przedsiębiorstwo | Laptop 1 nie może połączyć się z WLAN.                        | Zmiana metody uwierzytelniania na PSK, wprowadzenie wartości PSK z tabeli WLAN. |

### Część 2: Napraw problemy

1. Dokonaliśmy zmian w konfiguracji urządzeń, aby hosty mogły osiągnąć łączność z siecią.
2. Przetestowaliśmy, czy wszystkie hosty mogą osiągnąć cel komunikacji, tj. połączenie się z serwerem WWW za pomocą adresu IP oraz URL.

- Zmieniono adres statyczny na serwerze DHCP routera domowego na 10.100.100.254.
- Użyto przewodu miedzianego do połączenia PC Administracyjnego z routerem bezprzewodowym domowym.
- Zmieniono ustawienia serwera DNS IP na 10.100.100.254 i zapisano ustawienia.
- Wykonano odnowienie IP na smartfonie, laptopie i PC domowym.
- Tablet PC został zmieniony na ustawienia DHCP.
- Interfejs internetowy routera bezprzewodowego został ustawiony na DHCP.
- Włączono WLAN 20 i zastosowano zmiany na WLC.
- Zmieniono nazwę użytkownika na "user2" w Laptopie 2.
- Zmieniono konfigurację profilu WLAN 20 na Laptopie 2, uwierzytelniając za pomocą WPA2-Enterprise.
- W WLC zmieniono Authentication Key Management dla WLAN-Wireless VLAN 10 na PSK.

Po wykonaniu tych zmian sprawdziliśmy, czy Laptop 1 połączył się z WLAN-Wireless VLAN 10.

## Wnioski


### Pakiet Tracer - Konfiguracja WPA2 Enterprise WLAN na WLC

1. **Tworzenie nowej sieci LAN:**
    - Utworzono nowy interfejs VLAN z odpowiednimi parametrami, co pozwoliło na wydzielenie odrębnej sieci dla "Pracownicy Piętra 2".
    - Skonfigurowano serwer RADIUS, który jest istotny dla autoryzacji użytkowników w sieci.

2. **Konfiguracja zabezpieczeń WLAN:**
    - Przeprowadzono zmianę z WPA2-PSK na WPA2-Enterprise, co umożliwia bardziej zaawansowane zarządzanie użytkownikami i zwiększa poziom bezpieczeństwa sieci.

3. **Skonfiguruj zakres DHCP i SNMP:**
    - Ustawiono zakres DHCP dla zarządzania siecią przewodową, umożliwiając przydział adresów IP dla urządzeń.
    - Skonfigurowano serwer SNMP, który wspiera zarządzanie siecią.

4. **Podłączenie hostów do sieci:**
    - Pomyślnie skonfigurowano hostów, zapewniając im łączność z nową siecią przedsiębiorstwa.
    - Testowano łączność poprzez pingowanie różnych urządzeń w sieci, co potwierdziło pełną łączność w topologii.

### Packet Tracer - Rozwiązywanie problemów z siecią WLAN

1. **Rozwiązywanie problemów sieci:**
    - Wykryto różne problemy w konfiguracji sieci bezprzewodowej, takie jak błędna konfiguracja DNS, nieprawidłowe ustawienia interfejsów i problemy z uwierzytelnianiem użytkowników.
    - Poprawnie zidentyfikowano problemy i zastosowano odpowiednie rozwiązania.

2. **Naprawa problemów:**
    - Wdrożono zmiany w konfiguracji urządzeń, takie jak zmiana adresu DNS, ustawienia interfejsów, poprawienie konfiguracji użytkowników i protokołów uwierzytelniania.
    - Po zastosowaniu zmian przetestowano łączność, aby upewnić się, że wszystkie hosty mogą poprawnie się połączyć z siecią.
