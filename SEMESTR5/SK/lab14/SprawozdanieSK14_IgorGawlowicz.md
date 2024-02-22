<style>
h1 {
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
            <Rtext>01.06.2023</Rtext>
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
        <Rtext>14</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Weryfikacja adresacji IPv4 i IPv6

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Część 1: Uzupełnienie tabeli adresacji

### Krok 1: Użyj polecenia ipconfig w celu sprawdzenia adresacji IPv4.

Aby sprawdzić adresacji IPv4 musimy wejść w oba komputery i za pomocą polecenia `ipconfig /all` w konsoli otrzymamy wszystkie potrzebne nam informację dotyczące adresowania IPv4 naszych obiektów.

PC1

```bash
C:\>ipconfig /all

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.47CA.4DEE
   Link-local IPv6 Address.........: FE80::260:47FF:FECA:4DEE
   IPv6 Address....................: 2001:DB8:1:1::A
   IPv4 Address....................: 10.10.1.100
   Subnet Mask.....................: 255.255.255.224
   Default Gateway.................: FE80::1
                                     10.10.1.97
   DHCP Servers....................: 0.0.0.0
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-16-28-EE-50-00-60-47-CA-4D-EE
   DNS Servers.....................: ::
                                     0.0.0.0

Bluetooth Connection:

   Connection-specific DNS Suffix..:
   Physical Address................: 0007.ECE0.556B
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
   DHCP Servers....................: 0.0.0.0
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-16-28-EE-50-00-60-47-CA-4D-EE
   DNS Servers.....................: ::
                                     0.0.0.0
```

<div style="page-break-after: always;"></div>

PC2

```bash
C:\>ipconfig /all

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.7034.6930
   Link-local IPv6 Address.........: FE80::260:70FF:FE34:6930
   IPv6 Address....................: 2001:DB8:1:4::A
   IPv4 Address....................: 10.10.1.20
   Subnet Mask.....................: 255.255.255.240
   Default Gateway.................: FE80::3
                                     10.10.1.17
   DHCP Servers....................: 0.0.0.0
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-7D-E7-A7-7A-00-60-70-34-69-30
   DNS Servers.....................: ::
                                     0.0.0.0

Bluetooth Connection:

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.4752.0498
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
   DHCP Servers....................: 0.0.0.0
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-7D-E7-A7-7A-00-60-70-34-69-30
   DNS Servers.....................: ::
                                     0.0.0.0
```

<div style="page-break-after: always;"></div>

### Krok 2: Użyj polecenia ipv6config do weryfikacji adresacji IPv6.

Dla adresu IPv6 możemy zrobić dokładnie to samo za pomocą polecenia `ipv6config /all`.

PC1

```bash
C:\>ipv6config /all

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.47CA.4DEE
   Link-local IPv6 Address.........: FE80::260:47FF:FECA:4DEE
   IPv6 Address....................: 2001:DB8:1:1::A
   Default Gateway.................: FE80::1
   DNS Servers.....................: ::
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-16-28-EE-50-00-60-47-CA-4D-EE

Bluetooth Connection:

   Connection-specific DNS Suffix..:
   Physical Address................: 0007.ECE0.556B
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   Default Gateway.................: ::
   DNS Servers.....................: ::
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-16-28-EE-50-00-60-47-CA-4D-EE
```

PC2

```bash
C:\>ipv6config /all

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.7034.6930
   Link-local IPv6 Address.........: FE80::260:70FF:FE34:6930
   IPv6 Address....................: 2001:DB8:1:4::A
   Default Gateway.................: FE80::3
   DNS Servers.....................: ::
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-7D-E7-A7-7A-00-60-70-34-69-30

Bluetooth Connection:

   Connection-specific DNS Suffix..:
   Physical Address................: 0060.4752.0498
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   Default Gateway.................: ::
   DNS Servers.....................: ::
   DHCPv6 IAID.....................:
   DHCPv6 Client DUID..............: 00-01-00-01-7D-E7-A7-7A-00-60-70-34-69-30
```

Tabela adresowania

| Urządzenie | Interfejs      | Adres IP / Prefiks            | Brama domyślna |
| ---------- | -------------- | ----------------------------- | -------------- |
| R1         | G0/0           | 10.10.1.97 / 255.255.255.224  | ND             |
|            |                | 2001:db8:1:1::1/64            |                |
|            | S0/0/1         | 10.10.1.6 / 255.255.255.252   | ND             |
|            |                | 2001:db8:1:2::2/64            |                |
|            |                | fe80::1                       |                |
| R2         | S0/0/0         | 10.10.1.5 / 255.255.255.252   | ND             |
|            |                | 2001:db8:1:2::1/64            |                |
|            | S0/0/1         | 210.10.1.9 / 255.255.255.252  | ND             |
|            |                | 2001:db8:1:3::1/64            |                |
|            |                | fe80::2                       |                |
| R3         | G0/0           | 10.10.1.17 / 255.255.255.240  | ND             |
|            |                | 2001:db8:1:4::1/64            |                |
|            | S0/0/1         | 10.10.1.10 / 255.255.255.252  | ND             |
|            |                | 2001:db8:1:3::2/64            |                |
|            |                | fe80::3                       |                |
| PC1        | Karta sieciowa | 10.10.1.100 / 255.255.255.224 | 10.10.1.97     |
|            |                | 2001:db8:1:1::a/64            | fe80::1        |
| PC2        | Karta sieciowa | 10.10.1.20 / 255.255.255.240  | 10.10.1.17     |
|            |                | 2001:db8:1:4::a/64            | fe80::3        |

<div style="page-break-after: always;"></div>

## Część 2: Sprawdenie łączności poleceniem ping

### Krok 1: Użyj polecenia ping aby zweryfikować łączność IPv4.

```bash
C:\>ping 10.10.1.20

Pinging 10.10.1.20 with 32 bytes of data:

Reply from 10.10.1.20: bytes=32 time=30ms TTL=125
Reply from 10.10.1.20: bytes=32 time=26ms TTL=125
Reply from 10.10.1.20: bytes=32 time=17ms TTL=125
Reply from 10.10.1.20: bytes=32 time=24ms TTL=125

Ping statistics for 10.10.1.20:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 17ms, Maximum = 30ms, Average = 24ms
```

Pomyślnie możemy zpingować PC2 z PC1

```bash
C:\>ping 10.10.1.100

Pinging 10.10.1.100 with 32 bytes of data:

Reply from 10.10.1.100: bytes=32 time=33ms TTL=125
Reply from 10.10.1.100: bytes=32 time=19ms TTL=125
Reply from 10.10.1.100: bytes=32 time=23ms TTL=125
Reply from 10.10.1.100: bytes=32 time=2ms TTL=125

Ping statistics for 10.10.1.100:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 33ms, Average = 19ms
```

Pomyślnie możemy zpingować PC1 z PC2

<div style="page-break-after: always;"></div>

### Krok 2: Użyj polecenia ping aby zweryfikować łączność IPv6.

```bash
C:\>ping 2001:db8:1:4::a

Pinging 2001:db8:1:4::a with 32 bytes of data:

Reply from 2001:DB8:1:4::A: bytes=32 time=31ms TTL=125
Reply from 2001:DB8:1:4::A: bytes=32 time=2ms TTL=125
Reply from 2001:DB8:1:4::A: bytes=32 time=26ms TTL=125
Reply from 2001:DB8:1:4::A: bytes=32 time=2ms TTL=125

Ping statistics for 2001:DB8:1:4::A:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 31ms, Average = 15ms
```

Pomyślnie możemy zpingować PC2 z PC1

```bash
C:\>ping 2001:db8:1:1::a

Pinging 2001:db8:1:1::a with 32 bytes of data:

Reply from 2001:DB8:1:1::A: bytes=32 time=2ms TTL=125
Reply from 2001:DB8:1:1::A: bytes=32 time=32ms TTL=125
Reply from 2001:DB8:1:1::A: bytes=32 time=19ms TTL=125
Reply from 2001:DB8:1:1::A: bytes=32 time=2ms TTL=125

Ping statistics for 2001:DB8:1:1::A:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 32ms, Average = 13ms
```

Pomyślnie możemy zpingować PC1 z PC2

<div style="page-break-after: always;"></div>

## Część 3: Określenie ścieżki poleceniem trace

### Krok 1: Użyj polecenia tracert, aby sprawdzić ścieżkę IPv4.

#### Z PC1 prześledź trasę do PC2.

Jakie adresy napotkano po drodze?

`10.10.1.97, 10.10.1.5, 10.10.1.10, 10.10.1.20`

Z którymi interfejsami są skojarzone cztery adresy?

`G0/0 z R1, S0/0/0 z R2, S0/0/1 z R3, Karta sieciowa z PC2`

#### Z PC2 prześledź trasę do PC1.

Jakie adresy napotkano po drodze?

`10.10.1.17, 10.10.1.9, 10.10.1.6, 10.10.1.100`

Z którymi interfejsami są skojarzone cztery adresy?

`G0/0 z R3, S0/0/1 z R2, S0/0/1 z R1, Karta sieciowa z PC1`

### Krok 2: Użyj polecenia tracert, aby sprawdzić ścieżkę IPv6.

#### Z PC1 prześledź trasę do adresu IPv6 PC2.

Jakie adresy napotkano po drodze?

`2001:db8:1:1::1, 2001:db8:1:2::1, 2001:db8:1:3::2, 2001:db8:1:4::a`

Z którymi interfejsami są skojarzone cztery adresy?

`G0/0 z R1, S0/0/0 z R2, S0/0/1 z R3, Karta sieciowa z PC2`

#### Z PC2 prześledź trasę do adresu IPv6 PC1.

Jakie adresy napotkano po drodze?

`2001:db8:1:4::1, 2001:db8:1:3::1, 2001:db8:1:2::2, 2001:db8:1:1::a`

Z którymi interfejsami są skojarzone cztery adresy?

`G0/0 z R3, S0/0/1 z R2, S0/0/1 z R1, Karta sieciowa z PC1`
