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
<h1>LABORATORIUM PROJEKTOWANIE I OBSŁUGA SIECI KOMPUTEROWYCH II</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>19.03.2023</Rtext>
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
            <Rtext>6</Rtext>
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
        <Rtext>3</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Modyfikowanie jednoobszarowego OSPFv2 / Propagowanie trasy domyślnej w OSPFv2

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Modyfikowanie jednoobszarowego OSPFv2

_W tym ćwiczeniu protokół OSPF został już skonfigurowany i wszystkie urządzenia końcowe mają ze sobą pełną łączność. Zmodyfikujesz domyślne konfiguracje routingu OSPF, zmieniając interwały Hello i Dead oraz dostosowując szerokość pasma łącza. Następnie sprawdzisz czy łączność w sieci została przywrócona dla wszystkich urządzeń._

## Część 1: Modyfikowanie ustawień domyślnych OSPF

### Krok 1: Przetestuj łączność między wszystkimi urządzeniami końcowymi.

Przed rozpoczęciem modyfikacji właściwości protokołu OSPF sprawdź, czy wszystkie komputery mają łączność ze sobą i serwerem WWW.

### Krok 2: Dopasuj interwały hello i dead pomiędzy routerami R1 i R2.

a. Wprowadź następujące polecenia na R1.

```bash
R1(config)# interface s0/0/0

R1(config-if)# ip ospf hello-interval 15

R1(config-if)# ip ospf dead-interval 60
```

b. Po krótkim czasie połączenie OSPF z R2 zakończy się niepowodzeniem, jak pokazano na wyjściu routera.

```bash
00:02:40: %OSPF-5-ADJCHG: Process 1, Nbr 209.165.200.225 on Serial0/0/0 from FULL to DOWN, Neighbor Down: Dead timer expired

00:02:40: %OSPF-5-ADJCHG: Process 1, Nbr 209.165.200.225 on Serial0/0/0 from FULL to DOWN, Neighbor Down: Interface down or detached
```

Obydwie strony na łączu muszą mieć ustawione takie same interwały w celu utrzymania przyległości. Zidentyfikuj interfejs na R2 podłączony do R1. Dostosuj interwały na interfejsie R2, aby pasowały do ustawień R1.

```bash
R2(config)# interface s0/0/0
R2(config-if)# ip ospf hello-interval 15
R2(config-if)# ip ospf dead-interval 60
```

Po krótkim czasie powinien zostać wyświetlony komunikat o stanie informujący o ponownym ustanowieniu przylegania OSPF.

```bash
00:21:52: %OSPF-5-ADJCHG: Process 1, Nbr 192.168.10.5 on Serial0/0/0 from LOADING to FULL, Loading Done
```

### Krok 3: Dopasuj ustawienia szerokości pasma na R1.

a. Prześledź trasę pomiędzy komputerem PC1 i serwerem WWW o adresie 64.100.1.2. Zauważ, że trasa od PC1 do serwera WWW jest routowana przez R2. OSPF preferuje trasy z najniższym kosztem.

```bash
C:\> tracert 64.100.1.2

Tracing route to 64.100.1.2 over a maximum of 30 hops:

1 1 ms 0 ms 8 ms 172.16.1.1

2 0 ms 1 ms 0 ms 172.16.3.2

3 1 ms 9 ms 2 ms 209.165.200.226

4 \* 1 ms 0 ms 64.100.1.2

Trace complete.
```

b. Na interfejsie S0/0/0 routera R1 ustaw szerokość pasma na 64 kb/s. Nie zmieni to aktualnej szybkości transmisji na porcie R1; wartość ta będzie używana tylko do wyliczenia metryki OSPF i wyznaczenia najlepszej trasy.

```bash
R1(config-if)# bandwidth 64
```

c. Prześledź trasę pomiędzy komputerem PC1 i serwerem WWW o adresie 64.100.1.2. Zauważ, że trasa od PC1 do serwera WWW jest routowana teraz przez R3. OSPF preferuje trasy z najniższym kosztem.

```bash
C:\> tracert 64.100.1.2

Tracing route to 64.100.1.2 over a maximum of 30 hops:

1 1 ms 0 ms 3 ms 172.16.1.1

2 8 ms 1 ms 1 ms 192.168.10.6

3 2 ms 0 ms 2 ms 172.16.3.2

4 2 ms 3 ms 1 ms 209.165.200.226

5 2 ms 11 ms 11 ms 64.100.1.2

Trace complete.
```

## Część 2: Weryfikacja połączeń

Sprawdź, czy wszystkie komputery mają łączność ze sobą i serwerem WWW.

`Testy pomiędzy urządzeniami przechodzą poprawnie`

## Packet Tracer - Propagowanie trasy domyślnej w OSPFv2

_W tym ćwiczeniu skonfigurujesz trasę domyślną IPv4 do sieci Internet i roześlesz tę trasę do pozostałych routerów OSPF. Następnie sprawdzisz, czy trasa domyślna znajduje się tablicach routingu oraz czy komputery mogą już komunikować się z serwerem WWW znajdującym się w sieci Internet._

## Część 1: Propagowanie trasy domyślnej

### Krok 1: Testowanie łączności z serwerem sieci Web

a. Z PC1, PC2 i PC3 spróbuj wykonać polecenie ping do adresu IP serwera sieci Web, 64.100.1.2.

_Czy jakieś z przeprowadzonych testów zakończyły się sukcesem?_

`Nie, żaden z testów nie powiódł się `

Jaką wiadomość otrzymałeś i które urządzenie wydało wiadomość?

`"Destination unreachable" z R2.`

b. Sprawdź tablice routingu na routerach R1, R2 i R3.

_Jaki wpis znajduje się w tablicach routingu, który wskazuje, że ping do serwera sieci Web nie powiedzie się?_

`Gateway of last resort is not set`

### Krok 2: Skonfiguruj trasę domyślną na R2.

Skonfiguruj R2 z bezpośrednio dołączoną domyślną trasą do Internetu.

```bash
R2(config)# ip route 0.0.0.0 0.0.0.0 Serial0/1/0
```

Uwaga: Router wyświetli ostrzeżenie, że jeśli ten interfejs nie jest połączeniem typu punkt-punkt, może to mieć wpływ na wydajność. Ostrzeżenie to można zignorować, ponieważ jest to połączenie punkt-punkt.

Krok 3: Propagacja trasy w protokole OSPF.
Skonfiguruj protokół OSPF do propagowania trasy domyślnej w aktualizacjach routingu OSPF.

```bash
R2(config)# router ospf 1

R2(config-router)# default-information originate

Krok 4: Sprawdź tablice routingu na R1 i R3.
Wyświetl tablice routingu routerów R1 i R3 w celu sprawdzenia, czy trasa została rozgłoszona.

R1> show ip route

(wyniki pominięto)

Gateway of last resort is 172.16.3.2 to network 0.0.0.0

(wyniki pominięto)

O*E2 0.0.0.0/0 [110/1] via 172.16.3.2, 00:00:08, Serial0/0/0

!-------------------

R3> show ip route

(wyniki pominięto)

Gateway of last resort is 192.168.10.9 to network 0.0.0.0

(wyniki pominięto)

O*E2 0.0.0.0/0 [110/1] via 192.168.10.9, 00:08:15, Serial0/0/1

```

Część 2: Weryfikacja połączeń
_Sprawdź, czy PC1, PC2 i PC3 mogą komunikować się z serwerem WWW za pomocą polecenia ping._

Wszystkie testy połączenia powiodły się.
