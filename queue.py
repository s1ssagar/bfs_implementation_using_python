class Queue:
    def __init__(self):
        self.arr = [-1,]
    def queue(self, value):
        self.arr.insert(0,value)
    def dequeue(self):
        if self.arr[0] == -1:
            print "Fuck off empty Queue"
        else:
            del self.arr[-2]
    def get_item(self):
        if self.arr[0] != -1:
            return self.arr[-2]
        else:
            return "Empty Queue"
    def show_queue(self):
        return self.arr[:-1]
    def clear_queue(self):
        self.arr = []