#include <iostream>
#include <unordered_map>
#include <vector>
#include <stack>
#include <algorithm> // find
#define umivi unordered_map<int, vector<int>>

using namespace std;

int n, m, v, w, p;
umivi streets;
vector<vector<int>> noDirectWayBack;

bool dfs(){
    if(streets.find(v) == streets.end()) return false;
    stack<int> theStack;
    int discovered[n] = {0};
    int numOfDisc = 0;
    theStack.push(v);
    cout << v << w << endl;
    while(!theStack.empty()){
        v = theStack.top(); theStack.pop();
        if (v == w) return true;
        discovered[numOfDisc++] = v;
        for (int i = 0; i < streets[v].size(); i++)
        {
            p = streets[v][i];
            if (find(discovered, discovered+n, p) == discovered+n){
                // Not discovered, add to stack
                theStack.push(p);
            }
        }
    }
    return find(discovered, discovered+n, 0) == discovered+n;
}

bool check(){
    // Check whole graph
    w = 0;
    if (!dfs()) return false;
    // Check from critical points the we can get back
    for (int i = 0; i < noDirectWayBack.size(); i++)
    {
        v = noDirectWayBack[i][0];
        w = noDirectWayBack[i][1];
        if (!dfs()) return false;  
    }
    return true;
}

int main(){ 
    while (true){
        cin >> n >> m;
        if (n == 0 && m == 0) break;
        streets.clear(); noDirectWayBack.clear();
        for (int i = 0; i < m; i++)
        {
            cin >> v >> w >> p;
            streets[v].push_back(w);
            if (p==2) streets[w].push_back(v);
            else noDirectWayBack.push_back({w, v});
        }
        cout << check() << endl;
        // check();
    }
    return 0;
}