class Stat:

    def __init__(self, lst = []):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __add__(self, other):
        new_lst = self.lst + other.lst
        return Stat(new_lst)

    def __contains__(self, value):
        if value in self.lst:
            return True
        else:
            return False

    def max(self):
        try:
            return max(self.lst)
        except:
            return 0.0

    def min(self):
        try:
            return min(self.lst)
        except:
            return 0.0

    def add(self, value):
        try:
            self.lst.append(value)
        except:
            pass

    def mean(self):
        try:
            return sum(self.lst) / len(self.lst)
        except:
            return 0.0

    def clear(self):
        try:
            return self.lst.clear()
        except:
            pass

    def sum(self):
        accum = 0
        for num in self.lst:
            accum += num
        return accum


s1 = Stat()
val = len(s1)
print(val)

val = s1.min()
print(val)

val = s1.max()
print(val)

val = s1.mean()
print(val)

print(3 in s1)

s1.add(3)
s1.add(4)
s1.add(5)
print(len(s1))

val = s1.min()
print(val)

val = s1.max()
print(val)

val = s1.mean()
print(val)

print(3 in s1)

print(6 in s1)

s2 = Stat([1, 2, 3])
print(len(s2))

print(s2.min())

print(s2.max())

print(s2.mean())

s3 = s1 + s2
print(len(s3))

print(s3.min())

print(s3.max())

print(3 in s3)

print(6 in s3)

val = s3.sum()
print(val)

print(s3.mean())

print(s3.clear())
print(len(s3))



