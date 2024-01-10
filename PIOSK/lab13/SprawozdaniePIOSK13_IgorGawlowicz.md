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
            <Rtext>10.01.2024</Rtext>
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
        <Rtext>13</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Rozwiązywanie problemów z trasami statycznymi i domyślnymi

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Rozwiązywanie problemów z trasami statycznymi i domyślnymi

*Nowo zatrudniony technik sieciowy próbuje wstępnie skonfigurować prostą topologię, która zostanie dostarczona klientowi. Technik nie był w stanie ustalić łączności między trzema sieciami LAN. Poproszono Cię o rozwiązanie problemów z topologią i sprawdzenie łączności między hostami w trzech sieciach LAN przez IPv4 i IPv6.*

Zaczniemy od przeanalizowania ścieżek na wszystkich 3 routerach


R1
```bash
R1#show ip route 
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is 172.31.1.195 to network 0.0.0.0

     172.31.0.0/16 is variably subnetted, 4 subnets, 3 masks
C       172.31.1.0/25 is directly connected, GigabitEthernet0/0
L       172.31.1.1/32 is directly connected, GigabitEthernet0/0
C       172.31.1.192/30 is directly connected, Serial0/0/0
L       172.31.1.194/32 is directly connected, Serial0/0/0
S*   0.0.0.0/0 [1/0] via 172.31.1.195

R1#
R1#show ipv6 route 
IPv6 Routing Table - 8 entries
Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP
       U - Per-user Static route, M - MIPv6
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
       O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
       D - EIGRP, EX - EIGRP external
C   2001:DB8:1::/64 [0/0]
     via GigabitEthernet0/0, directly connected
L   2001:DB8:1::1/128 [0/0]
     via GigabitEthernet0/0, receive
C   2001:DB8:2::/64 [0/0]
     via Serial0/0/0, directly connected
L   2001:DB8:2::194/128 [0/0]
     via Serial0/0/0, receive
S   2001:DB8:3::/64 [1/0]
     via Serial0/0/0, directly connected
S   2001:DB8:4::/64 [1/0]
     via Serial0/0/0, directly connected
S   2001:DB8:5::/64 [1/0]
     via Serial0/0/0, directly connected
L   FF00::/8 [0/0]
     via Null0, receive
R1#
```

R2
```bash
R2#show ip route 
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     172.31.0.0/16 is variably subnetted, 8 subnets, 5 masks
C       172.31.0.0/24 is directly connected, GigabitEthernet0/0
L       172.31.0.1/32 is directly connected, GigabitEthernet0/0
S       172.31.1.0/25 [1/0] via 172.31.1.198
S       172.31.1.128/26 [1/0] via 172.31.1.194
C       172.31.1.192/30 is directly connected, Serial0/0/0
L       172.31.1.193/32 is directly connected, Serial0/0/0
C       172.31.1.196/30 is directly connected, Serial0/0/1
L       172.31.1.197/32 is directly connected, Serial0/0/1

R2#show ipv6 route 
IPv6 Routing Table - 9 entries
Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP
       U - Per-user Static route, M - MIPv6
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
       O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
       D - EIGRP, EX - EIGRP external
S   2001:DB6:1::/64 [1/0]
     via 2001:DB8:2::194
C   2001:DB8:2::/64 [0/0]
     via Serial0/0/0, directly connected
L   2001:DB8:2::193/128 [0/0]
     via Serial0/0/0, receive
C   2001:DB8:3::/64 [0/0]
     via GigabitEthernet0/0, directly connected
L   2001:DB8:3::1/128 [0/0]
     via GigabitEthernet0/0, receive
C   2001:DB8:4::/64 [0/0]
     via Serial0/0/1, directly connected
L   2001:DB8:4::197/128 [0/0]
     via Serial0/0/1, receive
S   2001:DB8:5::/64 [1/0]
     via 2001:DB8:4::198
L   FF00::/8 [0/0]
     via Null0, receive
R2#
```

R3
```bash
R3#show ip route 
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     172.31.0.0/16 is variably subnetted, 7 subnets, 5 masks
S       172.31.0.0/24 is directly connected, Serial0/0/1
S       172.31.1.0/28 is directly connected, Serial0/0/1
C       172.31.1.128/26 is directly connected, GigabitEthernet0/0
L       172.31.1.129/32 is directly connected, GigabitEthernet0/0
S       172.31.1.192/30 is directly connected, Serial0/0/1
C       172.31.1.196/30 is directly connected, Serial0/0/1
L       172.31.1.198/32 is directly connected, Serial0/0/1

R3#show ipv6 route 
IPv6 Routing Table - 7 entries
Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP
       U - Per-user Static route, M - MIPv6
       I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
       ND - ND Default, NDp - ND Prefix, DCE - Destination, NDr - Redirect
       O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
       ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
       D - EIGRP, EX - EIGRP external
S   2001:DB8:2::/64 [1/0]
     via Serial0/0/1, directly connected
S   2001:DB8:3::/64 [1/0]
     via Serial0/0/1, directly connected
C   2001:DB8:4::/64 [0/0]
     via Serial0/0/1, directly connected
L   2001:DB8:4::198/128 [0/0]
     via Serial0/0/1, receive
C   2001:DB8:5::/64 [0/0]
     via GigabitEthernet0/0, directly connected
L   2001:DB8:5::1/128 [0/0]
     via GigabitEthernet0/0, receive
L   FF00::/8 [0/0]
     via Null0, receive
R3#
```

Na podstawie powyższych wyników możemy dojść do następujących wniosków

| Lokalizacja | Problem | Rozwiązanie |
|-------------|---------|-------------|
| R1 | Adres interfejsu następnej bramy domyślnej IPv4 jest niepoprawny. | Zmień adres następnej bramy na 172.31.1.193 |
| R2 | Trasa IPv6 do LAN 1 ma niepoprawny adres sieci docelowej. | Zmień adres docelowy z 2001:DB6:1::/64 na 2001:DB8:1::/64 |
| R2 | Adresy następnej bramy w dwóch trasach IPv4 są zamienione. | Zmień polecenia na ip route 172.31.1.0 255.255.255.128 172.31.1.194 i ip route 172.31.1.128 255.255.255.192 172.31.1.198 |
| R3 | Trasa IPv6 do LAN 1 jest brakująca. | Skonfiguruj statyczną trasę bezpośrednio połączoną do 2001:DB8:1::/64 |
| R3 | Trasa IPv4 do LAN 1 ma niepoprawną maskę sieci. | Zmień maskę na 255.255.255.128 |

Teraz żeby rozwiązać te problemy musimy zrobić następujące operacje na routerach

R1
```bash
enable
conf t
no ip route 0.0.0.0 0.0.0.0 172.31.1.195
ip route 0.0.0.0 0.0.0.0 172.31.1.193
end
```

R2
```bash
enable
conf t
no ip route 172.31.1.0 255.255.255.128 172.31.1.198
no ip route 172.31.1.128 255.255.255.192 172.31.1.194
ip route 172.31.1.0 255.255.255.128 172.31.1.194
ip route 172.31.1.128 255.255.255.192 172.31.1.198
no ipv6 route 2001:DB6:1::/64 2001:DB8:2::194
ipv6 route 2001:DB8:1::/64 2001:DB8:2::194
end
```

R3
```bash
enable
conf t
no ip route 172.31.1.0 255.255.255.240 Serial0/0/1
ip route 172.31.1.0 255.255.255.128 Serial0/0/1
ipv6 route 2001:DB8:1::/64 Serial0/0/1
end
```

Po implementacji tych zmian konfiguracja jest zgodna z tabelą adresowania i wszystko powinno działać w porządku.
