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
            <Rtext>18.10.2023</Rtext>
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
        <Rtext>3</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguracja DTP

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Konfiguracja DTP

## Część 1: Weryfikacja konfiguracji sieci VLAN.

Pierwszym co chcemy zrobić jest zweryfikowanie obecnych sieci VLAN poprzez polecenie

`show vlan brief`

Musimy tutaj pamiętać o uprzednim włączeniu trybu uprzywilejowanego za pomocą `enable`

Po sprawdzeniu obecnych sieci dla S1, S2 i S3 możemy zauważyć, że na przełącznikach istnieją już 2 skonfigurowane sieci: 99 Management i 999 Native

## Część 2: Utworzenie dodatkowych sieci VLAN na S2 i S3.

Chcemy utworzyć nowe sieci VLAN na urządzeniach S2 i S3 zrobimy to w sposób następujący:

```cmd
S2#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 10
S2(config-vlan)#name Red
S2(config-vlan)#exit
S2(config)#vlan 20
S2(config-vlan)#name Blue
S2(config-vlan)#exit
S2(config)#vlan 30
S2(config-vlan)#name Yellow
```

Teraz po sprawdzeniu `show vlan brief` możemy zauważyć że pojawiły nam się nasze nowe sieci:

- 10 Red
- 20 Blue
- 30 Yellow

następnie powtórzymy taki sam proces dla S3.

## Część 3: Przypisywanie sieci VLAN do portów

Za pomocą poleceń `switchport mode acces` i `switchport access vlan {number}` przypiszemy nasze sieci vlan do odpowiednich portów dla S2 i S3.

S2

```cmd
S2(config)#interface range f0/1 - 8
S2(config-if-range)#switchport mode access
S2(config-if-range)#switchport access vlan 10
S2(config-if-range)#exit
S2(config)#interface range f0/9 - 16
S2(config-if-range)#switchport mode access
S2(config-if-range)#switchport access vlan 20
S2(config-if-range)#exit
S2(config)#interface range f0/17 -24
S2(config-if-range)#switchport mode access
S2(config-if-range)#switchport access vlan 30
```

S3

```cmd
S3(config)#interface range f0/1 - 8
S3(config-if-range)#switchport mode access
S3(config-if-range)#switchport access vlan 10
S3(config-if-range)#exit
S3(config)#interface range f0/9 - 16
S3(config-if-range)#switchport mode access
S3(config-if-range)#switchport access vlan 20
S3(config-if-range)#exit
S3(config)#interface range f0/17 - 24
S3(config-if-range)#switchport mode access
S3(config-if-range)#switchport access vlan 30
```

Teraz, gdy masz porty przypisane do sieci VLAN, spróbuj wykonać ping z PC1 do PC6.

_Czy test ping zakończył się sukcesem? Wyjaśnij._

Nie, ping nie powiódł się ponieważ porty pomiędzy switchami są we VLAN 1 a porty w PC1 i PC6 są we VLAN10.

## Część 4: Konfiguracja łączy trunk na S1, S2 i S3.

```cmd
S1>enable
S1#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#interface g0/1
S1(config-if)#switchport mode dynamic desirable

S1(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan99, changed state to up
```

_Jaki będzie wynik negocjacji między S1 i S2?_

Połączenie trunk zostało utworzone

Możemy teraz zauważyć że gdy sprawdzimy interfacy z poziomu S2

`Gig0/1      auto         n-802.1q       trunking      1`

W przypadku łącza trunk między S1 i S3 skonfiguruj interfejs GigabitEthernet 0/2 jako statyczne łącze trunk na S1. Ponadto wyłącz negocjacje DTP na interfejsie G0/2 na S1.

```cmd
S1(config)# interface g0/2
S1(config-if)# switchport mode trunk
S1(config-if)# switchport nonegotiate
```

```cmd
S1#show dtp
Global DTP information
    Sending DTP Hello packets every 30 seconds
    Dynamic Trunk timeout is 300 seconds
    2 interfaces using DTP
```

```cmd
S1#show interfaces trunk
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      desirable    n-802.1q       trunking      1
Gig0/2      on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gig0/1      1-1005
Gig0/2      1-1005

Port        Vlans allowed and active in management domain
Gig0/1      1,99,999
Gig0/2      1,99,999

Port        Vlans in spanning tree forwarding state and not pruned
Gig0/1      1,99,999
Gig0/2      1,99,999
```

_Jaka jest obecnie natywna sieć VLAN dla tych łączy?_

VLAN 1

Następnie skonfigurujemy VLAN 999 jako natywną sieć VLAN

Jakie wiadomości otrzymałeś na S1? Jak to można poprawić?

```cmd
S1(config-if-range)#%SPANTREE-2-RECV_PVID_ERR: Received BPDU with inconsistent peer vlan id 1 on GigabitEthernet0/1 VLAN999.

%SPANTREE-2-BLOCK_PVID_LOCAL: Blocking GigabitEthernet0/1 on VLAN0999. Inconsistent local vlan.
```

Aby naprawić ten komunikat musimy skonfigurować VLAN 999 także dla S2 i S3, zrobimy to w sposób identyczny do S1.

Teraz spradzimy czy połączenie zostało dobrze skonfigurowane:

```cmd
S1#ping 192.168.99.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.99.2, timeout is 2 seconds:
..!!!
Success rate is 60 percent (3/5), round-trip min/avg/max = 0/0/0 ms
```

Teraz możemy sprawdzić czy uda nam się spingować PC1 do PC6 i będziemy mogli zauważyć że dalej dochodzi do niepowodzenia. Jest to spowodowane błędną konfiguracją na S1, aby to naprawić musimy:

```cmd
S1#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 10
S1(config-vlan)#name Red
S1(config-vlan)#exit
S1(config)#vlan 20
S1(config-vlan)#name Blue
S1(config-vlan)#exit
S1(config)#vlan 30
S1(config-vlan)#name Yellow
```

Tym razem w końcu możemy zaobserwować sukces

Sprawdźmy teraz konfiguracje trunk na S3.

Po wpisaniu `show interface trunk` możemy zauważyć `Mode: on | Encapsulation: 802.1q`

Musimy więc skonfigurować G0/2 by pasowało do S1

```cmd
S3(config)#interface g0/2
S3(config-if)#switchport nonegotiate
```

Jednak `show interface trunk` nadal zwraca nam `Mode: on | Encapsulation: 802.1q`

Po sprawdzeniu `show interface G0/2 switchport` na S3 możemy zauważyć, że `Negotiation of Trunking: Off`

## Część 6: Sprawdzenie łączności od końca do końca.

Ping PC1 do PC6 > Sukces

Ping PC2 do PC5 > Sukces

Ping PC3 do PC4 > Sukces

# Pakiet Tracer - Wdrożenie sieci VLAN i łączy trunk

## Część 1: Konfiguracja sieci VLAN

Skonfigurujemy te same VLANy dla siecie A, B i C

```cmd
SWA>enable
SWA#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
SWA(config)#vlan 10
SWA(config-vlan)#name Admin
SWA(config-vlan)#vlan 20
SWA(config-vlan)#name Accounts
SWA(config-vlan)#vlan 30
SWA(config-vlan)#name HR
SWA(config-vlan)#vlan 40
SWA(config-vlan)#name Voice
SWA(config-vlan)#vlan 99
SWA(config-vlan)#name Management
SWA(config-vlan)#vlan 100
SWA(config-vlan)#name Native
```

## Część 2: Przypisywanie portów do sieci VLAN

Zaczniemy od konfiguracji w taki sam sposób SWB i SWC

```cmd
SWB(config)#interface f0/1
SWB(config-if)#switchport mode access
SWB(config-if)#switchport access vlan 10
SWB(config-if)#interface f0/2
SWB(config-if)#switchport mode access
SWB(config-if)#switchport access vlan 20
SWB(config-if)#interface f0/3
SWB(config-if)#switchport mode access
SWB(config-if)#switchport access vlan 30
```

Następnie skonfigurujemy VOICE dla SWC

```cmd
SWC(config-if)#interface f0/4
SWC(config-if)#switchport mode access
SWC(config-if)#switchport access vlan 10
SWC(config-if)#interface f0/4
SWC(config-if)#mls qos trust cos
SWC(config-if)#switchport voice vlan 40
```

Aby switche nie były w stanie się wzajemnie pingowac musimy dla każdego przeprowadzić taki ciąg operacji:

```cmd
SWA(config)#interface vlan 99
SWA(config-if)#
%LINK-5-CHANGED: Interface Vlan99, changed state to up

SWA(config-if)#ip address 192.168.99.252 255.255.255.0
SWA(config-if)#no shutdown
```

Z różnicą taką, że w adresie 4 oktet dla kolejnych to 253 i 254.

## Część 3: Konfiguracja statycznej magistrali trunk

Aby ustawić statyczną magistralę trunk musimy wpisać ciąg poleceń do SWA i SWB

```cmd
SWA(config)#interface g0/1
SWA(config-if)#switchport mode trunk

SWA(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan99, changed state to up

SWA(config-if)#switchport nonegotiate
SWA(config-if)#switchport trunk native vlan 100
```

## Część 4: Konfiguracja dynamicznej magistrali trunk

SWA

```cmd
SWA(config)#interface g0/2
SWA(config-if)#switchport mode dynamic desirable
```

SWC

```cmd
SWC(config)#interface g0/2
SWC(config-if)#switchport mode trunk
SWC(config-if)#switchport trunk native vlan 100
```

## Wnioski

W sprawozdaniu przeprowadziliśmy konfigurację sieci VLAN na przełącznikach S2 i S3 oraz przypisaliśmy porty do odpowiednich VLANów. Następnie skonfigurowaliśmy łącza trunk między przełącznikami S1, S2 i S3, zarówno w trybie statycznym, jak i dynamicznym, co umożliwiło skuteczną komunikację między nimi. Wprowadziliśmy także VLAN natywny na wszystkich przełącznikach i wyłączyliśmy negocjację DTP na jednym z łączy trunk. Po skonfigurowaniu wszystkich elementów sieci przetestowaliśmy łączność od końca do końca, co potwierdziło poprawność naszej konfiguracji. W trakcie sprawozdania zapoznaliśmy się z ważnymi aspektami związanymi z zarządzaniem sieciami, w tym tworzeniem i konfiguracją VLANów oraz łączami trunk, co ma istotne znaczenie dla prawidłowego funkcjonowania sieci komputerowych.