def maxArea(height):
    max_val = 0
    current = 0

    p_j = 0
    p_i = 0
    j = len(height) - 1
    i = 0

    while (i < j and i >= 0 and j < len(height)):
        if (height[i] < height[j]):
            p_i = i

            current = height[i] * (j - i)
            if (current > max_val):
                max_val = current

            while (p_i < j and height[p_i] <= height[i]):
                p_i += 1
            i = p_i
            
        elif (height[j] < height[i]):
            p_j = j

            current = height[j] * (j - i)
            if (current > max_val):
                max_val = current
            
            while (i < j and height[p_j] <= height[j]):
                p_j -= 1
            j = p_j
        
        elif (height[i] == height[j]):
            p_i = i
            p_j = j

            current = height[i] * (j - i)
            if (current > max_val):
                max_val = current

            while (p_i < p_j):
                if (height[p_i] > height[p_j]):
                    p_j = j
                    break
                if (height[p_j] > height[p_i]):
                    p_i = i
                    break
                if (height[p_i] == height[p_j] and height[p_j] != height[j]):
                    break

                p_i += 1
                p_j -= 1
            
            i = p_i
            j = p_j

    return max_val
