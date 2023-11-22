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

<p align="center">
  <img src="./ubblogo.png" alt="ubb logo"/>
</p>

<h3 style="text-align:center"><b>Wydział budowy maszyn i informatyki</b></h3>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<h2 style="text-align:center; border: none;"><b>Architektura komputerów</b></h2>
<h3 style="text-align:center; border: none;">(Laboratorium №3)</h3>

**Temat ćwiczenia: Systemy kodowania liczb**

Data wykonania ćwiczenia: 22.11.2023

&nbsp;

&nbsp;

Igor Gawłowicz

<div style="page-break-after: always;"></div>

## Zadanie 1

Napisz program, który:
- przeliczy podaną przez użytkownika liczbę dziesiętną na jej odpowiednik w systemie binarnym, ósemkowym i szesnastkowym;
- obliczy sumę, różnicę, iloczyn w systemie dwójkowym. Funkcja powinna przyjmować dwa argumenty w postaci ciągów znaków (np. "1010" i "1101") i zwracać wynik również w postaci ciągu znaków;
- wczyta liczbę w systemie ósemkowym od użytkownika, przeliczy ją na system dziesiętny, a następnie wyświetli jej reprezentację binarną;
- który przeliczy podaną przez użytkownika liczbę szesnastkową na jej odpowiednik w systemie dziesiętnym i binarnym.

Zaczniemy od przeliczania liczb na odpowiednie typy

Decimal -> Binary
```cpp
std::string decimalToBinary(int num) {
    std::string binary = "";
    if (num == 0) {
        binary = "0";
    } else {
        while (num > 0) {
            binary = (num % 2 == 0 ? "0" : "1") + binary;
            num /= 2;
        }
    }
    return binary;
}
```

Decimal -> Octal
```cpp
std::string decimalToOctal(int num) {
    std::string octal = "";
    if (num == 0) {
        octal = "0";
    } else {
        while (num > 0) {
            // Building the octal representation by appending the remainder of division by 8
            octal = std::to_string(num % 8) + octal;
            num /= 8;
        }
    }
    return octal;
}
```

Deciaml -> Hexadecimal
```cpp
std::string decimalToHexadecimal(int num) {
    std::string hex = "";
    if (num == 0) {
        hex = "0";
    } else {
        while (num > 0) {
            int remainder = num % 16;
            char digit;
            if (remainder < 10) {
                digit = '0' + remainder;
            } else {
                digit = 'A' + (remainder - 10);
            }
            hex = digit + hex;
            num /= 16;
        }
    }
    return hex;
}
```

Następnie w funkcji main możemy uruchomić nasz kod

```cpp
int main() {
    int number = 555;
    std::string binary = decimalToBinary(number);
    std::string octal = decimalToOctal(number);
    std::string hexadecimal = decimalToHexadecimal(number);
    
    std::cout << "Binary representation: " << binary << std::endl;
    std::cout << "Octal representation: " << octal << std::endl;
    std::cout << "Hexadecimal representation: " << hexadecimal << std::endl;

    return 0;
}
```

W wyniku dla liczby **555** otrzymamy
```cmd
Binary representation: 1000101011
Octal representation: 1053
Hexadecimal representation: 22B
```

Następnym krokiem będzie napisanie kalkulatora przyjmującego liczby binarne i zwracającego wynik także w liczbach binarnych

Dodawanie
```cpp
std::string binaryAddition(const std::string& bin1, const std::string& bin2) {
    int carry = 0;
    std::string result = "";
    int length = std::max(bin1.length(), bin2.length());

    for (int i = 0; i < length || carry; ++i) {
        int digit1 = (i < bin1.length()) ? bin1[bin1.length() - 1 - i] - '0' : 0;
        int digit2 = (i < bin2.length()) ? bin2[bin2.length() - 1 - i] - '0' : 0;
        int sum = digit1 + digit2 + carry;
        result = char(sum % 2 + '0') + result;
        carry = sum / 2;
    }
    return result;
}
```

Odejmowanie
```cpp
std::string binarySubtraction(const std::string& bin1, const std::string& bin2) {
    std::string result = "";
    int borrow = 0;
    int length = std::max(bin1.length(), bin2.length());

    for (int i = 0; i < length || borrow; ++i) {
        int digit1 = (i < bin1.length()) ? bin1[bin1.length() - 1 - i] - '0' : 0;
        int digit2 = (i < bin2.length()) ? bin2[bin2.length() - 1 - i] - '0' : 0;

        digit1 -= borrow;
        if (digit1 < 0) {
            digit1 += 2;
            borrow = 1;
        } else {
            borrow = 0;
        }

        int diff = digit1 - digit2;
        if (diff < 0) {
            diff += 2;
            borrow = 1;
        }

        result = char(diff % 2 + '0') + result;
    }

    while (result.length() > 1 && result[0] == '0') {
        result = result.substr(1);
    }

    return result;
}
```

Mnożenie
```cpp
std::string binaryMultiplication(const std::string& bin1, const std::string& bin2) {
    std::string result = "0";
    for (int i = bin2.length() - 1; i >= 0; --i) {
        if (bin2[i] == '1') {
            std::string temp = bin1;
            int padding = bin2.length() - i - 1;
            while (padding-- > 0) {
                temp += "0";
            }
            result = binaryAddition(result, temp);
        }
    }
    return result;
}
```

Następnie możemy sprawdzić wyniki w mainie

```cpp
int main() {
    int number = 555;
    int secondNumber = 777;
    std::string binary = decimalToBinary(number);
    std::string secondBinary = decimalToBinary(secondNumber);

    std::cout << "Binary addtion: " << binaryAddition(binary, secondBinary) << std::endl;
    
    std::cout << "Binary Subtraction: " << binarySubtraction(secondBinary, binary) << std::endl;
    
    std::cout << "Binary Multiplication: " << binaryMultiplication(binary, secondBinary) << std::endl;

    return 0;
}
```

```cmd
Binary addtion: 10100110100
Binary Subtraction: 11011110
Binary Multiplication: 1101001010010000011
```

Następnym punktem jest konwersja z liczby ósemkowej do dziesiętnej a następnie do binarnej

Potrzebujemy do tego funkcji, która konwertuje z liczby oktalnej do dekagonalnej

```cpp
int octalToDecimal(const std::string& octal) {
    int decimal = 0;
    int power = 0;
    for (int i = octal.length() - 1; i >= 0; --i) {
        int digit = octal[i] - '0';
        decimal += digit * pow(8, power);
        ++power;
    }
    return decimal;
}
```

I teraz w mainie wywołamy utworzoną funkcję

```cpp
int main() {
    int number = 555;
    std::string octal = decimalToOctal(number);

    std::cout << "Octal: " << octal << std::endl;
    
    int decimal = octalToDecimal(octal);
    
    std::cout << "decimal " << decimal << std::endl;
    
    std::string binary = decimalToBinary(decimal);
    
    std::cout << "Binary: " << binary << std::endl;

    return 0;
}
```

Po czym otrzymamy następujące wynik
```cmd
Octal: 1053
decimal 555
Binary: 1000101011
```

