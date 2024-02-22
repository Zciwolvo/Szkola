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
            <Rtext>08.11.2023</Rtext>
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
        <Rtext>5</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguracja przełączania w warstwie 3 i routingu między sieciami VLAN

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Konfiguracja przełączania w warstwie 3 i routingu między sieciami VLAN

## Część 1: Konfiguracja przełączania warstwy 3

Zaczynamy od skonfigurowania `G0/2`

```cmd
MLS>enable
MLS#config
Configuring from terminal, memory, or network [terminal]? 
Enter configuration commands, one per line.  End with CNTL/Z.
MLS(config)#interface g0/2
MLS(config-if)#no switchport
MLS(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to up

MLS(config-if)#ip address 209.165.200.225 255.255.255.252
```

Następnie możemy zweryfikować działanie naszego połączenia poprzez:

```cmd
MLS#ping 209.165.200.225

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 209.165.200.225, timeout is 2 seconds:
.!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 0/2/7 ms

```

## Część 2: Konfiguracja routingu między sieciami VLAN

Musimy zacząć od dodania sieci VLAN

```cmd
MLS(config)#vlan 10
MLS(config-vlan)#name Staff
MLS(config-vlan)#vlan 20
MLS(config-vlan)#name Student
MLS(config-vlan)#vlan 30
MLS(config-vlan)#name Faculty
```

Następnie skonfigurujemy SVI na MLS

```cmd
MLS(config)#interface vlan 10
MLS(config-if)#
%LINK-5-CHANGED: Interface Vlan10, changed state to up

MLS(config-if)#ip address 192.168.10.254 255.255.255.0
MLS(config-if)#interface vlan 20
MLS(config-if)#
%LINK-5-CHANGED: Interface Vlan20, changed state to up

MLS(config-if)#ip address 192.168.20.254 255.255.255.0
MLS(config-if)#interface vlan 30
MLS(config-if)#
%LINK-5-CHANGED: Interface Vlan30, changed state to up

MLS(config-if)#
MLS(config-if)#ip address 192.168.30.254 255.255.255.0
MLS(config-if)#ipv6 address 2001:db8:acad:30::1/64
MLS(config-if)#interface vlan 99
MLS(config-if)#
%LINK-5-CHANGED: Interface Vlan99, changed state to up

MLS(config-if)#ip address 192.168.99.254 255.255.255.0
MLS(config-if)#
```

Po czym skonfigurujemy trunki na MLS

```cmd
MLS(config)#interface g0/1
MLS(config-if)#switchport mode trunk

MLS(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan10, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan20, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan30, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan99, changed state to up

MLS(config-if)#switchport trunk native vlan 99
MLS(config-if)#switchport trunk encapsulation dot1q
```

a teraz skonfigurujemy trunk z poziomu S1

```cmd
S1(config)#interface g0/1
S1(config-if)#switchport mod
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (1), with MLS GigabitEthe
S1(config-if)#switchport mode trunk

S1(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up
%SPANTREE-2-RECV_PVID_ERR: Received BPDU with inconsistent peer vlan id 99 on GigabitEthernet0/1 VLAN1.

%SPANTREE-2-BLOCK_PVID_LOCAL: Blocking GigabitEthernet0/1 on VLAN0001. Inconsistent local vlan.


S1(config-if)#switchport trunk native vlan 99
```

Teraz musimy włączyć routing

`MLS(config)#ip routing`

Teraz możemy sprawdzić czy wszystko jest skonfigurowane poprawnie

```cmd
MLS#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    192.168.10.0/24 is directly connected, Vlan10
C    192.168.20.0/24 is directly connected, Vlan20
C    192.168.30.0/24 is directly connected, Vlan30
C    192.168.99.0/24 is directly connected, Vlan99
     209.165.200.0/30 is subnetted, 1 subnets
C       209.165.200.224 is directly connected, GigabitEthernet0/2

```

Teraz możemy sprawdzić bezpośrednio z komputerów czy połączenie jest prawidłowe i dla wszystkich testów otrzymamy podobne rezultaty:

```cmd
C:\>ping 192.168.10.2

Pinging 192.168.10.2 with 32 bytes of data:

Reply from 192.168.10.2: bytes=32 time=12ms TTL=128
Reply from 192.168.10.2: bytes=32 time<1ms TTL=128
Reply from 192.168.10.2: bytes=32 time=1ms TTL=128
Reply from 192.168.10.2: bytes=32 time=1ms TTL=128

Ping statistics for 192.168.10.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 12ms, Average = 3ms
```

## Część 3: Konfiguracja routingu IPv6 między sieciami VLAN

Zaczniemy od włączenia routingu na IPv6

`MLS(config)#ipv6 unicast-routing`

Następnie skonfigurujemy SVI dla protokołu IPv6 na MLS

```cmd
MLS(config)#interface vlan 10
MLS(config-if)#ipv6 address 2001:db8:acad:10::1/64
```

Teraz skonfigurujemy `G0/2`

```cmd
MLS(config)#interface G0/2
MLS(config-if)#ipv6 address 2001:db8:acad:a::1/64
```

Możemy zweryfikować połączenie

```cmd
MLS#show ipv6 route
IPv6 Routing Table - 8 entries
Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP
       U - Per-user Static route, M - MIPv6
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
       O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
       D - EIGRP, EX - EIGRP external
S   ::/0 [1/0]
     via 2001:DB8:ACAD:A::2, GigabitEthernet0/2
C   2001:DB8:ACAD:A::/64 [0/0]
     via ::, GigabitEthernet0/2
L   2001:DB8:ACAD:A::1/128 [0/0]
     via ::, GigabitEthernet0/2
C   2001:DB8:ACAD:10::/64 [0/0]
     via ::, Vlan10
L   2001:DB8:ACAD:10::1/128 [0/0]
     via ::, Vlan10
C   2001:DB8:ACAD:30::/64 [0/0]
     via ::, Vlan30
L   2001:DB8:ACAD:30::1/128 [0/0]
     via ::, Vlan30
L   FF00::/8 [0/0]
     via ::, Null0
```

Ostatecznie sprawdzimy połącznenia z PCtów do MLS, między sobą oraz do chmury żeby zweryfikować poprawność działania konfiguracji.

## Wnioski

- Konfiguracja przełączania w warstwie 3 jest istotnym krokiem w zapewnieniu poprawnej komunikacji między urządzeniami w sieci. Konfiguracja interfejsów i przypisywanie adresów IP pozwala na wymianę danych i ruch między urządzeniami.

- Konfiguracja routingu między sieciami VLAN pozwala na wydzielenie ruchu na różne segmenty sieci, co zwiększa bezpieczeństwo i efektywność sieci. Dodatkowo, trunki umożliwiają przesyłanie ruchu między różnymi VLAN-ami.

- Konfiguracja routingu IPv6 to ważny krok w kierunku zapewnienia przyszłościowej komunikacji w sieciach. IPv6 umożliwia obsługę większej liczby adresów IP i jest coraz bardziej istotny w sieciach.