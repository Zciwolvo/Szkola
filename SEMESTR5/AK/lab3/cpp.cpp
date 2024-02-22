#include <iostream>
#include <string>
#include <cmath>

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

std::string binarySubtraction(const std::string& bin1, const std::string& bin2) {
    // Function to perform binary subtraction
    std::string result = "";
    int borrow = 0;
    int length = std::max(bin1.length(), bin2.length());

    for (int i = 0; i < length || borrow; ++i) {
        int digit1 = (i < bin1.length()) ? bin1[bin1.length() - 1 - i] - '0' : 0;
        int digit2 = (i < bin2.length()) ? bin2[bin2.length() - 1 - i] - '0' : 0;

        // Adjust digit1 if borrow is set
        digit1 -= borrow;
        if (digit1 < 0) {
            digit1 += 2;
            borrow = 1;
        } else {
            borrow = 0;
        }

        // Perform subtraction
        int diff = digit1 - digit2;
        if (diff < 0) {
            diff += 2;
            borrow = 1;
        }

        result = char(diff % 2 + '0') + result;
    }

    // Remove leading zeroes
    while (result.length() > 1 && result[0] == '0') {
        result = result.substr(1);
    }

    return result;
}

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

int binaryToDecimal(const std::string& binary) {
    int decimal = 0;
    int power = 0;
    for (int i = binary.length() - 1; i >= 0; --i) {
        if (binary[i] == '1') {
            decimal += pow(2, power);
        }
        ++power;
    }
    return decimal;
}

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

int hexadecimalToDecimal(const std::string& hex) {
    int decimal = 0;
    int power = 0;
    for (int i = hex.length() - 1; i >= 0; --i) {
        int digit;
        if (hex[i] >= '0' && hex[i] <= '9') {
            digit = hex[i] - '0';
        } else if (hex[i] >= 'A' && hex[i] <= 'F') {
            digit = hex[i] - 'A' + 10;
        } else if (hex[i] >= 'a' && hex[i] <= 'f') {
            digit = hex[i] - 'a' + 10;
        }
        decimal += digit * pow(16, power);
        ++power;
    }
    return decimal;
}

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
