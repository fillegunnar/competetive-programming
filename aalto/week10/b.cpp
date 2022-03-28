#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()

bool compare(P a, P b){
    if (a[0].X == b[0].X)
    return a[0].X < b[0].X;
}

int main(){
    long long n;
    cin >> n;
    P lines[n][2];
    for (long long i = 0; i < n; i++){
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        lines[i][0] = {x1,y1};
        lines[i][1] = {x2,y2};
    }
    
    sort(lines, lines+n, compare);
    // for (long long i = 0; i < n*2; i+=2){
    //     P a, b;
    //     a = lines[i];
    //     b = lines[i+1];
    // }

    return 0;
}