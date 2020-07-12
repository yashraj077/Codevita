#include<stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    int arr[a];
    for(int i=0; i<a; i++)
        scanf("%d", &arr[i]);
    int temp = 0;
    int temparr[a];
    for(int j=0; j<a; j++)
    {
        temp = temp + arr[j];
        temparr[j] = temp;
    }
    int sum = 0;
    for(int k=0; k<a; k++)
    {
        sum = sum + temparr[k];
    }
    printf("%d", (sum-1));
    return 0;
}
