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
            <Rtext>25.10.2023</Rtext>
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
        <Rtext>4</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfigurowanie routingu między sieciami VLAN sposobem router na patyku

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Konfigurowanie routingu między sieciami VLAN sposobem router na patyku

## Część 1: Tworzenie sieci VLAN w przełaczniku

Zaczniemy od stworzenia sieci VLAN 10 i 30

```cmd
S1(config)#vlan 10
S1(config-vlan)#vlan 30
```

Następnie przypiszemy te sieci do odpowiednich portów 

```cmd
S1(config)#interface f0/11
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 10
S1(config-if)#interface f0/6
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 30
```

Kolejnym krokiem było sprawdzenie czy w wszystko jest w porządku za pomocą `show vlan brief`, po czym sprawdziliśmy czy PC1 łączy się z PC3 na co otrzymaliśmy negatywny rezultat.

Jest to spowodowane tym że komputery są pod innym adresem IP więc wymagają routera do poprawnej komunikacji.

## Część 2: Konfiguracja podinterfejsów

Zaczniemy od utworzenia interfejsów dla wcześniej stworzonych vlanów

VLAN 10
```cmd
R1(config)# int g0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 172.17.10.1 255.255.255.0
```

VLAN 30
```cmd
R1(config-subif)#int g0/0.30
R1(config-subif)#encapsulation dot1Q 30
R1(config-subif)#ip address 172.17.30.1 255.255.255.0
```

Następnie ponownie zweryfikujemy konfigurację za pomocą `show vlan brief`

Możemy zauważyć że oba nasze nowo utworzone interfejsy są nieaktywne, będziemy musieli je więc uruchomić.

```cmd
R1(config)#interface g0/0
R1(config-if)#no shutdown

R1(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up

%LINK-5-CHANGED: Interface GigabitEthernet0/0.10, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0.10, changed state to up

%LINK-5-CHANGED: Interface GigabitEthernet0/0.30, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0.30, changed state to up

```

## Część 3: Testowanie łączność z routingiem między sieciami VLAN

Ping dalej nie powodzi się ponieważ wciąż nie ustawiliśmy połączenie trunk

G0/1 jest przypisany do sieci VLAN 1

Ustawimy teraz połączenie trunk

```cmd
S1(config)#int g0/1
S1(config-if)#switchport mode trunk

S1(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

```

*Jak można określić, że interfejs jest portem trunk, używając polecenia show vlan?*

Interfejs nie jest już widoczny przy poleceniu `show vlan`

```cmd
S1#show interface trunk
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gig0/1      1-1005

Port        Vlans allowed and active in management domain
Gig0/1      1,10,30

Port        Vlans in spanning tree forwarding state and not pruned
Gig0/1      1,10,30
```

Teraz w końcu jesteśmy w stanie uzyskać połączenie między PC1 i PC3

## Wnioski

Ćwiczenie laboratoryjne dotyczyło konfiguracji routingu między VLAN-ami za pomocą podejścia "router-on-a-stick". Celem było umożliwienie komunikacji między urządzeniami w różnych VLAN-ach. W rezultacie skonfigurowano VLAN-y na przełączniku, utworzono podinterfejsy na routerze i skonfigurowano połączenie trunk między nimi. Dzięki temu udało się uzyskać poprawną komunikację między VLAN-ami.