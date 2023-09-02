class Vector:
    def __init__(self, data):
        self.data = []
        self.size = 0        
        for item in data:
            self.add(item)
    
    def push_back(self, item):
        if self.size == 0:
            self.data[0] = item
        else:
            self.data[self.size - 1] = item
        self.size += 1
    
    def push_front(self, item):
        if self.size == 0:
            self.data[0] = item
        else:
            for i in range(self.size - 1, 0, -1):
                self.data[i] = self.data[i - 1]
            self.data[0] = item
        self.size += 1

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError
        if index == self.size:
            self.push_back(item)
        else:
            for i in range(self.size - 1, index - 1, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = item
            self.size += 1
    
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
    