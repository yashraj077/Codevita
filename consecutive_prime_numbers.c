#include<stdio.h>
// Consecutive Prime Sum
int input()
{
    int num;
    printf("Enter number : ");
    scanf("%d", &num);
    return num;
}
int check_prime(int num)
{
    int temp=0;
    if(num>1)
    {
        for(int i=2; i<num; i++)
        {
            if(num%i==0)
            {
                temp = temp+1;
            }
        }
        if(temp==0)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}
int consecutive_prime(int num)
{
    int arr[20];
    int count = 0;
    for(int i=2; i<=num; i++)
    {
        while(count<=num)
        {
            if(check_prime(i)==1)
            {
                arr[count] = i;
                count = count + 1;
                // printf("%d  ", count);
                // printf("%d  ", arr[0]);
            }
            break;
        }
    }
    // printf("%d  ", count);
    int check=2;
    while(check<count)
    {
        // printf("inside while loop\n");
        int sum = 0;
        for(int i=0; i<check; i++)
        {
            sum = sum +arr[i];
        }

        for(int j=0; j<num; j++)
        {
            if(arr[j]==sum)
            {
                printf("%d  ", arr[j]);
                break;
            }
        }
        check = check + 1;
    }
}
int main()
{
    int num;
    num = input();
    consecutive_prime(num);
    return 0;
}