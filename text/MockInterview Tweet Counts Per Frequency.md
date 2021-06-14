https://leetcode.com/problems/tweet-counts-per-frequency/

据反馈，这是不久前 Twitter 考的原题。

如果 frequency 是 分钟，那么 `[0,60]` 需要分成两个 list 分别是 `[0,59]` 和 `[60, 60]`。
因此，根据 startTime 和 endTime 可以求出一共需要多少个 list。
```
res = [0] * ((endTime - startTime) // 60 + 1)
```

## 简单方法
```python
class TweetCounts:

    def __init__(self):
        self.tweetTime = collections.defaultdict(list)
        self.word2Second = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweetTime[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        res = [0] * ((endTime - startTime) // self.word2Second[freq] + 1)
        for t in self.tweetTime[tweetName]:
            if startTime <= t <= endTime:
                res[(t -  startTime) // self.word2Second[freq]] += 1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```

## Follow Up
如何节省存储资源？
