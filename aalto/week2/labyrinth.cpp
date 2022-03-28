#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;

int main(){
    int h, w;
    cin >> h >> w;
    int start [2];
    char map [h][w];
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 'A'){
                start[0] = i;
                start[1] = j;
                // cout << i <<" "<< j << endl;
            }
        }
    }

    queue<int[2]> fifo;
    fifo.push(start);
    vector<string> paths;
    paths.insert(0, "");
    vector<int[2]> discovered;
    bool found = false;
    while (!fifo.empty())
    {
        int cur[2] = {fifo.front()[0], fifo.front()[1]};
        fifo.pop();
        discovered.push_back(cur);
        string path = paths[0];
        paths
    }
}