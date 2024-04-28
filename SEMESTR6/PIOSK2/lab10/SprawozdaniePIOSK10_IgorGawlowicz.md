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
            <Rtext>27.04.2023</Rtext>
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
        <Rtext>10</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguracja PAT

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Konfiguracja PAT

### Część 1: Konfiguracja dynamicznego NAT z przeciążeniem

#### Krok 1: Konfiguracja dozwolonego ruchu.

Na R1, skonfiguruj standardową listę ACL 1 zezwalającą na ruch dla adresów należących do przestrzeni 172.16.0.0/16.

```bash
R1(config)# access-list 1 permit 172.16.0.0 0.0.255.255
```

#### Krok 2: Konfiguracja puli adresów NAT.

Skonfiguruj router R1 z pulą NAT, która używa dwóch użytecznych adresów w przestrzeni adresowej 209.165.200.232/30.

```bash
R1(config)# ip nat pool ANY_POOL_NAME 209.165.200.233 209.165.200.234 netmask 255.255.255.252
```

#### Krok 3: Skojarz listę ACL 1 z pulą NAT i zezwól na ponowne wykorzystanie adresów.

```bash
R1(config)# ip nat inside source list 1 pool ANY_POOL_NAME overload
```

#### Krok 4: Konfiguracja interfejsów NAT.

Stosując właściwe polecenia NAT skonfiguruj interfejsy R1 oznaczając je, jako połączone do wewnątrz i połączone na zewnątrz.

```bash
R1(config)# interface s0/1/0
R1(config-if)# ip nat outside
R1(config-if)# interface g0/0/0
R1(config-if)# ip nat inside
R1(config-if)# interface g0/0/1
R1(config-if)# ip nat inside
```

### Część 2: Weryfikacja dynamicznego NAT z implementacją przeciążenia

#### Krok 1: Uzyskaj dostęp do usług przez Internet.

Z przeglądarki internetowej każdego z komputerów PC, które używają R1 jako swojej bramy (PC1, L1, PC2 i L2), przejdź do strony www na Server1.

_Czy wszystkie połączenia były udane?_

`Tak`

#### Krok 2: Wyświetl translacje NAT.

Wyświetl odwzorowania NAT na R1.

```bash
R1# show ip nat translations
```

Zauważ, że wszystkie cztery urządzenia były w stanie się komunikować i używają tylko jednego adresu z puli. PAT będzie nadal używać tego samego adresu, dopóki nie skończą się numery portów w celu skojarzenia z tłumaczeniem. Gdy to nastąpi, zostanie użyty następny adres w puli. Chociaż teoretyczna granica wyniosłaby 65 536, ponieważ pole numeru portu jest liczbą 16-bitową, urządzenie prawdopodobnie zabraknie pamięci przed osiągnięciem tego limitu.

### Część 3: Konfigurowanie PAT przy użyciu interfejsu

#### Krok 1: Konfiguracja dozwolonego ruchu.

Na R2, skonfiguruj standardową listę ACL 1 zezwalającą na ruch dla adresów należących do przestrzeni 172.17.0.0/16.

#### Krok 2: Skojarz listę ACL 2 z interfejsem NAT i zezwól na ponowne wykorzystanie adresów.

Wprowadź instrukcję NAT na R2, aby korzystać z interfejsu podłączonego do Internetu i zapewnić tłumaczenia dla wszystkich urządzeń wewnętrznych.

```bash
R2(config)# ip nat inside source list 2 interface s0/1/1 overload
```

#### Krok 3: Konfiguracja interfejsów NAT.

Stosując właściwe polecenia NAT skonfiguruj interfejsy R2 oznaczając je, jako połączone do wewnątrz i połączone na zewnątrz.

```bash
R2(config)# interface s0/1/1
R2(config-if)# ip nat outside
R2(config-if)# interface g0/0/0
R2(config-if)# ip nat inside
R2(config-if)# interface g0/0/1
R2(config-if)# ip nat inside
```

### Część 4: Weryfikacja implementacji NAT na interfejsie

#### Krok 1: Uzyskaj dostęp do usług przez Internet.

Z przeglądarki internetowej każdego z komputerów PC, które używają R2 jako swojej bramy (PC3, L3, PC4 i L4), przejdź do strony www na Server1.

Czy wszystkie połączenia były udane?

`Tak`

#### Krok 2: Wyświetl translacje NAT.

Wyświetl odwzorowania NAT na R2.

R2

```bash
R2#show ip nat translations
```

#### Krok 3: Porównaj statystyki NAT na R1 i R2.

Porównaj statystyki NAT na obu urządzeniach.

R1

```bash
R1#show ip nat statistics
Total translations: 0 (0 static, 0 dynamic, 0 extended)
Outside Interfaces: Serial0/1/0
Inside Interfaces: GigabitEthernet0/0/0 , GigabitEthernet0/0/1
Hits: 0  Misses: 0
Expired translations: 0
Dynamic mappings:
-- Inside Source
access-list 1 pool DYNAMIC refCount 0
 pool DYNAMIC: netmask 255.255.255.252
       start 209.165.200.233 end 209.165.200.234
       type generic, total addresses 2 , allocated 0 (0%), misses 0
```

R2

```bash
R2#show ip nat statistics
Total translations: 0 (0 static, 0 dynamic, 0 extended)
Outside Interfaces: Serial0/1/1
Inside Interfaces: GigabitEthernet0/0/0 , GigabitEthernet0/0/1
Hits: 0  Misses: 0
Expired translations: 0
Dynamic mappings:
```

_Dlaczego R2 nie zawiera żadnych mapowań dynamicznych?_

`R1 zawiera dynamiczne odwzorowania dla puli adresów, która została skonfigurowana. R2 używa tylko interfejsu zewnętrznego jako adresu do przekładu adresów wewnętrznych, więc nie ma żadnych dynamicznych odwzorowań`
