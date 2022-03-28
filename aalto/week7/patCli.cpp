#include<bits/stdc++.h>
using namespace std;


int main(){
    int n, m, k;
    string patterns[n];
    vector<int> patGroups;
    for (int i = 0; i < n; i++)
    {
        cin >> patterns[i];
    }

    int patCli = 0;
    for (int i = 0; i < n; i++)
    {
        if (patterns[i].size() == 0) continue;
        int samePat = 1;
        string str1 = patterns[i];
        for (int j = i+1; j < n; j++)
        {
            string str2 = patterns[j];
            bool nb = true;
            for (int c = 0; c < m; c++)
            {
                if ((str1.at(c) == 'B' && str2.at(c) == 'A') ||
                    (str1.at(c) == 'A' && str2.at(c) == 'B'))
                    nb = false;
            }
            if (nb) {
                samePat++;
                patterns[j] == "";
            }
        }
        patterns[i] == "";
        if (samePat > k) patGroups.push_back(samePat);
    }
    for (int i = 0; i < patGroups.size(); i++)
    {
        cout << patGroups[i] << endl;
    }
    return 0;
}