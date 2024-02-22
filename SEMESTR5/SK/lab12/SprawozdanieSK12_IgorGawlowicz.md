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
<h1>LABORATORIUM SIECI KOMPUTEROWYCH</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>18.05.2023</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Rok studiów:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>2</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Semestr:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>4</Rtext>
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

<b>Temat: </b> Podział sieci na podsieci

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Część 1: Podziel przypisaną sieć na podsieci

### Krok 1: Przygotuj schemat podziału na podsieci spełniający wymagania co do ilości podsieci oraz adresów hostów.

_W tym scenariuszu jesteś technikiem sieciowym skierowanym do zainstalowania nowej sieci dla klienta. Musisz utworzyć wiele podsieci spełniających poniższe wymagania, używając adresów 192.168.0.0/24._

_a. Pierwszą podsiecią jest sieć LAN-A. Potrzebujesz minimum 50 adresów IP dla komputerów._

**Aby utworzyć sieć LAN-A o minimalnej liczbie 50 adresów IP, możesz użyć adresu 192.168.0.0/26. Adres sieci to 192.168.0.0, a adres rozgłoszeniowy to 192.168.0.63. Pozostałe adresy IP w tej podsieci będą dostępne dla hostów.**

_b. Druga podsieć to sieć LAN-B. Potrzebujesz minimum 40 adresów IP dla komputerów._

**Podobnie, aby utworzyć sieć LAN-B o minimalnej liczbie 40 adresów IP, możesz użyć adresu 192.168.0.64/26. Adres sieci to 192.168.0.64, a adres rozgłoszeniowy to 192.168.0.127. Pozostałe IP w tej podsieci będą dostępne dla hostów.**

_c. Potrzebujesz także co najmniej dwóch dodatkowych nieużywanych podsieci do przyszłej rozbudowy sieci._

**Dwie pozostałe nieużywane podsieci można utworzyć, używając adresów 192.168.0.128/26 i 192.168.0.192/26. Każda z tych podsieci będzie miała 62 dostępne adresy IP, z czego 2 będą zarezerwowane dla adresu sieci i adresu rozgłoszeniowego.**

W ten sposób wszystkie sieci będą miały tą samą długości i jednocześnie będą spełniały wszystkie warunki.

_d. Odpowiedz na poniższe pytania, aby pomóc stworzyć schemat tworzenia podsieci, który spełnia określone wymagania sieci:_

_Jaka ilość adresów użytecznych jest potrzebna w największej wymaganej podsieci?_

**50**

_Jaka jest wymagana minimalna ilość podsieci?_

**Ze względu na polecenie będziemy potrzebować 4 podsieci, gdyż dwie mamy zdefiniowane już teraz i będziemy potrzebować dwóch kolejnych w przypadku przyszłego rozwoju.**

_Sieć, której należy użyć do podziału na podsieci to 192.168.0.0/24. Jaka jest reprezentacja maski /24 w systemie binarnym?_

**1111111.11111111.11111111.00000000**

_e. Maska podsieci składa się z dwóch części. Części sieciowej oraz części hosta. Podział ten jest reprezentowany w masce w postaci binarnej przez bity o wartości 1 oraz zero._

_Co reprezentują bity o wartości jeden w masce podsieci?_

**Reprezentują one część sieciową**

_Co reprezentują bity o wartości zero w masce podsieci?_

**Reprezentują one część hosta**

_f. Podział sieci polega na tym, że bity z części hosta oryginalnej sieci zamieniane są na bity części sieciowej. Liczba bitów podsieci określa liczbę podsieci._

_Biorąc pod uwagę każdą z możliwych masek podsieci przedstawionych w formacie binarnym, określ ile podsieci i z jaką ilością hostów zostanie utworzonych w każdym przykładzie?_

_1) (/25) 11111111.11111111.11111111.10000000_

_Odpowiednik maski podsieci dziesiętnie : _

**255.255.255.128**

_Liczba podsieci? Liczba hostów?_

**2(2^1) podsieci i 128(2^7) hostow więc**

**(2^7) -2 = 126 hostow na podsieć**

_2) (/26) 11111111.11111111.11111111.11000000_

_Odpowiednik maski podsieci dziesiętnie :_

**255.255.255.192**

_Liczba podsieci? Liczba hostów?_

**4(2^2) podsieci i 64(2^6) hostow więc**

**(2^6) -2 = 62 hostow na podsieć**

_3) (/27) 11111111.11111111.11111111.11100000_

_Odpowiednik maski podsieci dziesiętnie :_

**255.255.255.224**

_Liczba podsieci? Liczba hostów?_

**8(2^3) podsieci i 32(2^5) hostow więc**

**(2^5) -2 = 30 hostow na podsieć**

_4) (/28) 11111111.11111111.11111111.11110000_

_Odpowiednik maski podsieci dziesiętnie :_

**255.255.255.240**

_Liczba podsieci? Liczba hostów?_

**16(2^4) podsieci i 16(2^4) hostow więc**

**(2^4) -2 = 14 hostow na podsieć**

_5) (/29) 11111111.11111111.11111111.11111000_

_Odpowiednik maski podsieci dziesiętnie :_

**255.255.255.248**

_Liczba podsieci? Liczba hostów?_

**32(2^5) podsieci i 8(2^3) hostow więc**

**(2^3) -2 = 6 hostow na podsieć**

_6) (/30) 11111111.11111111.11111111.11111100_

_Odpowiednik maski podsieci dziesiętnie :_

**255.255.255.252**

_Liczba podsieci? Liczba hostów?_

**64(2^6) podsieci i 4(2^2) hostow więc**

**(2^2) -2 = 2 hostow na podsieć**

_Biorąc pod uwagę swoje powyższe odpowiedzi, wybierz maski podsieci, które spełniają wymaganą liczbę minimalnych adresów hostów?_

**Maski: 25, 26**

_Biorąc pod uwagę swoje powyższe odpowiedzi, wybierz maski podsieci, które spełniają wymaganą minimalną liczbę podsieci?_

**Maski: 26, 27, 28, 29, 30**

_Biorąc pod uwagę powyższe odpowiedzi, która maska podsieci spełnia zarówno wymaganą minimalną liczbę hostów, jak i minimalną wymaganą liczbę podsieci?_

**Maska: 26, dzięki niej otrzymamy 62 hostow na sieć co pasuje nam perfekcyjnie do wymogów z początku zadania**

_Po ustaleniu, która maska podsieci spełnia wszystkie podane wymagania sieciowe, należy wyprowadzić każdą z podsieci. Wypisz podsieci od pierwszej do ostatniej w tabeli. Pamiętaj, że pierwszą podsiecią jest 192.168.0.0 z wybraną maską podsieci._

| Adres podsieci | Prefiks | Maska podsieci  |
| -------------- | ------- | --------------- |
| 192.168.0.0    | /26     | 255.255.255.192 |
| 192.168.0.64   | /26     | 255.255.255.192 |
| 192.168.0.128  | /26     | 255.255.255.192 |
| 192.168.0.192  | /26     | 255.255.255.192 |

### Krok 2: Wypełnij brakujące adresy IP w tabeli

| Urządzenie      | Interfejs      | Adres IP        | Maska podsieci  | Brama domyślna  |
| --------------- | -------------- | --------------- | --------------- | --------------- |
| Customer Router | G0/0           | 192.168.0.1     | 255.255.255.192 | ND              |
|                 | G0/1           | 192.168.0.65    | 255.255.255.192 | ND              |
|                 | S0/1/0         | 209.165.201.2   | 255.255.255.252 | ND              |
| LAN-A Switch    | VLAN1          | 192.168.0.2     | 255.255.255.192 | 192.168.0.1     |
| LAN-B Switch    | VLAN1          | 192.168.0.66    | 255.255.255.192 | 192.168.0.65    |
| PC-A            | karta sieciowa | 192.168.0.62    | 255.255.255.192 | 192.168.0.1     |
| PC-B            | karta sieciowa | 192.168.0.126   | 255.255.255.192 | 192.168.0.65    |
| ISPRouter       | G0/0           | 209.165.200.225 | 255.255.255.224 | ND              |
|                 | S0/1/0         | 209.165.201.1   | 255.255.255.252 | ND              |
| ISPSwitch       | VLAN1          | 209.165.200.226 | 255.255.255.224 | 209.165.200.225 |
| ISP Workstation | karta sieciowa | 209.165.200.235 | 255.255.255.224 | 209.165.200.255 |
| ISP Server      | karta sieciowa | 209.165.200.240 | 255.255.255.224 | 209.165.200.255 |

## Część 2: Skonfiguruj urządzenia

### Krok 1 Skonfiguruj CustomerRouter.

```s
enable
configure terminal
hostname CustomerRouter
enable secret Class123
line con 0
password Cisco123
login
interface GigabitEthernet0/0
ip address 192.168.0.1 255.255.255.192
no shutdown
interface GigabitEthernet0/1
ip address 192.168.0.65 255.255.255.192
no shutdown
interface Serial0/1/0
ip address 209.165.201.2 255.255.255.252
no shutdown
end
```

<div style="page-break-after: always;"></div>

### Krok 2: Skonfiguruj dwa przełączniki LAN klienta.

```s
enable
configure terminal
interface Vlan1
ip address 192.168.0.2 255.255.255.192
no shutdown
ip default-gateway 192.168.0.1
end
```

```s
enable
configure terminal
interface Vlan1
ip address 192.168.0.66 255.255.255.192
no shutdown
ip default-gateway 192.168.0.65
end
```

### Krok 3: Skonfiguruj interfejsy komputerów PC.

Ustawiamy adresy według wypełnionej wcześniej tabeli.

## Część 3: Przetestuj działanie sieci

Ping bramy domyślnej PC A:

```s
C:\>ping 192.168.0.1

Pinging 192.168.0.1 with 32 bytes of data:

Reply from 192.168.0.1: bytes=32 time<1ms TTL=255
Reply from 192.168.0.1: bytes=32 time<1ms TTL=255
Reply from 192.168.0.1: bytes=32 time<1ms TTL=255
Reply from 192.168.0.1: bytes=32 time<1ms TTL=255

Ping statistics for 192.168.0.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

<div style="page-break-after: always;"></div>

Ping bramy domyślnej PC B:

```s
C:\>ping 192.168.0.65

Pinging 192.168.0.65 with 32 bytes of data:

Reply from 192.168.0.65: bytes=32 time<1ms TTL=255
Reply from 192.168.0.65: bytes=32 time<1ms TTL=255
Reply from 192.168.0.65: bytes=32 time<3ms TTL=255
Reply from 192.168.0.65: bytes=32 time<3ms TTL=255

Ping statistics for 192.168.0.65:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 4ms, Average = 1ms
```

Ping komputera B z komputera A:

```s
C:\>ping 192.168.0.126

Pinging 192.168.0.126 with 32 bytes of data:

Reply from 192.168.0.126: bytes=32 time<1ms TTL=127
Reply from 192.168.0.126: bytes=32 time<3ms TTL=127
Reply from 192.168.0.126: bytes=32 time<48ms TTL=127
Reply from 192.168.0.126: bytes=32 time<23ms TTL=127

Ping statistics for 192.168.0.126:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 48ms, Average = 18ms
```
