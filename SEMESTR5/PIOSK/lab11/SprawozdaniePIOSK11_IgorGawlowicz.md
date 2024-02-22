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
            <Rtext>20.12.2023</Rtext>
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
        <Rtext>11</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguracja sieci bezprzewodowej

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Konfiguracja sieci bezprzewodowej

### Część 1: Podłącz się do routera bezprzewodowego

#### Krok 1: Podłącz administratora do WR.

Podłączymy Admina do WR za pomocą miedzianego kabla ethernet do slotów FastEthernet0 w Adminie i GigabitEthernet1 w WR

#### Krok 2: Skonfiguruj Admin, aby użył protokołu DHCP.

Następnie w konfiguracji PC Admin musimy ustawić protokół DHCP 

*Jaki jest adres IP komputera?*

192.168.0.100

*Jaka jest maska podsieci komputera?*

255.255.255.0

*Jaka jest domyślna brama dla komputera?*

192.168.0.1

#### Krok 3: Połącz się z interfejsem WWW WR.

Po uruchomieniu przeglądarki i wejścia na adres lokalny routera, możemy zobaczyć konfiguracje sieci

*Czy adres IP Admin jest w tym zakresie? Czy tak miało być? Wyjaśnij swoją odpowiedź.* 

Tak. Administrator ma adres IP 192.168.0.100/24, który należy do podsieci 192.168.0.0/24 i mieści się w zakresie od 192.168.0.100 do 192.168.0.149. To jest oczekiwane, ponieważ Administrator uzyskał informacje dotyczące swojego adresu IP od WR za pomocą protokołu DHCP.

#### Krok 4: Skonfiguruj port internetowy WR.

Zmieniliśmy tutaj DHCP na statyczny adres i uzupełniliśmy go w sposób podany w zadaniu, następnie chciałem zaaplikować zmiany ale niestety doszło do timeouta, więc odczekaliśmy aż połączenie zostanie ustabilizowane, następnie udało się zaaplikować zmiany i mogliśmy przejść dalej.

### Część 2: Konfigurowanie ustawień łączności bezprzewodowej

#### Krok 1: Skonfiguruj SSID na WR.

Następnie w konfiguracji sieci zmienimy sieć bez przewodową a dokładnie jej SSID i bazowy kanał, a także wyłączymy obie sieci o częstotliwość 5GHz.

#### Krok 2: Skonfiguruj ustawienia zabezpieczeń sieci bezprzewodowej.

Teraz ustawimy zabezpieczenia sieci bezprzedwodowej na WPA2 Personal, ustawimy rodzaj enkrypcji oraz ustawimy hasło.

#### Krok 3: Połącz klientów bezprzewodowych.

W tym kroku połączymy oba laptopy do poprzednio utworzonej sieci bezprzewodowej.

### Część 3: Łączenie klientów bezprzewodowych z punktemdostępu

#### Krok 1: Skonfiguruj punkt dostępu.

Teraz musimy połączyć kablem ethernet nasz punkt dostępu do routera WR i skonfigurować sieć tak żeby zgadzała się z tym co wcześniej ustawiliśmy w konfiguracji sieci.

#### Krok 2: Połącz klientów bezprzewodowych.

Możemy teraz zauważyć w sieciach bezprzewodowych z laptopa 3, że pojawiła nam się druga sieć bezprzewodowa, ponieważ access point przekazał sieć dalej.

### Część 4: Inne zadania administracyjne


#### Krok 1: Zmień hasło dostępu WR.

W sekcji administration/Management ustawiliśmy hasło na cisco i zalogowaliśmy się przy użyciu nowych danych.

#### Krok 2: Zmień zakres adresów DHCP w WR.

Wróciliśmy do zakładki Setup/Basic Setup i ustawiliśmy adresy zgodnie z poleceniem.

## Pakiet Tracer - Konfiguracja podstawowej sieci WLAN w WLC

### Część 1: Monitorowanie WLC

#### Krok 1: Oczekiwanie na zbieżność STP w sieci

Poczekaj, aż protokół STP zbiegnie w sieci. Możesz kliknąć przycisk Przyspiesz Czas w Packet Tracer, aby przyspieszyć ten proces. Kontynuuj, gdy wszystkie diody łącz są zielone.

#### Krok 2: Połączenie się z kontrolerem WLC

a. Przejdź do pulpitu PC Administratora i otwórz przeglądarkę. Wprowadź adres IP zarządzania WLC-1 z tabeli adresacji do paska adresu. Musisz określić protokół HTTPS.

b. Kliknij "Login" i wprowadź następujące dane uwierzytelniające: Nazwa użytkownika: admin, Hasło: Cisco123. Po krótkim opóźnieniu zobaczysz ekran Podsumowania Monitora WLC.

c. Przewiń ekran Podsumowania Monitora.

*Co można dowiedzieć się z tego ekranu?*

**Można tutaj znaleźć wiele wartościowych informacji, w tym dane operacyjne dotyczące WLC, informacje o znanych punktach dostępowych i podłączonych klientach, a także punkty dostępowe i klientów dzikich, które zostały wykryte w sieci.**

*Czy WLC jest podłączony do punktu dostępowego?*

**Tak, WLC jest podłączony do jednego punktu dostępowego. Jest to widoczne w sekcji Podsumowanie punktów dostępowych na stronie.**

d. Kliknij Szczegóły obok Wszystkie AP w sekcji Podsumowanie punktów dostępowych na stronie. Jakie informacje można znaleźć dotyczące punktów dostępowych na ekranie Wszystkie AP?

Informacje wyświetlane na WLC obejmują nazwę AP, adres IP AP, model urządzenia, MAC, wersję oprogramowania, status operacyjny, źródło zasilania, itp.

### Część 2: Tworzenie sieci LAN bezprzewodowej

#### Krok 1: Utwórz i włącz sieć LAN bezprzewodową

a. Kliknij WLANs na pasku menu WLC. Zlokalizuj rozwijane pole w prawym górnym rogu ekranu WLANs. Będzie mówić Utwórz nowy. Kliknij Przejdź, aby utworzyć nową sieć LAN bezprzewodową.

b. Wprowadź Nazwę profilu nowej sieci LAN. Użyj nazwy profilu Pracownicy Piętra 2. Przypisz SSID SSID-5 do sieci LAN. Hosty będą musiały używać tego SSID do dołączenia do sieci.

c. Wybierz identyfikator dla sieci LAN. Ta wartość to etykieta, która będzie używana do identyfikacji sieci LAN w innych wyświetlaniach. Wybierz wartość 5, aby zachować spójność z numerem VLAN i SSID. To nie jest wymóg, ale pomaga zrozumieć topologię.

d. Kliknij Zastosuj, aby uaktywnić te ustawienia.

e. Teraz, gdy sieć LAN została utworzona, możesz skonfigurować funkcje sieci. Kliknij Włącz, aby sieć LAN była funkcjonalna. To jest częsty błąd, żeby przypadkowo pominąć ten krok.

f. Wybierz interfejs VLAN, który będzie używany dla sieci LAN. WLC będzie używał tego interfejsu do ruchu użytkownika w sieci. Kliknij pole rozwijane dla Interfejs/Grupa interfejsów (G). Wybierz interfejs WLAN-5. Ten interfejs został wcześniej skonfigurowany na WLC dla tej aktywności.

g. Kliknij zakładkę Zaawansowane.

h. Przewiń w dół do części FlexConnect na stronie. Kliknij, aby włączyć FlexConnect Local Switching i FlexConnect Local Auth.

i. Kliknij Zastosuj, aby włączyć nową sieć LAN. Jeśli zapomnisz to zrobić, sieć LAN nie będzie działać.

#### Krok 2: Zabezpiecz sieć LAN

Nowa sieć LAN obecnie nie ma ustawionego żadnego zabezpieczenia. Ta sieć LAN początkowo będzie używać zabezpieczenia WPA2-PSK. W innym zadaniu skonfigurujesz tę sieć LAN, aby używała WPA2-Enterprise, znacznie lepsze rozwiązanie dla większych sieci bezprzewodowych.

a. W ekranie Edycji sieci LAN dla sieci Pracownicy Piętra 2, kliknij zakładkę Zabezpieczenia. W zakładce Warstwa 2 wybierz WPA+WPA2 z rozwijanej listy Zabezpieczenia warstwy 2. To ujawni parametry WPA.

b. Zaznacz pole wyboru obok Zasady WPA2. To ujawni dodatkowe ustawienia zabezpieczeń. W Zarządzaniu kluczem autentykacji włącz PSK.

c. Teraz możesz wprowadzić współdzielony klucz, który będzie używany przez hosty do dołączenia do sieci LAN. Użyj Cisco123 jako hasła.

d. Kliknij Zastosuj, aby zapisać te ustawienia.

#### Krok 3: Weryfikacja ustawień
a. Po zastosowaniu konfiguracji, kliknij Wstecz. To przeniesie Cię z powrotem do ekranu sieci LAN.

Jakie informacje o nowej sieci LAN są dostępne na tym ekranie?
Nazwa sieci LAN, SSID, polityka zabezpieczeń i status administratora są dostępne tutaj. Warto

### Wnioski

Podczas monitorowania kontrolera WLC uzyskaliśmy istotne informacje o sieci i jej urządzeniach. Pomyślnie utworzyliśmy i zabezpieczyliśmy nową sieć LAN, zapewniając funkcjonalność oraz odpowiednie zabezpieczenia dla przyszłych użytkowników. Dzięki tym krokom zwiększyliśmy kontrolę i bezpieczeństwo naszej sieci bezprzewodowej.