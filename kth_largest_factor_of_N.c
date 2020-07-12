#include<stdio.h>
// kth_largest_factor_of_N
int main()
{
    int n, k;
    printf("Enter N, k : ");
    scanf("%d %d", &n, &k);
    int arr[n];
    int count = 0;
    for(int i=0; i<n; i++)
    {
        while(count<n)
        {
            if(n%(i+1)==0)
            {
                arr[count]=(i+1);
                count = count + 1;
            }
            break;
            // else
            // {
            //     break;
            // }
        }
    }
    int farr[count];
    for(int j=0; j<count; j++)
    {
        int temp = arr[j];
        farr[j]=temp;
    }
    int length = sizeof(farr)/sizeof(farr[0]);
    printf("%d  ", length);
    printf("%d  ", farr[count-1]);
    return 0;
}