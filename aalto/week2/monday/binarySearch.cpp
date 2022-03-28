#include <iostream>
using namespace std;

int binary_search(int* x, int* begin, int* end, int seq[]){
    int middle;
    while (true){
        middle = *begin + (*end-*begin)/2;
        if (seq[middle] == *x || middle == *end || middle == *begin) break;
        else if (seq[middle] < *x) *begin = middle;
        else *end = middle;
    }
    return middle;
}

int main() {
    int x, n, begin, end, middle;
    while (true){
        cin >> x;
        if (x == 0) break;
        cin >> n;
        int seq [n];
        for (int i = 0; i < n; i++)
        {
            cin >> seq[i];
        }

        int xRange [2];
        begin = 0;
        end = n;
        middle = binary_search(&x, &begin, &end, seq);
        if (seq[middle] == x){
            xRange[0] = middle;
            xRange[1] = middle;
            int temp = end;
            int temp2 = middle+1;
            while (seq[middle] == x && temp2 != middle){
                // cout << middle << endl;
                temp2 = middle;
                xRange[0] = middle;
                end = middle;
                middle = binary_search(&x, &begin, &end, seq);
            }
            end = temp;
            begin = xRange[1];
            middle = xRange[1];
            temp2 = middle+1;
            while (seq[middle] == x && temp2 != middle){
                temp2 = middle;
                xRange[1] = middle;
                begin = middle;
                middle = binary_search(&x, &begin, &end, seq);
            }

            int out = xRange[1]-xRange[0]+1;
            cout << out << endl;

        }else cout << 0 << endl;
    }
    return 0;
}
