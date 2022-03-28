#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()

bool compare(P a, P b){
    if(a.X == b.X) return a.Y < b.Y;
    return a.X < b.X;
}


int main(){
    int n;
    cin >> n;
    vector<P> vec(n);
    for (int i = 0; i < n; i++)
    {
        long long x, y;
        cin >> x >> y;
        vec[i] = {x,y};
    }

    sort(vec.begin(), vec.end(), compare);
    
    // Upper hull
    vector<P> uh;
    uh.push_back(vec[0]);
    uh.push_back(vec[1]);
    int i = 2;
    while (i<n)
    {
        P p1 = uh[uh.size()-2];
        P p2 = uh[uh.size()-1];
        P p3 = vec[i];
        long long c = (conj(p3-p1)*(p3-p2)).Y;
        if (c<=0){
            uh.push_back(p3);
            i++;
        }
        else if (uh.size() > 2) uh.pop_back();
        else {
            uh[1] = p3;
            i++;
        }
    }

    // Upper hull
    vector<P> lh;
    lh.push_back(vec[n-1]);
    lh.push_back(vec[n-2]);
    i = n-3;
    while (i>=0)
    {
        P p1 = lh[lh.size()-2];
        P p2 = lh[lh.size()-1];
        P p3 = vec[i];
        long long c = (conj(p3-p1)*(p3-p2)).Y;
        if (c<=0){
            lh.push_back(p3);
            i--;
        }
        else if (lh.size() > 2) lh.pop_back();
        else {
            lh[1] = p3;
            i--;
        }
    }
    vector<P> ch;
    for (int i = 0; i < uh.size()-1; i++)
    {
        ch.push_back(uh[i]);
    }
    for (int i = 0; i < lh.size()-1; i++)
    {
        ch.push_back(lh[i]);
    }
    
    cout << ch.size() << endl;
    for (int i = 0; i < ch.size(); i++)
    {
        cout << ch[i].X <<" "<< ch[i].Y << endl;
    }
}