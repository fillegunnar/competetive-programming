// N telling how many integers on the line
// Then all the integers come after that
// Ex N = 3, seq = 2 4 3 1
// 2 4 1 3, 2 1 4 3, 1 2 4 3, 1 2 3 4, is one way to solve it
// 2 3 4 1, 2 3 1 4, 2 1 3 4, 1 2 3 4, it will always be the same
// It is enough to count how many moves it is from its correct place
// 2 3 1, 2 1 3, 1 2 3
// 1 3 5 2 4, 1 3 2 5 4, 1 3 2 4 5, 1 2 3 4 5
// For every number, how many moves it needs to be moved and to the sum
// Remove the amount of number we will move from the sum
// add 1

#include <iostream>
using namespace std;

void merge(int seqCopy[], int begin, int middle, int end, int seq[], int* count){
    int i = begin;
    int j = middle;
    
    for (int k = begin; k < end; k++) {
        if (i < middle && (j >= end || seqCopy[i] <= seqCopy[j])){
            seq[k] = seqCopy[i];
            i++;
        }else{
            if (j < end) *count += middle - i; 
            seq[k] = seqCopy[j];
            j++;
        }
    }
    for (int k = begin; k < end; k++) {
        seqCopy[k] = seq[k];
    }
}


void mergeSort(int seq[], int begin, int end, int seqCopy[], int* count){
    if (end - begin <= 1) return; // We have only one element
    int middle = (end + begin) / 2;
    // Recursive sort
    mergeSort(seq, begin, middle, seqCopy, count);
    mergeSort(seq, middle, end, seqCopy, count);
    // Merge the results
    merge(seqCopy, begin, middle, end, seq, count);
}

int main() {
    int n, temp;
    cin >> n;
    while (n != 0){ 
        // Read values
        int seq [n];
        int seqCopy [n];
        for (int i = 0; i < n; i++) {
            cin >> temp;
            seq[i] = temp;
            seqCopy[i] = temp;
        }

        // Sort and decide winner
        int count = 0;
        mergeSort(seq, 0, n, seqCopy, &count);

        if (count % 2 == 0) cout << "Carlos" << endl;
        else cout << "Marcelo" << endl;
        cin >> n;
    }
    return 0;
}

// 3 2 1 -> 3 2 and 1 -> (3 and 2) and 1

// for (int i = 0; i < n; i++){
//     for (int j = i+1; j < n; j++){
//         if (seq[i]>seq[j]){
//             int temp = seq[i];
//             seq[i] = seq[j];
//             seq[j] = temp;
//             count++;
//         }
//     }
// }

// int main() {
//     int seq, n;
//     cin >> n;
//     while (n != 0){ 
//         int seq [n];
//         bool carlosWin = true;
//         for (int i = 0; i < n; i++){
//             cin >> seq[i];
//         }
//         while(true){
//             bool sortedSome = false;
//             for (int i = 1; i < n; i++){
//                 if (seq[i] < seq[i-1]){
//                     int temp = seq[i];
//                     seq[i] = seq[i-1];
//                     seq[i-1] = temp;
//                     carlosWin = !carlosWin;
//                     sortedSome = true;
//                 }
//             }
//             if (!sortedSome) break;
//         }
//         if (carlosWin) cout << "Carlos" << endl;
//         else cout << "Marcelo" << endl;
//         cin >> n;
//     }
//     return 0;
// }


// int main() {
//     int n, cur;
//     cin >> n;
//     while (n != 0){ 
//         int move = 0;
//         int sum = 0;
//         for (int i = 1; i <= n; i++){
//             cin >> cur;
//             if (cur == i) continue; //The number is at the right place

//             // We need to move the number
//             // sum += abs(cur - i);
//             move++;
//         }
//         // cout << sum << endl;
//         if (sum % 2 == 0) 
//             cout << "Carlos" << endl;
//         else cout << "Marcelo" << endl;
//         cin >> n;
//     }
//     return 0;
// }