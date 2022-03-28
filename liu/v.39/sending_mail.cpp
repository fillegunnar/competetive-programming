#include <iostream>
#include <vector>
#include <unordered_map>
#include <limits>
#define MVI unordered_map<int, vector<int[2]>>

using namespace std;

string dijkstras(int n, int m, int s, int t, MVI nodes, int c){
    if (m == 0) return "Case #" + to_string(c) + ": unreachable";
    int distance[n];
    for (int i = 0; i < n; i++) distance[i] = numeric_limits<int>::max();
    distance[s] = 0;
    vector<int> prioQueue;
    prioQueue.push_back(s);
    while (!prioQueue.empty()){
        int min = numeric_limits<int>::max();
        int cn, index;
        for (int i = 0; i < prioQueue.size(); i++){
            if (distance[prioQueue[i]] < min){
                cn = prioQueue[i];
                index = i;
                min = distance[prioQueue[i]];
            }
        }
        prioQueue.erase(prioQueue.begin()+index);
        if (cn == t) return "Case #" + to_string(c) + ": " + to_string(distance[cn]);
        for (int i = 0; i < nodes[cn]; i++)
        {
            /* code */
        }
        
    }
    return "Case #" + to_string(c) + ": unreachable";
}

int main(){
    int N, n, m, s, t, n1, n2, w;
    cin >> N;
    for (int c = 0; c < N; c++)
    {
        cin >> n >> m >> s >> t;
        MVI nodes;
        for (int i = 0; i < n; i++) nodes[i] = vector<int[2]>;
        
        for (int i = 0; i < m; i++)
        {
            cin >> n1 >> n2 >> w;
            nodes[n1].push_back({n2, w});
            nodes[n2].push_back({n1, w});
        }
        cout << dijkstras(n, m, s, t, nodes, c) << endl;
    }
    return 0;
}