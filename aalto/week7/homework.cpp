#include <iostream>
#include <math.h>
#include <map>

using namespace std;

void nAdd(){
    long long n = 450000000;
    long long add = 0;
    int add2 = 0;
    for (long long i = 0; i < n; i++){
        add += 3;
        // add2 = 3+3;
    }
    cout << add << endl;
}

void nMul(){
    long long n = 450000000;
    long long mul = 1;
    int mul2 = 0;
    for (long long i = 0; i < n; i++){
        mul *= 3;
        // mul2 = 3+3;
    }
    cout << mul << endl;
}

void nDiv(){
    long long n = 450000000;
    long long div = 9223372036854775807;
    int div2 = 0;
    for (long long i = 0; i < n; i++){
        div /= 2;
        // div2 = 3+3;
    }
    cout << div << endl;
}

map<int,int> nMap(){
    int n = 4000000;
    int j = 1;
    map<int,int> m;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        j = i+1; 
        m[i] = j;
        // if (i > 0) arr[i-1] = m[i-1];
    }
    return m;
}

void nFetch(map<int,int> m){
    int n = 4000000;
    for (int i = 0; i < n; i++)
    {
        m[i] = m[i]+1;
    }
    
}

int main(){
    // nAdd();
    // nMul();
    // nDiv();
    map<int,int> m = nMap();
    nFetch(m);

    return 0;
}