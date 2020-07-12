#include<stdio.h>

int main()
{
    int s, r, l1, l2;
    printf("Enter S, R seperated by space : ");
    scanf("%d %d", &s, &r);
    // printf("%d", s);
    int arr[s];
    int ans[r];
    printf("Enter Samples space seperated : ");
    for(int i=0; i<s; i++)
        scanf("%d", &arr[i]);
    for(int j=0; j<r; j++)
        scanf("%d %d", l1, l2);
        int count=0;
        for(int k=0; k<s; k++)
        {
            if(arr[k]>=l1 && arr[k]<=l2)
            {
                count = count + 1;
            }
        }
        ans[r] = count;
        printf("%d  ", count);
    return 0;
}