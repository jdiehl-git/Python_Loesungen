#A5 bubble sort in-place
def bubble_sort(self):
    i = 0
    while i < len(self) - 1:
        s = 0
        while s < len(self) - 1: 
            if self[s] > self[s + 1]:
                self[s],self[s + 1] = self[s + 1],self[s]
            s += 1
        i += 1
    print(self)