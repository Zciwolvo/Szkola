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

