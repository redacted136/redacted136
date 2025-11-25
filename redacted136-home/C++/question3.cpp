#include <iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    int loop;
    int result;
    vector<int> max_odd;
    vector<int> numbers;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> loop;
        numbers.push_back(loop);
    }
    
    for(int i=0; i<n;i++){
        for(int j=i+1; j<n;j++){
            result += numbers[i];
            if(result%2!=0){
                max_odd.push_back(result);
                cout << result << endl;
            }
        }
        
    }
    for(int num : max_odd){
        cout << num << endl;
    }
    return 0;
}