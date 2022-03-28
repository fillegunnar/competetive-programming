#include <iostream>
using namespace std;

int main(){
    int n;
    int water = 0;
    int last_big = 0;
    cin >> n;
    int walls [n];
    int possible [n];
    for (int i = 0; i < n; i++)
    {
        cin >> walls[i];
        possible[i] = last_big;
        if (walls[i] > last_big){
            last_big = walls[i];
        }
    }
    last_big = 0;
    for (int i = n-1; i >= 0; i--)
    {
        if (possible[i] > last_big){
            possible[i] = last_big;
        }
        water += max(walls[i], possible[i]);
        if (walls[i] > last_big){
            last_big = walls[i];
        }
    }
    cout << water << endl;
    return 0;
}