class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key,[]).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        for k,v in self.data.items():
            if k==key:
            
                left = 0
                latest_value = ""
                latest_time = 0
                right = len(v)-1
                while left <= right:
                    mid = (left+right)//2
                    if v[mid][1] == timestamp:
                        return v[mid][0]
                    elif(v[mid][1] <= timestamp):
                        latest_time = v[mid][1]
                        latest_value = v[mid][0]
                        left=mid+1
                    elif(v[mid][1] > timestamp):
                        right=mid-1
                    
                return latest_value
                        
        return ""

        
