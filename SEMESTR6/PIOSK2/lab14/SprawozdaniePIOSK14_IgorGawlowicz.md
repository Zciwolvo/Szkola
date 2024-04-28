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
            <Rtext>27.04.2023</Rtext>
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
        <Rtext>14</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Packet Tracer - Rozwiązywanie problemów - Udokumentuj sieć

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

# Packet Tracer - Rozwiązywanie problemów - Udokumentuj sieć

Twój pracodawca został zatrudniony do przejęcia administracji siecią firmową, ponieważ poprzedni administrator sieci opuścił firmę. Nie ma dokumentacji sieciowej i należy ją odtworzyć. Twoim zadaniem jest udokumentowanie hostów i urządzeń sieciowych, w tym wszystkich adresów urządzeń i logicznych połączeń. Będziesz mieć zdalny dostęp do urządzeń sieciowych i użyjesz funkcji wykrywania sieci do uzupełnienia tabeli urządzeń i narysowania topologii sieci.

To jest część I dwuczęściowej serii ćwiczeń. Będziesz używać dokumentacji, którą utworzysz w tym ćwiczeniu, aby poprowadzić Cię podczas rozwiązywania problemów z siecią w części II, Packet Tracer - Rozwiązywanie problemów - używanie dokumentacji do rozwiązywania problemów.

Podczas badania i dokumentowania topologii sieci zanotuj stwierdzone problemy, które nie są zgodne z praktykami przedstawionymi w programie CCNA.

# Część 1: Testowanie Połączenia

Wykonaj ping między komputerami a serwerem internetowym, aby przetestować sieć. Wszystkie komputery powinny móc pingować się nawzajem oraz serwer internetowy.

# Część 2: Poznawanie Konfiguracji Komputerów

Przejdź do wiersza polecenia każdego komputera i wyświetl ustawienia IP. Zapisz te informacje w tabeli dokumentacyjnej.

# Część 3: Poznawanie Informacji o Urządzeniach Bramy Domyślnej

Połącz się z każdym urządzeniem bramy domyślnej za pomocą protokołu Telnet i zapisz informacje o interfejsach używanych w tabeli. Hasło VTY to `cisco`, a hasło privileged EXEC to `class`.

```bash
C:\> telnet Adres_IP
```

# Część 4: Odtwarzanie Topologii Sieci

W tej części działalności będziesz kontynuować rejestrowanie informacji o urządzeniach w sieci w tabeli Adresacji. Ponadto, zaczniesz opracowywać topologię sieci na podstawie informacji o interakcjach urządzeń, które możesz odkryć.

## Krok 1: Dostęp do Tablic Routingu na Każdym Urządzeniu Bramy Domyślnej

Wykorzystaj tablice routingu w każdym ruterze, aby dowiedzieć się więcej o sieci. Dokonaj notatek na temat swoich odkryć.

## Krok 2: Odkrywanie Urządzeń Niekoniecznie Bramy Domyślnej

Wykorzystaj protokół odkrywania sieci do dokumentowania sąsiednich urządzeń. Zapisz swoje odkrycia w tabeli adresacji. W tym momencie powinieneś również móc rozpocząć dokumentowanie interakcji urządzeń.

# Część 5: Dalsze Eksplorowanie Konfiguracji i Interakcji Urządzeń

## Krok 1: Dostęp do Konfiguracji Urządzeń

Podłącz się do innych urządzeń w sieci. Zdobądź informacje na temat konfiguracji urządzeń.

## Krok 2: Wyświetlanie Informacji o Sąsiedztwie

Wykorzystaj protokoły odkrywania, aby zwiększyć swoją wiedzę na temat urządzeń sieciowych i topologii.

## Krok 3: Podłączanie do Innych Urządzeń

Wyświetl informacje o konfiguracji dla innych urządzeń w sieci. Zapisz swoje odkrycia w tabeli urządzeń.

Teraz powinieneś znać wszystkie urządzenia i konfiguracje interfejsów w sieci. Wszystkie wiersze tabeli powinny zawierać informacje o urządzeniach. Wykorzystaj swoje informacje, aby odtworzyć jak najwięcej topologii sieci, jak to możliwe.

# Refleksja

Mogłeś zauważyć, że niektóre praktyki używane do konfigurowania urządzeń sieciowych są przestarzałe, niewydajne lub niebezpieczne. Sporządź listę zaleceń dotyczących ponownej konfiguracji urządzeń zgodnie z praktykami, które nauczyłeś się w programie CCNA.

- Wszystkie urządzenia używają tych samych prostych i dobrze znanych haseł. Powinny być one zmienione, powinny się różnić między urządzeniami, a także powinny być silniejsze.
- Większość portów przełącznika znajduje się w VLAN 1. Należy je przenieść do innych VLAN-ów.
- Wszystkie nieużywane porty przełącznika znajdują się w VLAN 1 i są aktywne. Nieużywane porty przełącznika powinny zostać wyłączone i przeniesione do nieużywanego VLAN-u.
- OSPF jest aktywne na interfejsach LAN. Pasywne interfejsy zmniejszą niepotrzebny ruch sieciowy.
- VLAN 99 jest utworzony tylko na SW-B2. Nie jest używany, nie ma nazwy i powinien zostać usunięty.
- Routera buforującego ma ustawione polecenie `ip default-gateway`, a adres IP to jego własny adres.

| Device   | Interface | Device Type | IP Address    | Subnet Mask     | Default Gateway |
| -------- | --------- | ----------- | ------------- | --------------- | --------------- |
| PC1      | NIC       | Host        | 192.168.1.153 | 255.255.255.0   | 192.168.1.1     |
| PC2      | NIC       | Host        | 192.168.3.50  | 255.255.255.0   | 192.168.3.1     |
| PC3      | NIC       | Host        | 192.168.4.115 | 255.255.255.0   | 192.168.4.1     |
| PC4      | NIC       | Host        | 192.168.5.83  | 255.255.255.128 | 192.168.5.1     |
| PC5      | NIC       | Host        | 192.168.5.227 | 255.255.255.128 | 192.168.5.129   |
| PC6      | NIC       | Host        | 192.168.2.48  | 255.255.255.224 | 192.168.2.33    |
| PC7      | NIC       | Host        | 192.168.2.67  | 255.255.255.224 | 192.168.2.65    |
| Hub      | G0/0/0    | Router      | 192.0.2.1     | 255.255.255.252 | N/A             |
| Hub      | S0/1/0    | Router      | 192.168.0.1   | 255.255.255.252 | N/A             |
| Hub      | S0/1/1    | Router      | 192.168.0.5   | 255.255.255.252 | N/A             |
| Hub      | S0/2/0    | Router      | 192.168.0.9   | 255.255.255.252 | N/A             |
| Hub      | S0/2/1    | Router      | 192.168.0.13  | 255.255.255.252 | N/A             |
| Branch-1 | G0/0/0    | Router      | 192.168.1.1   | 255.255.255.0   | N/A             |
| Branch-1 | S0/1/0    | Router      | 192.168.0.2   | 255.255.255.252 | N/A             |
| Branch-2 | G0/0/0    | Router      | 192.168.2.33  | 255.255.255.224 | N/A             |
| Branch-2 | S0/1/0    | Router      | 192.168.0.6   | 255.255.255.252 | N/A             |
| Factory  | G0/0/0    | Router      | 192.168.3.1   | 255.255.255.0   | N/A             |
| Factory  | G0/0/1    | Router      | 192.168.4.1   | 255.255.255.0   | N/A             |
| Factory  | S0/1/0    | Router      | 192.168.0.14  | 255.255.255.252 | N/A             |
| HQ       | G0/0/0.1  | Router      | 192.168.6.1   | 255.255.255.0   | N/A             |
| HQ       | G0/0/0.5  | Router      | 192.168.5.1   | 255.255.255.128 | N/A             |
| HQ       | G0/0/0.10 | Router      | 192.168.5.128 | 255.255.255.128 | N/A             |
| HQ       | S0/1/0    | Router      | 192.168.0.10  | 255.255.255.252 | N/A             |
| SW-B1    | VLAN 1    | Switch      | 192.168.1.252 | 255.255.255.0   | 192.168.1.1     |
| SW-B2    | VLAN 1    | Switch      | 192.168.2.62  | 255.255.255.0   | 192.168.2.1     |
| SW-F1    | VLAN 1    | Switch      | 192.168.3.252 | 255.255.255.0   | 192.168.3.1     |
| SW-F2    | VLAN 1    | Switch      | 192.168.4.252 | 255.255.255.0   | 192.168.4.1     |
| SW-HQ1   | VLAN 1    | Switch      | 192.168.6.252 | 255.255.255.0   | 192.168.6.1     |
| SW-HQ2   | VLAN 1    | Switch      | 192.168.6.253 | 255.255.255.0   | 192.168.6.1     |
| SW-HQ3   | VLAN 1    | Switch      | 192.168.6.254 | 255.255.255.0   | 192.168.6.1     |
