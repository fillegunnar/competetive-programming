#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()

// bool compare(P a, P b){
//     if (a[0].X == b[0].X)
//     return a[0].X < b[0].X;
// }

int main(){
    long long n, v, h;
    cin >> n;
    v = 0; h = 0;
    for (long long i = 0; i < n; i++){
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        if (x1 == x2) v++;
        else h++;
    }

    cout << v*h << endl;
    return 0;
}