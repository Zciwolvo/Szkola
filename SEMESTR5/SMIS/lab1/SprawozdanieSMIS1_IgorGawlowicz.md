<style>
h1, h4, h2 {
    border-bottom: 0;
    display:flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
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
<h1>Akademia Techniczno-Humanistyczna w Bielsku-Białej </h1>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<h1 style="text-align: center;"><b>LABORATORIUM</b></h1>
<h1 style="text-align:center"><b>Systemy Monitorowania i Sterowania</b></h1>

&nbsp;

&nbsp;

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 1</b></h3>
<h2 style="text-align:center; border: none;">Układy kombinacyjne</h2>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

GRUPA: 2B / SEMESTR: 5 / ROK: 3

Igor Gawłowicz / 59096

<div style="page-break-after: always;"></div>

### Zadanie L1.12

*Skrzyżowanie 2.*

Zaprojektować system sterowania światłami na sygnalizatorach w trybie pracy ręcznej. Przez
zmianę stanu jednego z czterech przełączników operator może ustawić kolejną fazę świateł.
Niewykorzystane ustawienia przełączników powinny włączyć tryb mrugania świateł żółtych.

<p align="center">
  <img src="./s2.png" alt="Sublime's custom image"/>
</p>

Takie zadanie rozwiążemy w sposób następujący:

- Zapoznamy się z grafiką reprezentującą 8 faz świateł które musimy uwzględnić
- Stworzymy siatkę zależności wyjść od wejść na podstawie faz
- Na podstawie schematu zrobimy siatkę wykorzystując metodę Karnaugha dla każdego wyjścia
- Rozpiszemy jeszcze wszystkie pozostałe 8 scenariuszy, które nie zostały uwzględnione w podanych fazach
- Na podstawie pozostałych scenariuszy stworzymy siatkę uwzględniającą każdy z nie uwzględnionych scenariuszy, która będzie odpowiadać za włączenie migających żółtych świateł.
- Na podstawie naszych siatek napiszemy skrócone wzory dla każdego wyjścia
- Przeniesiemy nasze wzory do schematu drabinkowego w odpowiednim programie.


<div style="page-break-after: always;"></div>

Kolejność faz świateł:

<p align="center">
  <img src="./s4.png" alt="Sublime's custom image"/>
</p>

<div style="page-break-after: always;"></div>

Na podstawie powyższych informacji wiemy że mamy 4 wejścia:

W1, W2, W3 i W4

oraz 20 wyjść, oznacza to więc że musimy przygotować siatkę zależności zmiennych wejściowych na wyjściowe:

<p align="center">
  <img src="./s3.png" alt="Sublime's custom image"/>
</p>

Na wyżej załączonym obrazie możemy zauważyć, że w tym przypadku jak i w większości przypadków taka siatka jest po prostu zbyt długa i zbyt skomplikowana żeby w taki sposób przedstawiać ją w programie. Rozwiążemy ten problem poprzez zastosowanie siatek Carnough dla każdej zmiennej wyjściowej.

Oraz aby rozwiązać problem dla każdej kombinacji wejść innej od podanych faz, rozwiążemy jeszcze jedną siatkę dla wszystkich innych opcji.

<p align="center">
  <img src="./c1.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c2.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c3.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c4.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c5.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c6.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c7.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c8.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c9.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c10.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c11.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c12.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c13.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c14.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c15.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c16.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c17.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c18.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c19.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c20.png" alt="Sublime's custom image"/>
</p>

<p align="center">
  <img src="./c21.png" alt="Sublime's custom image"/>
</p>

Kolejnym krokiem będzie przełożenie naszych wzorów do odpowiedniego programu, który zapisze nam nasze dane wejściowe dla urządzenia do formatu możliwego do odczytania przez program PAC. 

Dla przykładu, tak wygląda schemat drabinkowy dla S1_CZER

<p align="center">
  <img src="./s5.png" alt="Sublime's custom image"/>
</p>

### Wnioski

Nasz projekt systemu sterowania światłami na sygnalizatorach w trybie pracy ręcznej opiera się na analizie ośmiu faz świateł, a metoda Karnaugha pomaga w zoptymalizowaniu logicznych funkcji. Siatki Karnaugha ułatwiają reprezentację tych funkcji. Dodatkowo, stworzyliśmy schemat drabinkowy dla wszystkich innych scenariuszy, co sprawia, że nasze rozwiązanie jest elastyczne i efektywne. Dzięki temu projekt pozwala na sprawną kontrolę nad sygnalizacją świetlną, niezależnie od potrzeb operatora i pojawiających się sytuacji.