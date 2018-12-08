import random


class Quicksort:
    @staticmethod
    def quicksort(array):
        if len(array) > 0:
            x = random.randint(0, len(array) - 1)
            l = [item for item in array if item < array[x]]
            e = [item for item in array if item == array[x]]
            g = [item for item in array if item > array[x]]
            if l:
                l = Quicksort.quicksort(l)
            if g:
                g = Quicksort.quicksort(g)
            return list(l) + list(e) + list(g)


