def next_higher_peak(heights):
    n = len(heights)
    result = [-1] * n
    st = []

    for i in range(n):
        while st and heights[i] > heights[st[-1]]:
            idx = st.pop()
            result[idx] = heights[i]
        st.append(i)

    return result

if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))

    result = next_higher_peak(heights)

    for height in result:
        print(height, end=" ")