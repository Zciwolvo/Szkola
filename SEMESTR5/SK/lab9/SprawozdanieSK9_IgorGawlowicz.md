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
            <Rtext>27.04.2023</Rtext>
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
        <Rtext>9</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Badanie modeli TCP/IP i OSI w działaniu

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h2 >Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

1. Zbadaj ruch internetowy HTTP. \
   Pierwszym krokiem jest przełączenie do trybu symulacji, w którym czas zostanie zatrzymany a następne polecenia będą wysyłane w momencie w którym będziemy tego chcieli. \
   Dokładniej polecenia będą wysyłane wtedy kiedy naciśniemy przycisk następnego wydarzenia w panelu symulacji. W aktualnym zadaniu będą nas interesować tylko wydarzenia HTTP dlatego też właśnie je ustawimy w filtrach. \
   Aktualnie nasz panel wydarzeń jest pusty tak więc pobudzimy go wysyłając zapytanie do przeglądarki. Po wpisaniu adresu strony w przeglądarkę zobaczymy, że będziemy mogli przeklikać 4 wydarzenia. W zależności od tego na który z tych 4 wydarzeń spojrzymy zobaczymy warstwy informacji przychodzących lub wychodzących. Możemy zauważyć tutaj informacje takie jak nazwa protokołu, port źródła i celu, a także adres ip źródła i celu. Dodatkowo z zakładce PDU możemy zobaczyć wiele więcej różnych informacji.

2. Wyświetlenie elementów zestawu protokołów TCP/IP \
   Tym razem klikając na przycisk **Show All/None** możemy zobaczyć odpowiedzi serwera/klienta dotyczące także innych protokołów takich jak właśnie TCP/IP lub DNS \
   Po zbadaniu pierwszego sygnału typu DNS możemy zauważyć, że w 7 warstwie zawsze wyświetlany jest typ sygnału. W szczegółach PDU możemy też zauważyć, że w panelu DNS jest obecna rzeczywista nazwa strony jaką wpisaliśmy w przeglądarkę pokazuje to nam sposób działania protokołu DNS.

3. Wnioski \
   Symulowanie zdarzeń sieciowych w programie Cisco Packet Tracer może być niesamowicie przydatne przy nauce i eksperymentowaniu, a w porównaniu do programu WireShark program zapewnia nam o wiele więcej informacji zapisanych w czytelniejszy sposób.
