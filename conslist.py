import typing

class ConsNilList:
    pass

class Cons(ConsNilList):
    def __init__(self, value: int, next: ConsNilList):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Cons(' + str(self.value) + ', ' + str(self.next) + ')'
    
    def __len__(self) -> int:
        return 1 + len(self.next)

    def __eq__(self, other) -> bool:
        if type(other) == Nil:
            return False
        else:
            return self.value == other.value and self.next == other.next

    def append(self, value: int) -> ConsNilList:
        return Cons(self.value, self.next.append(value))

    def insert(self, value: int, index: int) -> ConsNilList:
        if index != 0:
            return Cons(self.value, self.next.insert(value, index - 1))
        else:
            return Cons(value, self)

    def remove(self, index: int) -> int:
        if index != 0:
            return Cons(self.value, self.next.remove(index - 1))
        else:
            return self.next
        pass

    def count(self, value: int) -> int:
        return int(self.value == value) + self.next.count(value)

    # merge sort
    def sort(self) -> ConsNilList:
        return self.__sort_helper__(len(self) // 2)

    def __sort_helper__(self, half: int) -> ConsNilList:
        if self.next == Nil():
            return self

        left, right = self.split(half)
        left = left.__sort_helper__(half // 2)
        right = right.__sort_helper__(half // 2 + 1)
        return left.__merge_sorted__(right)
        
    def __merge_sorted__(self, other: ConsNilList) -> ConsNilList:
        if other == Nil():
            return self

        if self.value < other.value:
            return Cons(self.value,  self.next.__merge_sorted__(other))
        else:
            return Cons(other.value, other.next.__merge_sorted__(self))
    
    def split(self, index: int) -> (ConsNilList, ConsNilList):
        if index == 0:
            return Nil(), self
        else:
            left, right = self.next.split(index - 1)
            return Cons(self.value, left), right

class Nil(ConsNilList):
    def __str__(self) -> str:
        return 'Nil'

    def __len__(self) -> int:
        return 0

    def __eq__(self, other) -> bool:
        return type(self) == type(other)

    def append(self, value) -> ConsNilList:
        return Cons(value, Nil())

    def insert(self, value: int, index: int) -> ConsNilList:
        return Cons(value, Nil())

    def remove(self, index: int) -> ConsNilList:
        return Nil()

    def count(self, value: int) -> int:
        return 0

    def sort(self) -> ConsNilList:
        return Nil()

    def __sort_helper__(self, half: int) -> ConsNilList:
        return Nil()

    def __merge_sorted__(self, other: ConsNilList) -> ConsNilList:
        return other

    def split(self, index: int) -> ConsNilList:
        return Nil(), Nil()
