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
            <Rtext>11.10.2023</Rtext>
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
        <Rtext>2</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b>

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Konfiguracja sieci VLAN

## Część 1: Wyświetlanie domyślnej konfiguracji sieci VLAN

`S1>show vlan brief`

| VLAN | Name               | Status | Ports                                                                                                                                                                                         |
| ---- | ------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | default            | active | Fa0/1, Fa0/2, Fa0/3, Fa04,Fa0/5, Fa0/6, Fa0/7, Fa0/8,Fa0/9, Fa0/10,Fa0/11, Fa0/12,Fa0/13, Fa0/14, Fa0/15, Fa0/16,Fa0/17, Fa0/18, Fa0/19, Fa0/20,Fa0/21, Fa0/22, Fa0/23, Fa0/24,Gig0/1, Gig0/2 |
| 1002 | fddi-default       | active |                                                                                                                                                                                               |
| 1003 | token-ring-default | active |                                                                                                                                                                                               |
| 1004 | fddinet-default    | active |                                                                                                                                                                                               |
| 1005 | trnet-default      | active |                                                                                                                                                                                               |

Możemy zauważyć że ze wględu na to że komputery są w jednej sieci VLAN każdy komputer może się wzajomnie ze sobą skontaktować

```cmd
Cisco Packet Tracer PC Command Line 1.0
C:\>ping 172.17.10.24

Pinging 172.17.10.24 with 32 bytes of data:

Reply from 172.17.10.24: bytes=32 time=15ms TTL=128
Reply from 172.17.10.24: bytes=32 time=11ms TTL=128
Reply from 172.17.10.24: bytes=32 time=10ms TTL=128
Reply from 172.17.10.24: bytes=32 time=1ms TTL=128

Ping statistics for 172.17.10.24:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 15ms, Average = 9ms

```

Taka sama sytuacja powinna nastąpić dla każdego urządzenia w tej samej sieci.

Głównymi korzściami sieci VLAN są:

- Bezpieczeństwo
- redukcja kosztów
- lepsza wydajność
- prostota w zarządzaniu

## Część 2: Konfiguracja sieci VLAN

```cmd
S1>enable
S1#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 10
S1(config-vlan)#name Faculty/Staff
S1(config-vlan)#exit
S1(config)#vlan 20
S1(config-vlan)#name Students
S1(config-vlan)#exit
S1(config)#vlan 30
S1(config-vlan)#name Guest(Default)
S1(config-vlan)#exit
S1(config)#vlan 99
S1(config-vlan)#name Management&Native
S1(config-vlan)#exit
S1(config)#vlan 150
S1(config-vlan)#name VOICE
S1(config-vlan)#exit
```

`S1#show vlan brief`

| VLAN | Name               | Status | Ports                                                                                                                                                                                         |
| ---- | ------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | default            | active | Fa0/1, Fa0/2, Fa0/3, Fa04,Fa0/5, Fa0/6, Fa0/7, Fa0/8,Fa0/9, Fa0/10,Fa0/11, Fa0/12,Fa0/13, Fa0/14, Fa0/15, Fa0/16,Fa0/17, Fa0/18, Fa0/19, Fa0/20,Fa0/21, Fa0/22, Fa0/23, Fa0/24,Gig0/1, Gig0/2 |
| 10   | Faculty/Staff      | active |
| 20   | Students           | active |
| 30   | Guest(Default)     | active |
| 99   | Management&Native  | active |
| 150  | VOICE              | active |
| 1002 | fddi-default       | active |                                                                                                                                                                                               |
| 1003 | token-ring-default | active |                                                                                                                                                                                               |
| 1004 | fddinet-default    | active |                                                                                                                                                                                               |
| 1005 | trnet-default      | active |                                                                                                                                                                                               |

Następnie zgodnie z poleceniem utorzyliśmy takie same VLANy dla sieci S2 i S3.

## Część 3: Przypisywanie sieci VLAN do portów

```cmd
S2(config)#interface f0/11
S2(config-if)#switchport mode access
S2(config-if)#switchport access vlan 10
S2(config-if)#exit

S2(config)#interface f0/18
S2(config-if)#switchport mode access
S2(config-if)#switchport access vlan 20
S2(config-if)#exit

S2(config)#interface f0/6
S2(config-if)#switchport mode access
S2(config-if)#switchport access vlan 30
```

W powyższych poleceniach przypisaliśmy VLAN 10 do interface FastEthernet 0/11, następnie VLAN 20 do FE 0/18 i ostatecznie VLAN 30 do FE 0/6.
Kolejnym krokiem było wykorzystanie tego samego ciągu poleceń dla S3

```cmd
S3(config)#interface f0/11
S3(config-if)#mls qos trust cos
S3(config-if)#switchport voice vlan 150
```

W powyższym poleceniu połączyliśmy telefon.

Po ponownym sprawdzeniu sieci VLAN z S2 możemy zauważyć że nasze porty zostały połączone poprawnie i teraz w kolumnie _Ports_, mamy pokazane odpowiednie porty.

_Spróbuj wykonać test ping pomiędzy PC1 i PC4._

_Pomimo tego, że porty zostały przydzielone do odpowiednich sieci VLAN test ping nie kończy się sukcesem. Wyjaśnij._

Kończy się on niepowodzeniem ponieważ switche są w sieci VLAN 1 a komputery w sieci VLAN 10

_Co można zrobić, aby rozwiązać ten problem?_

Możemy to rozwiązać poprzez wykorzystanie połączenia **trunk**

# Packet Tracer - Konfiguracja połączeń trunk

## Część 1: Weryfikacja sieci VLAN

| VLAN | Name               | Status | Ports                                                                                                                                                                                         |
| ---- | ------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | default            | active | Fa0/1, Fa0/2, Fa0/3, Fa04,Fa0/5, Fa0/6, Fa0/7, Fa0/8,Fa0/9, Fa0/10,Fa0/11, Fa0/12,Fa0/13, Fa0/14, Fa0/15, Fa0/16,Fa0/17, Fa0/18, Fa0/19, Fa0/20,Fa0/21, Fa0/22, Fa0/23, Fa0/24,Gig0/1, Gig0/2 |
| 10   | Faculty/Staff      | active |
| 20   | Students           | active |
| 30   | Guest(Default)     | active |
| 99   | Management&Native  | active |
| 150  | VOICE              | active |
| 1002 | fddi-default       | active |                                                                                                                                                                                               |
| 1003 | token-ring-default | active |                                                                                                                                                                                               |
| 1004 | fddinet-default    | active |                                                                                                                                                                                               |
| 1005 | trnet-default      | active |                                                                                                                                                                                               |

W S2 i S3 róznica jest tak że w poprzednim ćwiczeniu połączyliśmy VLANy do odpowiednich portów.

W ostatnim kroku poprzedniego ćwiczenia wyjaśniliśmy też dlaczego PC1 i PC4 nie są w stanie załapać ze sobą połączenia.

## Część 2: Konfiguracja łączy trunk

```cmd
S1>enable
S1#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#interface range g0/1 -2
S1(config-if-range)#switchport mode trunk


S1(config-if-range)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to up

S1(config-if-range)#switchport trunk native vlan 99
S1(config-if-range)#
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (99), with S2 GigabitEthernet0/1 (1).

%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/2 (99), with S3 GigabitEthernet0/2 (1).

S1(config-if-range)#
```

Możemy teraz zauważyć że odkąd ustawiliśmy połączenie trunk możemy z powodzeniem pingować wszystkie komputery w sieci.

```cmd
C:\>ping 172.17.10.24

Pinging 172.17.10.24 with 32 bytes of data:

Reply from 172.17.10.24: bytes=32 time=3ms TTL=128
Reply from 172.17.10.24: bytes=32 time=11ms TTL=128
Reply from 172.17.10.24: bytes=32 time<1ms TTL=128
Reply from 172.17.10.24: bytes=32 time=13ms TTL=128

Ping statistics for 172.17.10.24:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 13ms, Average = 6ms
```

Po sprawdzeniu komendą `show interface trunk` możemy zauważyć że DTP pomyślnie wynegocjował połącznia trunk.

_Które aktywne sieci VLAN są dozwolone na połączeniach trunk?_

1,10,20,30,88,99

Możemy teraz poprawić błąd niedopasowania natywnego poprzez wpisanie następujących poleceń dla S2 i S3 z różnicą tego że do jednego skorzystamy z interfacu g0/1, a drugiego g0/2

```cmd
S2>enable
S2#config
Configuring from terminal, memory, or network [terminal]?
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#interface g0/1
S2(config-if)#switchport mode trunk
S2(config-if)#switchport trunk native vlan 99
S2(config-if)#%SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking GigabitEthernet0/1 on VLAN0099. Port consistency restored.

%SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking GigabitEthernet0/1 on VLAN0001. Port consistency restored.
```

Następnie możemy zweryfikować czy błąd udało się naprawić poprzez polecenie

`S2#show interface g0/1 switchport`

`S3#show interface g0/2 switchport`

I powiniśmy otrzymać mniej więcej taki wynik

```cmd
Name: Gig0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (Native)
Voice VLAN: none
Administrative private-vlan host-association: none
Administrative private-vlan mapping: none
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: All
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL
Protected: false
Unknown unicast blocked: disabled
Unknown multicast blocked: disabled
Appliance trust: none
```

_Dlaczego port G0/1 na S2 nie jest już przypisany do sieci VLAN 1?_

Port G0/1 nie jest wyświetlany ponieważ trunk porty nie są nigdy listowane w zestawieniu.
