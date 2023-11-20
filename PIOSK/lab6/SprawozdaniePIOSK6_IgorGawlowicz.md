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
            <Rtext>15.11.2023</Rtext>
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
        <Rtext>6</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Rozwiązywanie problemów z routingiem między sieciami VLAN

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Rozwiązywanie problemów z routingiem między sieciami VLAN

## Część 1: Wyszukiwanie problemów w sieci

Polecenie sugeruje nam użycie nastepujących komend:

```
R1# show ip interface brief
R1# show interface g0/1.10
R1# show interface g0/1.30
S1# show interface trunk
```

Aby odnaleźć wszystkie błędy postąpimy w sposób następujący:

- Sprawdzimy wszystkie połączenia i użyjemy powyższych komend
- Spradzimy czy konfiguracja urządzeń jest taka sama jak w tablicy adresowania
- Zapiszemy wszystkie błędy i ich potencjalne rozwiązania

1. Fizyczny interface G0/1 jest aktywny ale subinterface G0/1.10 jest wyłączony

Rozwiązanie:

Aby włączyć subinterfejs G0/1.10, wykonamy polecenie no shutdown na tym interfejsie.

```cmd
R1(config)#interface g0/1.10
R1(config-subif)#no shutdown
R1(config-subif)#exit
```

2. PC3 ma skonfigurowany nieprawidłowy adres bramy domyślnej.

Rozwiązanie:

Zmienimy adres bramy domyślnej na PC3 z 172.17.10.1 na 172.17.30.1, aby był zgodny z konfiguracją sieci VLAN.

```cmd
R1(config)#interface g0/1.10
R1(config-subif)#no encapsulation dot1Q 

R1(config-subif)#int g0/1.30
R1(config-subif)#no encapsulation dot1Q 
R1(config-subif)#exit
```

3. Interfejs G0/1 na urządzeniu S1 jest skonfigurowany jako port dostępu zamiast portu trunk.

Rozwiązanie:

Aby zmienić interfejs G0/1 na urządzeniu S1 z trybu dostępu na tryb trunk, wykonamy polecenie switchport mode trunk.

```cmd
S1(config)#interface g0/1
S1(config-if)#switchport mode trunk
```

4. Przypisania VLAN dla subinterfejsów zostały zamienione na urządzeniu R1. Skonfigurowane przypisania nie zgadzają się z tymi przedstawionymi w tablicy adresowania.

Rozwiązanie:

Aby naprawić niezgodne przypisania VLAN dla subinterfejsów na R1, wykonaj następujące kroki:

```cmd
R1(config)#int g0/1.10
R1(config-subif)#encapsulation dot1Q 10
R1(config-subif)#ip address 172.17.10.1 255.255.255.0
R1(config-subif)#
R1(config-subif)#int g0/1.30
R1(config-subif)#encapsulation dot1Q 30
R1(config-subif)#ip address 172.17.30.1 255.255.255.0
```

## Wnioski

Podczas tego laboratorium wykorztstaliśmy naszą wcześniej zdobytą wiedzę, zby znaleźć i zneutralizować błedy w konfiguracji sieciowej.
Po zidentyfikowaniu i naprawieniu problemów konfiguracja działa prawidłowo.