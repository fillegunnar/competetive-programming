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
    
    long long area = 0;
    int j = n-1;
    for (int i = 0; i < n; i++)
    {
        area += (seq[i].X*seq[j].Y) - (seq[j].X*seq[i].Y);
        j = i;
    }
    cout << abs(area) << endl;
    
}