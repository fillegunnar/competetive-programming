#include<bits/stdc++.h>
using namespace std;
typedef long long C;
typedef complex<C> P;
#define X real()
#define Y imag()



int main(){
    long long n, m;
    cin >> n >> m;
    
    unordered_map<long long, vector<pair<long long, long long>>> nodes;
    
    for (long long i = 0; i < m; i++)
    {
        long long a, b, c;
        cin >> a >> b >> c;
        cout << b << endl; 
        if (nodes.find(b) == nodes.end()){
            vector<pair<long long, long long>> temp;
            nodes[b] = temp;
        }
        nodes[b].push_back(make_pair(c, a));
    }

    for (auto b : nodes[1]){
        cout << b.first << b.second << endl;
    }
    
    long long distance[n+1];
    bool processed[n];
    for (int i = 0; i < n+1; i++)
    {
        distance[i] = 10000000000; // 10^10
        processed[i] = false;
    }

    distance[1] = 0;
    
    priority_queue<pair<long long, long long>> pq;
    pq.push(make_pair(distance[1], 1));
    
    while (!pq.empty())
    {
        long long a = pq.top().second; pq.pop();
        if (processed[a]) continue;
        processed[a] = true;
        cout << a << endl;
        for (auto b : nodes[a]){
            long long nb = b.second, val = b.first;
            if (distance[a]+val < distance[nb]){
                distance[nb] = distance[a]+val;
                pq.push(make_pair(distance[nb], nb));
            }
        }
    }

    for (int i = 1; i < n+1; i++)
    {
        cout << distance[i] << " ";
    }
    
    return 0;
}