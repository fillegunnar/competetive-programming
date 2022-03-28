#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()



int main(){
    int t;

    cin >> t;

    long long seq[t][6];
    for (int i = 0; i < t; i++)
    {
        cin>>seq[i][0]>>seq[i][1]>>seq[i][2]>>seq[i][3]
        >>seq[i][4]>>seq[i][5];
    }

    for (int i = 0; i < t; i++)
    {
        P p1 = {seq[i][0], seq[i][1]};
        P p2 = {seq[i][2], seq[i][3]};
        P p3 = {seq[i][4], seq[i][5]};
        long long c = (conj(p3-p1)*(p3-p2)).Y;

        if (c>0) cout << "LEFT" << endl;
        else if (c<0) cout << "RIGHT" << endl;
        else cout << "TOUCH" << endl;
    }
    
    
    return 0;
}