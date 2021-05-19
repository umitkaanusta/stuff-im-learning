from collections import defaultdict
import bisect

class TweetCounts:
    # idea: use the least memory space
    # so keep tweets in a dict to not repeatedly keep same tweet names
    # (defaultdict chosen to avoid KeyErrors if the tweet name is non-existent)
    # keep the list of "times" sorted to have less iterations

    def __init__(self):
        self.tweets = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)
        
    
    @staticmethod
    def secondsToBiggerUnits(incr: int, startTime: int, currTime: int) -> int:
        return (currTime - startTime) // incr
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freqs = {"minute": 60, "hour": 3600, "day": 86400}
        incr = freqs[freq]
        tweets = self.tweets[tweetName]
        counts = [0] * (self.secondsToBiggerUnits(incr, startTime, endTime) + 1)
        i = bisect.bisect_left(tweets, startTime)
        end = bisect.bisect_right(tweets, endTime)
        while i < end:
            idx = self.secondsToBiggerUnits(incr, startTime, tweets[i])
            counts[idx] += 1
            i += 1
        return counts
