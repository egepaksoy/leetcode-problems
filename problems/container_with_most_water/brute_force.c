int max_area(int *height, int heightSize)
{
    int max = 0;
    int currentVal = 0;

    for (int i = 0; i < heightSize - 1; i++)
    {
        for (int j = 0; j < heightSize; j++)
        {
            if (height[i] < height[j])
                currentVal = height[i] * (j - i);
            else
                currentVal = height[j] * (j - i);
                
            if (currentVal > max)
                max = currentVal;
        }
    }

    return max;
}
