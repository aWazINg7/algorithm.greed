
def maxArea(height):
        i = len(height) - 1
        j = 0
        area = 0
        while j < i:
            if height[i] >= height[j]:
                temp = (i - j) * height[j]
                j += 1
            else:
                temp = (i - j) * height[i]
                i -= 1
            if temp > area:
                area = temp
        return area


in_put = input("height = ")
height = [int(n) for n in in_put.split(',')]

print(maxArea(height))

