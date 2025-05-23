# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from collections import Counter # count task frequencies
class Solution(object):
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks) # Count how many times each task appears

        max_freq = max(task_counts.values()) # find the max frequency among all tasks

        # count hiw many tasks have this maximum frequency | each time i found the max_freq -> +1 
        num_max_tasks = sum(1 for count in task_counts.values() if count == max_freq)
       
       # Calculate the minimum time using the formula:
        min_time = (max_freq - 1) * (n + 1) + num_max_tasks

       # the result is the larger of:
       # - total number of tasks (if there's no idle time)
       # - or calculated minimum time (if idle time is needed)
        return max(len(tasks),min_time)