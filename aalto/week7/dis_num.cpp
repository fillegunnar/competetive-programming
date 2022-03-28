#include<bits/stdc++.h>
using namespace std;

int main(){
    unsigned long long n;
    cin >> n;
    unsigned long long vals[n];
    vector<bool> unique(1000000001, true);

    for (unsigned long long i = 0; i < n; i++){
        cin >> vals[i];
    }
    unsigned long long nUnique = 0;
    for (unsigned long long i = 0; i < n; i++)
    {
        if (unique[vals[i]]){
            unique[vals[i]] = false;
            nUnique++;
        }   
    }
    cout << nUnique << endl;
    return 0;
}