# reviterator.py

class RevIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1 # len 은 그냥 숫자만 알려줘서 -1로 인덱스 번호로 만들어야 한다.

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
if __name__ == "__main__":
    i = RevIterator([1,2,3])
    for item in i :
        print(item)