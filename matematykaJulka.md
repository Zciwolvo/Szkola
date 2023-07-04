# 1. Oblicz pierwszą i drugą pochodną funkcji

## Kilka ważnych informacji przed liczeniem

Pochodną wykorzystujemy aby sprawdzić jak funkcja zmienia się w danym przedziale.

- pierwsza pochodna lub pochodna pierwszego stopnia mówi nam o monotoniczności funkcji czyli, w którym miejscu funkcja rośnie a, w którym maleje.
- druga pochodna lub pochodna drugiego stopnia mówi nam o krzywiźnie funkcji czyli, gdzie jest wypukła a gdzie wklęsła (co to znaczy, funckja jest wypukła lub wklęskła raczej nie musi cię obchodzić)

Jeśli chodzi o samo liczenie bardzo prosto sobie zapamiętać że liczenie pochodnej polega na cofnięciu każdego elementu funkcji o jedną potęgę w tył, czyli w najprostszych sytuacjach stosujemy:

$$ (x^n)' = nx^{n-1} $$

Czyli mnożymy naszą liczbę przez wartość naszej potęgi po czym odejmujemy od niej 1 i wstawiamy spowrotem na miejsce potęgi.

W wielu sytuacjach sprawa jest troszkę utrudniona dlatego mamy wiele różnych wzorów pomocnicznych do liczenia pochodnów, które wywodzą się z powyższego wzoru, ale żeby nie musieć tego przekształcać za każdym razem prościej skorzystać ze wzorów.

Jedną bardzo przydatną rzeczą jest także przepisywanie pierwiastków do postaci potęgi

$$ \sqrt x = x^{1 \over 2}$$

No i z tą więdzą możemy przejść do przykładów

### pierwszy przykład

$$ 2x^5 - { 4 \over x} + { 1 \over 3x^3}$$

### Pierwszy stopień

$$ 10x^4 - { -4 \over x^2} + x^2 $$

$$ 10x^4 $$
Ponieważ wykorzystaliśmy wcześniejszy wzór

Do
$$ { 4 \over x} $$
Wykorzystaliśmy wzór z listy oraz wiedzę że 
$$ {1 \over x} = x^{-1} $$

No i do
$$ { 1 \over 3x^3} $$
Ponownie użyliśmy naszej umiejętności do przekształacania wzorów aby zmienić tą postać na 
$$ {x^3 \over 3}' = {1 \over 3} _ {x^3}' = {1 \over 3} _ 3x^2 = x^2 $$

### Drugi stopień

$$ 40x^3 - { 4 \over x^3 } + 2x $$

W drugim stopniu zrobiliśmy dokładnie to samo co w pierwszym tylko tym razem przekształcaliśmy równanie pierwszego stopnia.

### drugi przykład

$$ 3x^2 + {{x-1} \over e^x} - {1 \over 4} $$

### pierwszy stopień

Zaczniemy od uproszczenia równania

$$ 3x^2 + {{(x-1)} \times e^{-x}} - {1 \over 4} $$

Następnie pierwszy i ostatni wyraz jesteśmy w stanie od razu wyliczyć problemem jest jednak środkowy gdzie mamy przypadek iloczynu w pochodnej, sposobem na rozwiązania takiego przypadku jest dodanie do siebie tego elementu najpierw po pochodnej z pierwszego wyrazu, a następnie po pochodnej z drugiego:

$$ ({{(x-1)} \times e^{-x}})' = (x-1)' \times e^{-x} + (x-1) \times (e^{-x})' $$
Kolejnym problemem jest prawa część tego równania gdyż wyciągamy pochodną po **x**, który jest potęgą liczby _e_,
aby rozwiązać taki problem musimy pomnożyć ten element przez pochodną z jego potęgi.

$$ e^{-x} + (x-1) \times (e^{-x}) \times ({-x})' $$

$$ e^{-x} + (x-1) \times (e^{-x}) \times 1 $$

$$ e^{-x} + (x-1) \times (e^{-x}) $$

Wynik końcowy możnaby w teorii jeszcze uprościć ale myślę, że jest to nie do końca wskazane z liczbą _e_.

### drugi stopień

Ponownie musimy wykorzystać operacje poznane na przykładzie z pierwszego stopnia.

$$ e^{-x} \times -x' + (x-1)' \times e^{-x} + (x-1) \times (e^{-x})' $$

$$ -e^{-x} + e^{-x} + (x-1) + e^{-x} \times -x' $$

$$ -e^{-x} + e^{-x} + (x-1) - e^{-x} $$

$$ -(x-1) \times e^{-x} $$

Przykład może wydawać się dość długi i trudny jednak tak naprawdę opiera się na dwóch prostych trickach przez co jest bardzo repetetywne.

### Trzeci przykład

$$ (3 - x)sin(x) $$

### Pierwszy stopień

Ponownie przykład z ilorazem także rozdzielamy go na sumę dwóch osobnych pochodnych.

$$ (3-x)' \times sin(x) + (3-x) \times sin(x)' $$
$$ -sin(x) + (3-x) \times cos(x) $$

### Drugi stopień

$$ -cos(x) + (3-x)' \times cos(x) + (3-x) \times cos(x)' $$
$$ -cos(x) + -cos(x) + (3-x) \times -sin(x) $$
$$ -2cos(x) + -(3-x) \times sin(x) $$

### Czwarty przykład

$$ ln(x^3 + 3) $$

### Pierwszy stopień

Przy logarytmach mamy kolejną zasadę o funkcjach wewnętrznych gdyż:

$$ ln(u(x))' = {1 \over u(x)} \times u(x)' $$

A teraz musimy podstawić ten wzór do przykładu:

$$ {1 \over {x^3 + 3}} \times (x^3 +3)' $$
$$ {1 \over {x^3 + 3}} \times 3x^2 $$
$$ {3x^2 \over {x^3 + 3}} $$

### Drugi stopień

W sytuacji takiej jak ta musimy wykorzystać kolejną regułę, kiedy w ułamku licznik i mianownik stanowią osobnę funkcję:

$$ {u(x) \over v(x)}' = {{u(x)' \times v(x) - u(x) \times v(x)'} \over v(x)^2 } $$

Czyli:

$$ {3x^2 \over {x^3 + 3}}' = {{{(3x^2)}' \times {(x^3 + 3)} - (3x^2) \times {(x^3 + 3)}'} \over ({x^3 + 3})^2 } $$

$$ {6x \times (x^3 + 3)-3x^2 \times 3x^2} \over {x^6 + 6x^3 + 9} $$

$$ 6x^4 + 18x - 9x^4 \over {x^6 + 6x^3 + 9} $$
$$ -3x^4 + 18x \over {x^6 + 6x^3 + 9} $$

### Piąty przykład

$$ e^{x^2-x+2} $$

### Pierwszy stopień

$$ e^{x^2-x+2} \times ({x^2-x+2})' $$

$$ e^{x^2-x+2} \times (2x - 1) $$

# 2. Wyznacz równania prostych stycznych do wykresów funkcji.

$$ f(x) = x^2 -x $$
i
$$ g(x) = ln(x^2 - 3x + 3) $$
W punkcie
x0 = 2

Prostą styczną do wykresu funkcji f(x) w punkcie x0 wyraża się wzorem:

$$ y = f(x0)' \times (x-x0) + f(x0) $$

Równanie prostej stycznej zapisane w postaci kierunkowej, to:

$$ y = f(x0)' \times x + b $$

gdzie

$$ b = f(x0) - f(x0)' \times x0 $$

Czyli teraz musimy wykorzystać te wzory w przykładach:

Liczymy pochodną z f(x)

$$ (x^2 -x)' = 2x - 1 $$

$$ f(x0)' = f(2)' = 2 \times 2 - 1 = 3 $$

$$ y = f(x0)' \times x + b $$

$$ y = 3x + b $$

Żeby obliczyć współczynnik b podstawimy do równania prostej stycznej współrzędne punktu (x0,f(x0)), który należy do tej prostej.

$$ f(x0) = f(2) = 4 - 2 = 2 $$

Czyli punkt (x0,y)=(2,2). Zatem podstawiamy:

$$ y = 3x + b $$

$$ 2 = 2 \times 2 + b $$

$$ b = -2 $$

Czyli nasze równanie ma postać:

$$ y = 3x - 2 $$

### Drugi przykład

$$ g(x) = ln(x^2 - 3x + 3) $$

$$ ln(x^2 - 3x + 3)' = $$

$$ {1 \over x^2 - 3x + 3} \times (x^2 - 3x + 3)' $$

$$ {1 \over x^2 - 3x + 3} \times 2x - 3 $$

$$ {2x - 3 \over x^2 - 3x + 3} $$

$$ g(x0)' = g(2)' = {2 \times 2 - 3 \over 2^2 - 3 \times 2 + 3} = {1 \over 1 } = 1 $$

$$ y = g(x0)' \times x + b $$

$$ y = x + b $$

$$ g(2) = ln(2^2 - 3 \times 2 + 3) = ln(1) = 0 $$

$$ $$

$$ (x0,y)=(2,0) $$

$$ 0 = 2 + b $$
$$ b = -2 $$

$$ y = x - 2 $$

# Wyznacz przedziały monotoniczności funkcji i ekstremum lokalne w przedziale.

### a)

$$ g(x) = x -5 \sqrt x $$

Aby dowiedzieć się w jakich przedziałach funkcja rośnie a w jakich maleje musimy policzyć pochodną tej funkcji.

$$ (x -5 \sqrt x)' = 1 - {5 \over 2 \sqrt x} $$

Aby policzyć pochodną z pierwiastka musimy pamiętać że
$$ \sqrt x = x^{1 \over2} $$
$$ (x^{1 \over2})' = x^{-1 \over 2} $$

Funkcja jest rosnąca wtedy gdy g(x)' > 0

$$ 1 - {5 \over 2 \sqrt x} > 0 $$

$$ - {5 \over 2 \sqrt x} = -1 $$
$$ -5 = -2 \sqrt x $$
$$ {5 \over 2} = \sqrt x $$
$$ {25 \over 4} = x $$

Funkcja jest rosnąca dla:
$$ x > {25 \over 4} $$
Funkcja jest malejąca dla:
$$ x < {25 \over 4} $$

### b)

Najpierw policzymy dziedzinę funkcji, czyli szukamy czegoś co sprawia, że równanie będzie niemożliwe do obliczenia w tym przypadku: x należy do <0, inf> ponieważ nie może być pierwiastka z liczby ujemnej bez uwzględnienia liczb zespolonych.

Następnie skorzystamy z pochodnej wyliczonej w podpunkcie _a_ na podstawie, której wiemy że skoro funkcja rośnie powyżej 25/4, a maleje poniżej tej wartości to wiemy że:

Minimum lokalne tej funkcji w przedziale <0,9> to 25/4 a maksimum lokalne to 9, ponieważ punkt 25/4 jest miejscem przegięcia, gdzie funkcja z malejącej zmienia się w rosnącą, 9 ponieważ funkcja rośnie już do końca więc oczywistym jest że u szczytu będzie miała największą wartość.

# 5. Wyliczając odpowiednie pierwsze i drugie pochodne ustal, w którym spośród punktów funkcja ma maksimum lokalne, a w którym punkt przegięcia.

$$ f(x) = x^4 + {1 \over 3}x^3 - 7x^2 $$

$$ (x^4 + {1 \over 3}x^3 - 7x^2)' = 4x^3 + x^2 - 14x $$

Do punktu przegięcia będziemy potrzebować pochodnej drugiego rzędu, którą następnie przyrównamy do 0 i obliczymy.

$$ (4x^3 + x^2 - 14x)' = 12x^2 + 2x - 14 $$

$$ 12x^2 + 2x - 14 = 0 $$

$$ b^2 - 4ac = \Delta $$

$$ \Delta = 4 - 784 $$
$$ \Delta < 0 $$
Oznacza brak rozwiązania dlatego musimy szukać dalej, następnie możemy spróbować przekształcić równanie do innej postaci

$$ 12x^2 + 2x - 14 = 2(6x^2 + x -7) = 2(x-1)(6x+7)$$
$$ (x-1) = 0 \ dla \ x = 1 $$
$$ (6x+7) = \ dla \ x = {-7 \over 6} $$

Czyli widzimy już, że punktem przegięcia spośród podanych w zadaniu jest 1

Wracając do ekstremum, obliczymy je z pochodnej pierwszego stopnia, przyrównując ją do 0.

$$ 4x^3 + x^2 - 14x = 0 $$
$$ x(4x^2 + x - 14) = 0 $$
$$ x(x+2)(4x-7) = 0 $$
Czyli nasze ekstremum jest w punkcie -2, 7/4 lub 0. 7/4 nie jest w puli potencjalnych rozwiązań więc pozostaje nam -2 lub 0 także pozostaje nam podstawić je do oryginalnej funkcji.

$$ f(-2) = -2^4 + {1 \over 3} \times -2^3 - 7 \times -2^2 = 16 + {-8 \over 3} - 28 = -14 {2 \over 3} $$

$$ f(0) = 0 $$

Na podstawie tego wiemy, że nasze maksimum lokalne jest w punkcie 0, a minimum lokalne w punkcie -2
