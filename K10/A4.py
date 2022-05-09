#A4 selection sort in-place
def selection_sort_in_place(self):
    i = 0
    while i < len(self) - 1:
        s = 0
        lowest_element = self[0]
        index_of_lowest = 0
        while s < len(self) - i - 1:
            if lowest_element > self[s + 1]:
                lowest_element = self[s + 1]
                index_of_lowest = s + 1
            s += 1
        self.pop(index_of_lowest)
        self.append(lowest_element)
        i += 1
    self.append(self[0])
    self.pop(0)
    print(self)