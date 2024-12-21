#include <bits/stdc++.h>

using namespace std;

void selection_sort(int arr[], int size)
{
    for (int i = 0; i < (size - 1); i++)
    {
        int min_pos = i;
        for(int j = i + 1; j < size; j++){
            if(arr[j] < arr[min_pos]){
                min_pos = j;
            }
        }

        if(min_pos != i){
            int temp = arr[i];
            arr[i] = arr[min_pos];
            arr[min_pos] = temp;
        }
    }
}

int main()
{
    int size;
    cin >> size;

    int arr[size];

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
    
    selection_sort(arr, size);

    for(int i = 0; i < size; i++){
        cout << arr[i] << " ";
    }

    return 0;
}