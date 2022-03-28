#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;


int main(){
    ull n;
    cin >> n;
    ull vals[n];

    for (ull i = 0; i < n; i++)
    {
        cin >> vals[i];
    }

    vector<ull> seqMax;
    vector<ull> seqLen;
    seqMax.push_back(vals[0]);
    seqLen.push_back(1);
    for (ull i = 1; i < n; i++)
    {
        ull x = vals[i];
        ull bestOpt = 0;
        ull maxLenUnderX = 0;
        bool notBigger = true;
        for (ull j = 0; j < seqMax.size(); j++)
        {
            if (x>seqMax[j] && seqLen[j]>maxLenUnderX){
                maxLenUnderX = seqLen[j];
                bestOpt = j;
            }
            if (x>seqMax[j]) notBigger = false;
        }
        if (maxLenUnderX == 0 && notBigger){
            seqMax.push_back(x);
            seqLen.push_back(1);
        }
        else{
            seqMax[bestOpt] = x;
            seqLen[bestOpt]++;
        }
    }
    ull ans = 0;
    for (ull i = 0; i < seqLen.size(); i++)
    {
        if (seqLen[i]>ans) ans = seqLen[i];
    }

    cout << ans << endl;

    return 0;
}