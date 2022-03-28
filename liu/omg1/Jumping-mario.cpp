// T < 30 // Test cases
// 0 < N < 50 // Number of walls
// Next line is the height of the walls from left to right, not exceeding 10

#include <iostream>
using namespace std;

int main() {
    int t, n, currentWall, nextWall;
    string line;
    cin >> t;
    int i = 1;
    while(i <= t){ // Go through test by test
        cin >> n;
        int highJumps = 0;
        int lowJumps = 0;
        cin >> currentWall; // Read first wall
        for (int j = 0; j < n-1; j++){ // Look if we jump high or low to next walls
            cin >> nextWall;
            if (currentWall < nextWall) highJumps++;
            else if(currentWall > nextWall) lowJumps++;
            currentWall = nextWall;
        }
        cout<<"Case "<<i<<": "<<highJumps<<" "<<lowJumps<<endl;
        i++;
    }
    return 0;
}
