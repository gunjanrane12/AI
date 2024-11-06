def printJobScheduling(arr, t):
    n = len(arr)

    # Sort the jobs based on descending order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Initialize result slots and job sequence
    result = [False] * t
    job = ['-1'] * t

    # Iterate over the jobs to schedule them
    for i in range(len(arr)):
        # Find a free slot for this job (starting from its deadline)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # Print the job sequence
    print(job)


# Example job list [Job ID, Deadline, Profit]
arr = [[1, 2, 50], [2, 1, 10], [3, 3, 40], [4, 2, 60], [5, 1, 30], [6, 3, 20]]

print("Following is the maximum profit sequence of jobs:")
printJobScheduling(arr, 3)