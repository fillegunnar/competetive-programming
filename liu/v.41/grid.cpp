#include <iostream>
#include <stack>

using namespace std;

char gf[3][3];
bool vis[3][3];

// Fattar verkligen inte problemet av nån anledning

int dfs(int i, int j){
    stack<int> next;
    int count = -1;
    next.push(i);
    next.push(j);
    while (true){
        if (next.empty()) return count;
        count++;
        int x, y;
        x = next.top();
        next.pop();
        y = next.top();
        // cout << x << y << endl;
        next.pop();
        gf[x][y] = '0';
        bool found = false;
        if (x>0 && gf[x-1][y] == '1' && !vis[x-1][y]){
            next.push(x-1);
            next.push(y);
            vis[x-1][y] = true;
        } 
        if (y>0 && gf[x][y-1] == '1' && !vis[x][y-1]){
            next.push(x);
            next.push(y-1);
            vis[x][y-1] = true;
        } 
        if (x<2 && gf[x+1][y] == '1' && !vis[x+1][y]){
            next.push(x+1);
            next.push(y);
            vis[x+1][y] = true;
        } 
        if (y<2 && gf[x][y+1] == '1' && !vis[x][y+1]){
            next.push(x);
            next.push(y+1);
            vis[x][y+1] = true;
        }
    }
}

void solve(){
    for (int i = 0; i < 3; i++){
        string temp;
        cin >> temp;
        for (int j = 0; j < 3; j++){
            gf[i][j] = temp[j];
            vis[i][j] = false;
        }
    }
    int max = -1;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (gf[i][j] == '1'){
                int temp = dfs(i, j);
                if (temp > max) max = temp;
            }
        }
    }
    cout << max << endl;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        solve();
    }
    
}

// int recSolve(int i, int j){
//     if (i<0 || i>2 || j<0 || j>2) return 0;
//     if (gf[i][j] == '0') return 0;
//     int max = 1;
//     int temp = 1+recSolve(i-1, j);
//     if (max<temp) max = temp;
//     temp = 1+recSolve(i+1, j);
//     if (max<temp) max = temp;
//     temp = 1+recSolve(i, j-1);
//     if (max<temp) max = temp;
//     temp = 1+recSolve(i, j+1);
//     if (max<temp) max = temp;

//     return max;
// }

// void solve(){
//     for (int i = 0; i < 3; i++)
//     {
//         string temp;
//         cin >> temp;
//         for (int j = 0; j < 3; j++)
//         {
//             gf[i][j] = temp[j];
//         }
//     }
//     int max = -1;
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             cout << gf[i][j];
//             if (gf[i][j] == '1')
//             {
//                 int temp = recSolve(i, j);
//                 if (temp>max) max = temp;
//             }
//         }
//         cout << endl;
//     }
//     cout << max << endl;
// }

// int main(){
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++)
//     {
//         solve();
//     }
//     return 0;
// }