#include <iostream>
using namespace std;
int main() {
    int perm,area,wid,len;
    cin >> len >> wid;
    perm = (2*len) + (2*wid);
    area = len*wid;
    cout << perm << endl << area << endl;
    return 0;
}