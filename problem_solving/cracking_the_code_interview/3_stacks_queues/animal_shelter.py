"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
"""
# [a b c d e f]
from typing import List


class Animal:
    def __init__(self, id_, dogcat):
        self.id = id_
        self.dogcat = dogcat

    def __str__(self):
        return f"Animal(id={self.id}, type={self.dogcat})"

    def __repr__(self):
        return f"Animal(id={self.id}, type={self.dogcat})"


class AnimalQueue:
    def __init__(self):
        self.q: List[Animal] = []
        self.cats: List[Animal] = []
        self.dogs: List[Animal] = []

    def enqueue(self, animal):
        self.q.append(animal)
        if animal.dogcat == "dog":
            self.dogs.append(animal)
        elif animal.dogcat == "cat":
            self.cats.append(animal)

    def _dequeue(self, arr, idx=0):
        if not arr:
            return False
        arr[idx] = None
        i = idx
        while i + 1 < len(arr):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        arr.pop()

    def dequeue_any(self):
        removed = self.q[0]
        if removed.dogcat == "dog":
            for idx, animal in enumerate(self.dogs):
                if animal.id == removed.id:
                    self.dequeue_dog(idx=idx)
        elif removed.dogcat == "cat":
            for idx, animal in enumerate(self.cats):
                if animal.id == removed.id:
                    self.dequeue_cat(idx=idx)
        return removed

    def dequeue_cat(self, idx=0):
        removed = self.cats[idx]
        for i, animal in enumerate(self.q):
            if animal.id == removed.id:
                self._dequeue(self.q, i)
        self._dequeue(self.cats, idx)
        return removed

    def dequeue_dog(self, idx=0):
        removed = self.dogs[idx]
        for i, animal in enumerate(self.q):
            if animal.id == removed.id:
                self._dequeue(self.q, i)
        self._dequeue(self.dogs, idx)
        return removed

    def __str__(self):
        return "All:  " + str(self.q) + "\nCats: " + str(self.cats) + "\nDogs: " + str(self.dogs)


def test_solution():
    shelter = AnimalQueue()
    shelter.enqueue(Animal(1, "cat"))
    shelter.enqueue(Animal(2, "cat"))
    shelter.enqueue(Animal(3, "dog"))
    shelter.enqueue(Animal(4, "dog"))
    shelter.enqueue(Animal(5, "cat"))

    shelter.dequeue_any()
    assert [animal.id for animal in shelter.q] == [2, 3, 4, 5]
    assert [animal.id for animal in shelter.cats] == [2, 5]
    assert [animal.id for animal in shelter.dogs] == [3, 4]

    shelter.dequeue_dog()
    assert [animal.id for animal in shelter.q] == [2, 4, 5]
    assert [animal.id for animal in shelter.cats] == [2, 5]
    assert [animal.id for animal in shelter.dogs] == [4]
    
    shelter.dequeue_cat()
    assert [animal.id for animal in shelter.q] == [4, 5]
    assert [animal.id for animal in shelter.cats] == [5]
    assert [animal.id for animal in shelter.dogs] == [4]


if __name__ == '__main__':
    test_solution()
