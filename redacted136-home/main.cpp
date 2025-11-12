#include <iostream>
using namespace std;

int main() {
    int number;
    cin >> number;
    
    int hundred = number / 100;
    int tens =(number / 10) % 10; 
    int ones = number % 10;

    if (hundred == tens || hundred == ones || tens == ones) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}