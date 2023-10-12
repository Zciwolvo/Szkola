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
<h1>LABORATORIUM BEZPIECZEŃSTWO TECHNOLOGII INFORMATYCZNYCH</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>03.10.2023</Rtext>
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
        <Rtext>1</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Konfiguracja Fierwalla na komputerze z systemem Windows.

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Zainstaluj oprogramowanie Comodo Firewall na komputerze z systemem Windows.

Przechodzimy przez instalację i bez problemów uruchamia się nam wstępna konfiguracja.

![z1](z1.png)

## Stwórz reguły zapory ogniowej przy użyciu Comodo Firewall, które zezwolą na dostęp do wybranych aplikacji lub portów, a także reguły, które zablokują dostęp do niektórych z nich.

### Opis scenariusza

Publiczna sieć wi-fi zlokalizowana na dworcu kolejowym.

### Zagrożenia

- Podejrzane strony
- Nadmiar zużycia sieci

### Konfiguracja sieci

Aby upewnić się że użytkownik nie zainfekuje naszej sieci poprzez podejrzane źródła możemy uruchomić tryb bezpieczny naszej zapory sieciowej, który zapewni dostęp tylko dla połączeń zweryfikowanych przez zaporę COMODO.

![z2](z2.png)

Następnie możemy zabezpieczyć wszystkie porty, dzięki czemu użytkownicy sieci będą bezpieczniejsi i nie będzie się ich dało tak łatwo zidentyfikować.

![z3](z3.png)

Następnie aby ograniczyć użycie sieci zablokujemy dostęp do platform streamingowych typu Netflix, Prime itp.

![z4](z4.png)

Po próbie wczytania dowolnej z tych stron otrzymamy komunikat o problemie z połączeniem do servera

![z5](z5.png)

# Wnioski

Podczas konfiguracji Firewalla dla naszej publicznej sieci na dworcu kolejowym zdecydowaliśmy się na COMODO Firewall ze względu na jego zdolność do tworzenia niestandardowych reguł, co jest niezbędne do skutecznej ochrony przed nieautoryzowanym dostępem oraz umożliwienie kontroli nad ruchem internetowym.
