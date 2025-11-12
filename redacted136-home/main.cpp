#include <iostream>
using namespace std;

int main() {
    int number;
    
    // Get input from user
    cout << "Enter a three-digit number: ";
    cin >> number;
    
    // Extract individual digits
    int digit1 = number / 100;           // Hundreds place
    int digit2 = (number / 10) % 10;     // Tens place
    int digit3 = number % 10;            // Units place
    
    // Check if any digits repeat
    if (digit1 == digit2 || digit1 == digit3 || digit2 == digit3) {
        cout << number << " contains repeating digits." << endl;
    } else {
        cout << number << " does not contain repeating digits." << endl;
    }
    
    return 0;
}