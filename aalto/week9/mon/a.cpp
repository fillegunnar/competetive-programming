#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()



int main(){
    int n;
    cin >> n;
    P seq[n];
    for (int i = 0; i < n; i++)
    {
        long long x,y;
        cin>>x>>y;
        seq[i] = {x,y};
    }

    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (seq[i].X + seq[i].Y > k) k = seq[i].X + seq[i].Y;
    }
    cout << k << endl;
}