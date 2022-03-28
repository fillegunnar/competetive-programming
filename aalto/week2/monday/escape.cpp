#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>
#include <queue>
#include <algorithm>
#define VI vector<int>
#define VAI vector<array<int, 2>>
#define MPVI unordered_map<int, VAI>


using namespace std;

void read(int* n, int* m, int* x, int* y, MPVI* nodes){
    cin >> *n >> *m >> *x >> *y;
    for (int i = 0; i < *m; i++)
    {
        int a, b, w;
        cin >> a >> b >> w;
        (*nodes)[a].push_back({b, w});
        (*nodes)[b].push_back({a, w});
    }
}

void bfs(int n, int m, int x, int y, MPVI nodes){
    for (int i = 1; i <= n; i++)
    {
        int depth = 0;
        queue<int> fifo;
        fifo.push(i);
        VI discovered;
        bool escape = false;
        while (!fifo.empty()){
            int c = fifo.front();
            fifo.pop();
            discovered.push_back(c);
            for (int j = 0; j < nodes[c].size(); j++)
            {
                int neighbour = nodes[c][j][0];
                int width = nodes[c][j][1];
                vector<int>::iterator it;
                it = find (discovered.begin(), discovered.end(), neighbour);
                if (it != discovered.end() || width < x) continue;
                if (width < y){
                    escape = true;
                    break;
                }
                fifo.push(neighbour);
            }
            depth++;
            if (escape) break;
        }
        if (escape) cout << depth << endl;
        else cout << "-1" << endl;
    }
    
}

int main(){
    int n, m, x, y;
    MPVI nodes;
    read(&n, &m, &x, &y, &nodes);
    bfs(n, m, x, y, nodes);
    return 0;
}