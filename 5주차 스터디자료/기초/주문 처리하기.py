class Queue:

    def __init__(self) :
        self.myQueue = []

    def push(self, n) :
        self.myQueue.append(n)

    def pop(self) :
        if self.empty() == 1 :
            return
        
        del self.myQueue[0]

    def size(self) :
        return len(self.myQueue)

    def empty(self) :
        if self.size() == 0:
            return 1
        
        return 0

    def front(self) :
        if self.empty() == 1:
            return -1
        
        return self.myQueue[0]

    def back(self) :
        if self.empty() == 1:
            return -1
        
        return self.myQueue[-1]
         
class orderInfo:
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders):
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()
    
    if vipIndex == -1:
        return normalQueue
    
    if normalIndex == -1:
        return vipQueue
    
    if time < orders[normalIndex].time and time < orders[vipIndex].time:
    
        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue
    
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue
    
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue
    
    return vipQueue

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''
    
    result = []
    
    normalQueue = Queue()
    vipQueue = Queue()
    
    jobEndTime = 0
    curTime = -1
    
    for i in range(len(orders)):
        curTime = orders[i].time
        
        if orders[i].vip == 0 :
            normalQueue.push(i)
        else:
            vipQueue.push(i)
        
    while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1):
        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
        index = targetQueue.front()
        
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
            
        result.append(index + 1)
        targetQueue.pop()
            
    while not(normalQueue.empty() == 1 and vipQueue.empty() == 1):

        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
        index = targetQueue.front()
        
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
            
        result.append(index + 1)
            
        targetQueue.pop()
            
    
    return result
