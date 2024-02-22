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
            <Rtext>25.05.2023</Rtext>
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
        <Rtext>13</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Projektowanie i stosowanie adresacji VLSM

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

| Urządzenie | Interfejs | Adres IP   | Maska podsieci  | Brama domyślna |
| ---------- | --------- | ---------- | --------------- | -------------- |
| East       | G0/0      | 10.1.1.97  | 255.255.255.240 | ND             |
|            | G0/1      | 10.1.1.65  | 255.255.255.224 | ND             |
|            | S0/0/0    | 10.1.1.121 | 255.255.255.252 | ND             |
| West       | G0/0      | 10.1.1.113 | 255.255.255.248 | ND             |
|            | G0/1      | 10.1.1.1   | 255.255.255.192 | ND             |
|            | S0/0/0    | 10.1.1.122 | 255.255.255.252 | ND             |
| ES-1       | VLAN1     | 10.1.1.98  | 255.255.255.240 | 10.1.1.97      |
| ES-2       | VLAN1     | 10.1.1.66  | 255.255.255.224 | 10.1.1.65      |
| WS-1       | VLAN1     | 10.1.1.114 | 255.255.255.248 | 10.1.1.113     |
| WS-2       | VLAN1     | 10.1.1.2   | 255.255.255.192 | 10.1.1.1       |
| PC E1-22   | NIC       | 10.1.1.110 | 255.255.255.240 | 10.1.1.97      |
| PC E2-47   | NIC       | 10.1.1.94  | 255.255.255.224 | 10.1.1.65      |
| PC W1-201  | NIC       | 10.1.1.118 | 255.255.255.248 | 10.1.1.113     |
| PC W2-87   | NIC       | 10.1.1.62  | 255.255.255.192 | 10.1.1.1       |

&nbsp;

&nbsp;

&nbsp;

| Opis podsieci | Ilość wymaganych hostów | Adres sieci/CIDR | Pierwszy użyteczny adres hosta | Adres rozgłoszeniowy |
| ------------- | ----------------------- | ---------------- | ------------------------------ | -------------------- |
| WS-2 LAN      | 47                      | 10.1.1.0/26      | 10.1.1.1                       | 10.1.1.63            |
| ES-2 LAN      | 28                      | 10.1.1.64/27     | 10.1.1.65                      | 10.1.1.95            |
| ES-1 LAN      | 11                      | 10.1.48.96/28    | 10.1.1.97                      | 10.1.1.111           |
| WS-1 LAN      | 5                       | 10.1.48.112/29   | 10.1.1.113                     | 10.1.1.119           |
| WAN Link      | 2                       | 10.1.48.120/30   | 10.1.1.121                     | 10.1.1.123           |

<div style="page-break-after: always;"></div>

### East Config

```bash
East>en
East#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
East(config)#int g0/0
East(config-if)#ip add 10.1.1.97 255.255.255.240
East(config-if)#no shut

East(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up

East(config-if)#int g0/1
East(config-if)#ip add 10.1.1.65 255.255.255.224
East(config-if)#no shut

East(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

East(config-if)#int s0/0/0
East(config-if)#ip add 10.1.1.121 255.255.255.252
East(config-if)#no shut

%LINK-5-CHANGED: Interface Serial0/0/0, changed state to down
```

### West Config

```bash
West>en
West#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
West(config)#int g0/0
West(config-if)#ip add 10.1.1.113 255.255.255.248
West(config-if)#no shut

West(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up

West(config-if)#int g0/1
West(config-if)#ip add 10.1.1.1 255.255.255.192
West(config-if)#no shut

West(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

West(config-if)#int s0/0/0
West(config-if)#ip add 10.1.1.122 255.255.255.252
West(config-if)#no shut

%LINK-5-CHANGED: Interface Serial0/0/0, changed state to down
```

### ES-1 Config

```bash
ES-1>en
ES-1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
ES-1(config)#int vlan 1
ES-1(config-if)#ip add 10.1.1.98 255.255.255.240
ES-1(config-if)#no shut

ES-1(config-if)#
%LINK-5-CHANGED: Interface Vlan1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
ip def 10.1.1.97
```

### ES-2 Config

```bash
ES-2>en
ES-2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
ES-2(config)#int vlan 1
ES-2(config-if)#ip add 10.1.1.66 255.255.255.224
ES-2(config-if)#no shut

ES-2(config-if)#
%LINK-5-CHANGED: Interface Vlan1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
ip def 10.1.1.65
```

<div style="page-break-after: always;"></div>

### WS-1 Config

```bash
WS-1>en
WS-1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
WS-1(config)#int vlan 1
WS-1(config-if)#ip add 10.1.1.114 255.255.255.248
WS-1(config-if)#no shut

WS-1(config-if)#
%LINK-5-CHANGED: Interface Vlan1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
ip def 10.1.1.113
```

### WS-2 Config

```bash
WS-2>en
WS-2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
WS-2(config)#int vlan 1
WS-2(config-if)#ip add 10.1.1.2 255.255.255.192
WS-2(config-if)#no shut

WS-2(config-if)#
%LINK-5-CHANGED: Interface Vlan1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
ip def 10.1.1.1
```
