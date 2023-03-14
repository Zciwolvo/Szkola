<style>
h1,h2,h3,h4 {
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
            <Rtext>03.09.2023</Rtext>
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
        <Rtext>2B</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Narzędzia diagnostyczne protokołów TCP/IP

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h2 >Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

1. za pomocą narzędzia IPCONFIG uzyskać szczegółowe informacje o wszystkich działach połączeń sieciowych. \
   <div style="text-align:center"><b>(ipconfig /allcompartments /all).</b></div>

   - Wypełnij poniższą tabelę otrzymanymi danymi.
      <div style="text-align: right;">Tabela 1. Informacje o sieci dla sekcji</div>

     | Nazwa komputera | Podstawowy sufiks DNS | Typ węzła | Routing IP jest włączony | WINS Proxy jest włączony |
     | --------------- | --------------------- | --------- | ------------------------ | ------------------------ |
     | DESKTOP-6GVNM2J | None                  | Hybrid    | No                       | No                       |
     | D               | None                  | Hybrid    | No                       | No                       |

     &nbsp;

      <div style="text-align: right;">Tabela 2. Adapter Ethernet. Połączenie z siecią lokalną</div>

      <center>

     |                                         |                                 |
     | --------------------------------------- | ------------------------------- |
     | None                                    | Sufiks połączenia DNS           |
     | Intel(R) Ethernet Connection (7) I219-V | Opis                            |
     | 00-D8-61-D6-2B-93                       | Adres fizyczny                  |
     | Yes                                     | DHCP jest włączony              |
     | Yes                                     | Autoconfiguration jest włączony |
     | fe80::7050:a7f8:82fe:6e5e%13(Preferred) | Adres IPv6 kanału               |
     | 192.168.88.19(Preferred)                | Adres IPv4                      |
     | 255.255.255.0                           | Maska podsieci                  |
     | 192.168.88.1                            | Brama domyślna                  |
     | 192.168.88.1                            | DHCP server                     |
     | 100718689                               | IAID DHCPv6                     |
     | 192.168.88.1                            | Serwery DNS                     |
     | Enabled                                 | NetBIOS over TCP/IP             |
     |                                         | Ethernet Adapter                |
     |                                         | Opis                            |
     |                                         | Adres fizyczny                  |

      </center>
     <img src="zad1.png">

&nbsp;

1. Za pomocą narzędzia **IPCONFIG** pobierz zawartość pamięci podręcznej serwera DNS systemu operacyjnego i zapisać wyniki do pliku raportu displaydnsXX.txt.Zastąp znaki w nazwie pliku "XX" numerem podanym przez prowadzącego.

<div style="text-align:center"><b>(ipconfig /displaydns> D:nowak-displaydnsXX.txt).</b></div>

<div style="text-align: right;">Tabela 3.</div>

| No  | Adres serwera DNS (Przed wyczyszczeniem pamięci podręcznej DNS) | Adres serwera DNS (Powyczyszczeniem pamięci podręcznej DNS) |
| --- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| 1.  | sdc.student.ath.edu.pl                                          | NULL                                                        |
| 2.  | cache2-waw1.steamcontent.com                                    | NULL                                                        |
| 3.  | ext2-fra1.steamserver.net                                       | NULL                                                        |
| 4.  | ext1-fra2.steamserver.net                                       | NULL                                                        |

Po wyczyszczeniu pamięci podręcznej DNS komenda nie zwraca żadnych wyników.

2.5. Po zwolnieniu adresów IPv4 za pomocą polecenia **ipconfig /release** następuje rozłączenie komputera z siecią Wi-Fi. \
2.8. Po odnowieniu połączenia za pomocą polecenia **ipconfig /renew** komputer stwierdza brak możliwości odnowienia połączenia do sieci Ethernet ponieważ kabel nie jest podłączony do komputera po czym łączy się z siecią Wi-Fi. \

&nbsp;

1. Sprawdź, czy protokół TCP/IP jest prawidłowo skonfigurowany w systemie operacyjnym komputera lokalnego. W tym celu wpisz w wierszu poleceń adres loopback.
<div style="text-align:center"><b>(ping 127.0.0.1)</b></div>
<div align="center">
<img src="zad32.png">
</div>

3.3.

<div style="text-align:center"><b>(ping -t ask.com)</b></div>
<div align="center">
<img src="zad33.png">
</div>
3.4.
<div style="text-align:center"><b>(ping -a 146.75.122.114)</b></div>
<div align="center">
<img src="zad34.png">
</div>

3.5.
| Publiczny adres IP | Domena |
| --- | --- |
| 146.75.122.114 | ask.com |
