# Day 21: Classes and Objects
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
        self.n = len(data)

    def count(self): return self.n
    def sum(self): return sum(self.data)
    def min(self): return self.data[0]
    def max(self): return self.data[-1]
    def range(self): return self.max() - self.min()
    def mean(self): return round(self.sum() / self.n)

    def median(self):
        mid = self.n // 2
        if self.n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        counts = Counter(self.data)
        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        return (modes[0], max_count)

    def var(self):
        mu = self.mean()
        return round(sum((x - mu) ** 2 for x in self.data) / self.n, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        counts = Counter(self.data)
        return sorted([(round((v/self.n)*100, 1), k) for k, v in counts.items()], reverse=True)

    def describe(self):
        return (f"Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\nMax: {self.max()}\n"
                f"Range: {self.range()}\nMean: {self.mean()}\nMedian: {self.median()}\n"
                f"Mode: {self.mode()}\nVariance: {self.var()}\nStandard Deviation: {self.std()}\n"
                f"Frequency Distribution: {self.freq_dist()}")

# Test datası
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())
class PersonAccount:
    def __init__(self, fn, ln): self.fn, self.ln, self.incomes, self.expenses = fn, ln, {}, {}
    def add_income(self, desc, amt): self.incomes[desc] = amt
    def add_expense(self, desc, amt): self.expenses[desc] = amt
    def total_income(self): return sum(self.incomes.values())
    def total_expense(self): return sum(self.expenses.values())
    def account_balance(self): return self.total_income() - self.total_expense()
    def account_info(self): return f"Owner: {self.fn} {self.ln}\nBalance: {self.account_balance()}"
