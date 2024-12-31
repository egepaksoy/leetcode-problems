#include <stdio.h>


int max_area(int *height, int heightSize)
{
    int max = 0;
    int currentVal = 0;

    for (int i = 0; i < heightSize - 1; i++)
    {
        for (int j = 0; j < heightSize; j++)
        {
            if (height[i] < height[j])
                currentVal = heightSize[i] * (j - i);
            else
                currentVal = heightSize[j] * (j - i);
                
            if (currentVal > max)
                max = currentVal;
        }
    }

    return max;
}


void main(void)
{
    int *height = {1,8,6,2,5,4,8,3,7};
    int n = 9;

    int result = max_area(height, n);

    printf("%d", result);
}