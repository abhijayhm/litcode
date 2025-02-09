# Insert Interval

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the ith interval, and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and intervals still do not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Note that you don't need to modify `intervals` in-place. You can make a new array and return it.

### Example:

**Input:**

intervals = [[1, 3], [6, 9]], newInterval = [2, 5]

**Output:**

[[1, 5], [6, 9]]

**Explanation:**

- The new interval `[2, 5]` merges with the first interval `[1, 3]`, resulting in `[1, 5]`.
- The second interval `[6, 9]` remains unchanged.

---

*Was too burnt out atp, very suboptimal solution 😵‍💫*

[ChatGPT Solution Link](https://chatgpt.com/share/67a8e3a7-2ae4-8012-8e75-ad16397e9014)
