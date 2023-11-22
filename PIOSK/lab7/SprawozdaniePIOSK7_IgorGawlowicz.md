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
            <Rtext>22.11.2023</Rtext>
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
        <Rtext>7</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Routing między sieciami VLAN - wyzwanie

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Routing między sieciami VLAN - wyzwanie

To ćwiczenie umożliwia prezentację oraz doskonalenie Twoich umiejętności dotyczących implementowania routingu między sieciami VAN z uwzględnieniem konfiguracji adresacji IP, konfiguracji sieci VLAN, tworzenia magistral (łączy typu trunk) i podinterfejsów.

Tabela adresowania

| Device | Interface | IP Address   | Subnet Mask     | Default Gateway |
|--------|-----------|--------------|-----------------|-----------------|
| R1     | G0/0      | 172.17.25.2  | 255.255.255.252 | N/A             |
| R1     | G0/1.10   | 172.17.10.1  | 255.255.255.0   |                 |
| R1     | G0/1.20   | 172.17.20.1  | 255.255.255.0   |                 |
| R1     | G0/1.30   | 172.17.30.1  | 255.255.255.0   |                 |
| R1     | G0/1.88   | 172.17.88.1  | 255.255.255.0   |                 |
| R1     | G0/1.99   | 172.17.99.1  | 255.255.255.0   |                 |
| S1     | VLAN 99   | 172.17.99.10 | 255.255.255.0   | 172.17.99.1     |
| PC1    | karta sieciowa       | 172.17.10.21 | 255.255.255.0   | 172.17.10.1     |
| PC2    | karta sieciowa       | 172.17.20.22 | 255.255.255.0   | 172.17.20.1     |
| PC3    | karta sieciowa       | 172.17.30.23 | 255.255.255.0   | 172.17.30.1     |
| Server | karta sieciowa       | 172.17.50.254| 255.255.255.0   | 172.17.50.1     |

Tabela sieci VLAN i przypisania portów do VLAN

| VLAN | Name            | Interface |
|------|-----------------|-----------|
| 10   | Faculty/Staff   | F0/11-17  |
| 20   | Students        | F0/18-24  |
| 30   | Guest(Default)  | F0/6-10   |
| 88   | Native          | G0/1      |
| 99   | Management      | VLAN 99   |

## instrukcje

Skonfiguruj urządzenia tak, aby spełniały następujące wymagania:

- Na podstawie tabeli adresacji skonfiguruj adresy na R1 oraz S1

R1
```cmd
R1(config)#interface GigabitEthernet0/0
R1(config-if)#no shutdown

R1(config-if)#interface GigabitEthernet0/1.10
R1(config-subif)#encapsulation dot1Q 10
R1(config-subif)#ip address 172.17.10.1 255.255.255.0

R1(config-subif)#interface GigabitEthernet0/1.20
R1(config-subif)#encapsulation dot1Q 20
R1(config-subif)#ip address 172.17.20.1 255.255.255.0

R1(config-subif)#interface GigabitEthernet0/1.30
R1(config-subif)#encapsulation dot1Q 30
R1(config-subif)#ip address 172.17.30.1 255.255.255.0

R1(config-subif)#interface GigabitEthernet0/1.88
R1(config-subif)#encapsulation dot1Q 88 native
R1(config-subif)#ip address 172.17.88.1 255.255.255.0

R1(config-subif)#interface GigabitEthernet0/1.99
R1(config-subif)#encapsulation dot1Q 99
R1(config-subif)#ip address 172.17.99.1 255.255.255.0

R1(config-subif)#end
```

S1
```cmd
S1>enable
S1#config
Configuring from terminal, memory, or network [terminal]? 
Enter configuration commands, one per line.  End with CNTL/Z.

S1(config)#interface vlan 99
S1(config-if)#ip address 172.17.99.10 255.255.255.0
S1(config-if)#no shutdown
```

- Skonfiguruj bramę domyślną na S1.

```cmd
S1(config)#ip default-gateway 172.17.99.1
```

Zgodnie z tabelą sieci VLAN i przypisania portów do VLAN na przełączniku S1 stwórz i nazwij sieci VLAN oraz przypisz do nich porty. Porty powinny pracować w trybie dostępowym. Nazwy VLAN powinny dokładnie pasować do nazw w tabeli.

```cmd
S1(config)#vlan 10
S1(config-vlan)#name Faculty/Staff

S1(config-vlan)#vlan 20
S1(config-vlan)#name Students

S1(config-vlan)#vlan 30
S1(config-vlan)#name Guest(Default)

S1(config-vlan)#vlan 88
S1(config-vlan)#name Native

S1(config-vlan)#vlan 99
S1(config-vlan)#
%LINK-5-CHANGED: Interface Vlan99, changed state to up

S1(config-vlan)#name Management

S1(config-vlan)#interface range f0/11 - 17
S1(config-if-range)#switchport mode access
S1(config-if-range)#switchport access vlan 10

S1(config-if-range)#interface range f0/18 - 24
S1(config-if-range)#switchport mode access 
S1(config-if-range)#switchport access vlan 20

S1(config-if-range)#interface range f0/6 - 10
S1(config-if-range)#switchport mode access
S1(config-if-range)#switchport access vlan 30
```

- Skonfiguruj G0/1 na S1 jako statyczny trunk i przypisz natywną sieć VLAN.

```cmd
S1(config)#interface g0/1
S1(config-if)#switchport mode trunk
S1(config-if)#switchport trunk native vlan 88
```

Wszystkie porty nie przypisane do żadnej sieci VLAN powinny być wyłączone.

```cmd
S1(config)#interface range f0/1-5,g0/2
S1(config-if-range)#shutdown

%LINK-5-CHANGED: Interface FastEthernet0/1, changed state to administratively down

%LINK-5-CHANGED: Interface FastEthernet0/2, changed state to administratively down

%LINK-5-CHANGED: Interface FastEthernet0/3, changed state to administratively down

%LINK-5-CHANGED: Interface FastEthernet0/4, changed state to administratively down

%LINK-5-CHANGED: Interface FastEthernet0/5, changed state to administratively down

%LINK-5-CHANGED: Interface GigabitEthernet0/2, changed state to administratively down
```

- W oparciu o tablicę adresacji skonfiguruj na routerze R1 routing między sieciami VLAN.

Możemy teraz sprawdzić i zobaczymy że połączenie pomiędzy routerem, switchem oraz wszystkimi komputerami powodzi się.

## Wnioski

 Ćwiczenie to pozwala zrozumieć i zaimplementować różne aspekty konfiguracji sieci VLAN, adresacji IP, trunków oraz routingu między sieciami. Jest to kluczowy krok dla zapewnienia efektywnej komunikacji w środowiskach sieciowych, zwłaszcza w większych sieciach, gdzie segmentacja sieci i kontrola ruchu są istotne.