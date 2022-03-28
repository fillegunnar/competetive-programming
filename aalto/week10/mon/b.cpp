#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()



int main(){
    long long n, q;
    cin >> n >> q;

    vector<long long> arr(n);
    for (long long i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    long long quer[q][2];
    for (long long i = 0; i < q; i++)
    {
        cin >> quer[i][0] >> quer[i][1];
    }

    unordered_map<string, long long> mins; 

    long long i = 0;
    while(pow(2,i) <= n){
        for (long long j = 0; j < n; j++)
        {
            long long jj = j+pow(2,i)-1;
            if (jj < n) 
                mins[to_string(j)+to_string(jj)] = min_element(begin(arr), );
            else break;
        }
        i++;
    }
    for (long long i = 0; i < q; i++) 
    {
        long long a, b, l, k, ans;
        a = quer[i][0]-1;
        b = quer[i][1]-1;
        l = b-a+1;
        k = 0;
        while (pow(2,k)<=l) k++;
        k--;
        k = pow(2,k);
        ans = min(mins[to_string(a)+to_string(a+k-1)], mins[to_string(b-k+1)+to_string(b)]);
        cout << ans << endl;
    }
    
    return 0;
}