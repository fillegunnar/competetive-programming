// uva 10039
// Not finished. Not really structured everything and started late so will not get the points.
// Learned to use #define (finally) and unordered map, so definetly not a waste of time.

#include <iostream>
#include <vector>
#include <unordered_map>
#define VS vector<string>
#define VVS vector<VS>
#define MAPSVS unordered_map<string, VS>

using namespace std;

MAPSVS getTrains(int nTrains){
    MAPSVS trains;
    for (int i = 0; i < nTrains; i++)
    {
        int nStops;
        cin >> nStops;
        VS stops;
        for (int j = 0; j < nStops; j++)
        {
            string time;
            string city;
            cin >> time >> city;
            time.append(city);
            stops.push_back(time);
        }
        string start = stops[0].substr(4, stops[0].size()-1);
        trains[start] = stops;
    }
    return trains;
}

void handleScenario(){
    int nCities, nTrains;
    string startTime, startLocation, destination;
    cin >> nCities;
    string cities [nCities];
    for (int i = 0; i < nCities; i++){
        cin >> cities[i]; 
    }
    cin >> nTrains;
    MAPSVS trains = getTrains(nTrains);
    cin >> startTime >> startLocation >> destination;
    for (auto city : trains){
        cout << city.first << endl;
    }
}

int main() {
    int nScenarios;
    cin >> nScenarios;
    for (int i = 1; i <= nScenarios; i++){
        cout << "Scenario " << i << endl;
        handleScenario();
    }
    
    return 0;
}

    // for (int i = 0; i < nTrains; i++)
    // {
    //     cout << "Train" << i << ": ";
    //     for (int j = 0; j < trains[i].size(); j++)
    //     {
    //         cout << trains[i][j] << " ";
    //     }
    //     cout << endl;
    // }