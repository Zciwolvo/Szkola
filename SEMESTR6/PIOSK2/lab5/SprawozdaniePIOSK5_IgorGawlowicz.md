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
            <Rtext>04.04.2023</Rtext>
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
        <Rtext>4</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguracja jednoobszarowego OSPFv2 punkt-punkt

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Packet Tracer - Konfiguracja jednoobszarowego OSPFv2 punkt-punkt

_Pomagasz inżynierowi sieciowemu przetestować protokół OSPF, budując sieć w laboratorium, w którym pracujesz. Połączyłeś urządzenia i skonfigurowałeś interfejsy oraz masz łączność w lokalnych sieciach LAN. Twoim zadaniem jest ukończenie konfiguracji OSPF zgodnie z wymaganiami pozostawionymi przez inżyniera._

_Użyj dostarczonych informacji i listy wymagań, aby skonfigurować sieć testową. Po pomyślnym zakończeniu zadania pingi z wszystkich hostów do serwera internetowego powinny zakończyć się sukcesem._

Zaczniemy od aktywacji OSPF na każdym z routerów według tablicy adresacji w sekcji `Headquarters`

```bash
P2P-1(config)#router ospf 10
P2P-1(config-router)#network 10.0.0.0 0.0.0.3 area 0
P2P-1(config-router)#network 10.0.0.8 0.0.0.3 area 0
P2P-1(config-router)#network 10.0.0.12 0.0.0.3 area 0
```

```bash
P2P-2(config)#router ospf 10
P2P-2(config-router)#network 10.0.0.0 0.0.0.3 area 0
P2P-2(config-router)#network 10.0.0.4 0.0.0.3 area 0
P2P-2(config-router)#network 192.168.1.0 0.0.0.255 area 0
P2P-2(config-router)#network 192.168.2.0 0.0.0.255 area 0
```

```bash
P2P-3(config)#router ospf 10
P2P-3(config-router)#network 10.0.0.4 0.0.0.3 area 0
P2P-3(config-router)#network 10.0.0.8 0.0.0.3 area 0
P2P-3(config-router)#network 192.168.3.0 0.0.0.15 area 0
```

Następnie będziemy aktywować OSPF w sekcji `Data Services`

```bash
BC-1(config)#interface GigabitEthernet0/0/0
BC-1(config-if)#ip ospf 10 area 0

BC-1(config-if)#interface Serial0/1/0
BC-1(config-if)#ip ospf 10 area 0
```

```bash
BC-2(config)#interface GigabitEthernet0/0/0
BC-2(config-if)#ip ospf 10 area 0

BC-2(config-if)#interface GigabitEthernet0/0/1
BC-2(config-if)#ip ospf 10 area 0
```

```bash
BC-3(config)#interface GigabitEthernet0/0/0
BC-3(config-if)#ip ospf 10 area 0

BC-3(config-if)#interface GigabitEthernet0/0/1
BC-3(config-if)#ip ospf 10 area 0
```

Teraz skonfigurujemy identyfikatory routerów

```bash
BC-1(config)#router ospf 10
BC-1(config-router)#router-id 6.6.6.6
```

```bash
BC-2(config)#router ospf 10
BC-2(config-router)#router-id 5.5.5.5
```

```bash
BC-3(config)#router ospf 10
BC-3(config-router)#router-id 4.4.4.4
```

Teraz dokonamy konfiguracji OSPFa na każdym z routerów

```bash
P2P-2(config)#router ospf 10
P2P-2(config-router)#passive-interface GigabitEthernet0/0/0
P2P-2(config-router)#passive-interface GigabitEthernet0/0/1
```

```bash
P2P-3(config)#router ospf 10
P2P-3(config-router)#passive-interface GigabitEthernet0/0/0
```

```bash
BC-1(config)#router ospf 10
BC-1(config-router)#passive-interface Serial0/1/1
```

```bash
BC-2(config)#router ospf 10
BC-2(config-router)#passive-interface GigabitEthernet0/0/0
```

```bash
BC-3(config)#router ospf 10
BC-3(config-router)#passive-interface GigabitEthernet0/0/0
```

Skonfiguruj router BC-1 z najwyższym priorytetem interfejsu OSPF, tak aby zawsze był routerem DR sieci wielodostępowej.

```bash
BC-1(config)#interface GigabitEthernet0/0/0
BC-1(config-if)#ip ospf priority 255
```

Skonfiguruj domyślną trasę do chmury ISP, używając jako argumentu polecenia interfejsu wyjścia.

```bash
BC-1(config)#ip route 0.0.0.0 0.0.0.0 Serial0/1/1
```

Automatycznie propaguj trasę domyślną do wszystkich routerów w sieci.

```bash
BC-1(config)#router ospf 10
BC-1(config-router)#default-information originate
```

Skonfiguruj routery OSPF tak, aby koszt interfejsu Gigabit Ethernet wynosił 10, a koszt Fast Ethernet wynosił 100.

```bash
P2P-1(config)#router ospf 10
P2P-1(config-router)#auto-cost reference-bandwidth 1000
```

```bash
P2P-2(config)#router ospf 10
P2P-2(config-router)#auto-cost reference-bandwidth 1000
```

```bash
P2P-3(config)#router ospf 10
P2P-3(config-router)#auto-cost reference-bandwidth 1000
```

```bash
BC-1(config)#router ospf 10
BC-1(config-router)#auto-cost reference-bandwidth 1000
```

```bash
BC-2(config)#router ospf 10
BC-2(config-router)#auto-cost reference-bandwidth 1000
```

```bash
BC-3(config)#router ospf 10
BC-3(config-router)#auto-cost reference-bandwidth 1000
```

Skonfiguruj wartość kosztu OSPF interfejsu P2P-1 Serial0/1/1 równą 50.

```bash
P2P-1(config)#interface Serial0/1/1
P2P-1(config-if)#ip ospf cost 50
```

Skonfiguruj wartości interwału hello i dead na interfejsach łączących P2P-1 i BC-1, aby były dwukrotnie wyższe od wartości domyślnych.

```bash
P2P-1(config)#interface Serial0/2/0
P2P-1(config-if)#ip ospf hello-interval 20
P2P-1(config-if)#ip ospf dead-interval 80
```

```bash
BC-1(config)#interface Serial0/1/0
BC-1(config-if)#ip ospf hello-interval 20
BC-1(config-if)#ip ospf dead-interval 80
```
