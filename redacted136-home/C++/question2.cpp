#include <iostream>
using namespace std;

int main() {
    int L;
    int sum;
    int counter;
    int divisor;
    cin >> L;
    while(sum<L){
        for(int i=2; i>0; i++){
            if (i/divisor==0)
            {
                //没思路了
                //找不到如何检测是否质数的算法
                cout << i << endl;
                break;
            }
            
        }
        counter++;
        sum+=counter;
    }
    return 0;
}
