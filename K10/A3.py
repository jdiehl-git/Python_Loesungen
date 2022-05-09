#A3 Selection sort out-of-place
def selection_sort_out_of_place(self):
    s = 0
    result = []
    self_copy = self.copy()
    while s < len(self) - 1:
        i = 0
        lowest_element = self_copy[0]
        index_of_lowest = 0
        while i < len(self_copy) - 1:
            if lowest_element > self_copy[i + 1]:
                lowest_element = self_copy[i + 1]
                index_of_lowest = i + 1
            i += 1
        self_copy.pop(index_of_lowest)
        result.append(lowest_element)
        s += 1
    result.append(self_copy[0])
    print(result)