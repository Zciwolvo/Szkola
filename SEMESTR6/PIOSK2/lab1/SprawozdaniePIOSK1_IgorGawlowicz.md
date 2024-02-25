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
            <Rtext>22.02.2023</Rtext>
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
        <Rtext>1</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Konfiguruj statyczne i domyślne trasy IPv4 i IPv6s

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Packet Tracer - Konfiguruj statyczne i domyślne trasy IPv4 i IPv6

## Część 1: Konfigurowanie statycznych i pływających statycznych tras domyślnych IPv4

*Sieć PT wymaga tras statycznych, aby zapewnić dostęp do Internetu wewnętrznym użytkownikom sieci LAN za pośrednictwem ISP. Ponadto routery ISP wymagają tras statycznych, aby dotrzeć do wewnętrznych sieci LAN. W tej części działania zostanie skonfigurowana statyczna trasa domyślna IPv4 i pływająca trasa domyślna w celu dodania nadmiarowości do sieci.*

### Krok 1: Skonfiguruj domyślną trasę statyczną IPv4.

W Edge_Router skonfiguruj bezpośrednio podłączoną domyślną trasę statyczną IPv4. Ta główna trasa domyślna powinna prowadzić przez router ISP1.

```bash
Edge_Router>enable
	
Edge_Router#config
Configuring from terminal, memory, or network [terminal]? 
Enter configuration commands, one per line.  End with CNTL/Z.

Edge_Router(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.1
```

### Krok 2: Skonfiguruj pływającą statyczną trasę domyślną IPv4.

Na Edge_Router skonfiguruj statyczną domyślną pływającą trasę IPv6 następnego przeskoku. Trasa powinna prowadzić przez router ISP2. Użyj dystansu administracyjnego równego 5.

```bash
Edge_Router(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.5 5
```

## Część 2: Konfiguracja statycznych i ruchomych statycznych tras domyślnych IPv6

*W tej części działania zostaną skonfigurowane statyczne domyślne i pływające statyczne trasy domyślne protokołu IPv6.*

### Krok 1: Skonfiguruj domyślną trasę statyczną IPv6.

Na Edge_Router skonfiguruj domyślną trasę statyczną następnego przeskoku. Ta główna trasa domyślna powinna prowadzić przez router ISP1.

```bash
Edge_Router(config)#ipv6 route ::/0 2001:db8:a:1::1
```

### Krok 2: Skonfiguruj pływającą statyczną trasę domyślną IPv6.

Na Edge_Router skonfiguruj statyczną domyślną pływającą trasę IPv6 następnego przeskoku. Trasa powinna prowadzić przez router ISP2. Użyj dystansu administracyjnego równego 5.

```bash
Edge_Router(config)#ipv6 route ::/0 2001:db8:a:2::1 5
```

## Część 3: Konfigurowanie statycznych i pływających tras statycznych IPv4 do wewnętrznych sieci LAN

*W tej części laboratorium skonfigurujesz statyczne i pływające routery statyczne z routerów ISP do wewnętrznych sieci LAN.*


### Krok 1: Skonfiguruj statyczne trasy IPv4 do wewnętrznych sieci LAN.

- a. Na ISP1 skonfiguruj trasę statyczną IPv4 następnego przeskoku do sieci LAN 1 przez Edge_Router.

    ```bash
    ISP1(config)#ip route 192.168.10.16 255.255.255.240 10.10.10.2
    ```

- b. Na ISP1 skonfiguruj trasę statyczną IPv4 następnego przeskoku do sieci LAN 2 przez Edge_Router.

    ```bash
    ISP1(config)#ip route 192.168.11.32 255.255.255.224 10.10.10.2
    ```

### Krok 2: Skonfiguruj pływające trasy statyczne IPv4 do wewnętrznych sieci LAN.

- a. Na ISP1 skonfiguruj bezpośrednio podłączoną pływającą trasę statyczną do sieci LAN 1 za pośrednictwem routera ISP2. Użyj dystansu administracyjnego równego 5.

    ```bash
    ISP1(config)#ip route 192.168.10.16 255.255.255.240 g0/0 5
    ```

- b Na ISP1 skonfiguruj bezpośrednio podłączoną pływającą trasę statyczną do sieci LAN 2 przez router ISP2. Użyj dystansu administracyjnego równego 5.

    ```bash
    ISP1(config)#ip route 192.168.11.32 255.255.255.224 g0/0 5
    ```

## Część 4: Skonfiguruj statyczne i pływające trasy statyczne IPv6 do wewnętrznych sieci LAN.

### Krok 1: Skonfiguruj statyczne trasy IPv6 do wewnętrznych sieci LAN.

- c. Na ISP1 skonfiguruj następną trasę statyczną IPv6 dosieci LAN 1 za pośrednictwem Edge_Router.

    ```bash
    ISP1(config)#ipv6 route 2001:db8:1:10::/64 2001:db8:a:1::2
    ```

- d. NaISP1 skonfiguruj następną trasę statyczną IPv6 do sieci LAN 2 za pośrednictwem Edge_Router.
  
    ```bash
    ISP1(config)#ipv6 route 2001:db8:1:11::/64 2001:db8:a:1::2
    ```

### Krok 2: Skonfiguruj pływające trasy statyczne IPv6 do wewnętrznych sieci LAN.

- a. Na ISP1 skonfiguruj następną zmienną trasę statyczną IPv6 do sieci LAN 1 za pośrednictwem routera ISP2. Użyj dystansu administracyjnego równego 5.

    ```bash
    ISP1(config)#ipv6 route 2001:db8:1:10::/64 2001:db8:f:f::2 5
    ```

- b. Na ISP1 skonfiguruj następną zmienną trasę statyczną IPv6 do sieci LAN 2 za pośrednictwem routera ISP2. Użyj dystansu administracyjnego równego 5.

    ```bash
    ISP1(config)#ipv6 route 2001:db8:1:11::/64 2001:db8:f:f::2 5
    ```

*Jeśli konfiguracja została zakończona poprawnie, powinieneś mieć możliwość pingowania serwera WWW z hostów w sieciach LAN 1 i LAN 2. Ponadto, jeśli główne łącze trasy jest wyłączone, łączność między hostami sieci LAN a serwerem sieci Web powinna nadal istnieć.*

## Część 5: Konfigurowanie tras hosta

*Użytkownicy sieci firmowej często mają dostęp do serwera należącego do ważnego klienta. W tej części działania, można skonfigurować statyczne trasy hosta do serwera. Jedna trasa będzie pływającą trasą statyczną obsługującą nadmiarowe połączenia ISP.*

### Krok 1: Skonfiguruj trasy hosta IPv4.

- a. Na Edge Router skonfiguruj bezpośrednio połączoną trasę IPv4 do serwera klienta.

    ```bash
    Edge_Router(config)#ip route 198.0.0.10 255.255.255.255 serial0/0/0
    ```

- b. Na Edger Router skonfiguruj bezpośrednio podłączoną pływającą trasę IPv4 hosta do serwera odbiorcy. Użyj dystansu administracyjnego równego 5.

    ```bash
    Edge_Router(config)#ip route 198.0.0.10 255.255.255.255 serial0/0/1 5
    ```

### Krok 2: Skonfiguruj trasy hosta IPv6.

- a. Na routerze Edge skonfiguruj trasę hosta następnego przeskoku IPv6 do serwera klienta przez router ISP1.

    ```bash
    Edge_Router(config)#ipv6 route 2001:db8:f:f::10/128 2001:db8:a:1::1
    ```

- b. Na Edger Router skonfiguruj bezpośrednio podłączoną pływającą trasę IPv6 hosta do odbiorcy za pośrednictwem routera ISP2. Użyj dystansu administracyjnego równego 5.

    ```bash
    Edge_Router(config)#ipv6 route 2001:db8:f:f::10/128 2001:db8:a:2::1 5
    ```