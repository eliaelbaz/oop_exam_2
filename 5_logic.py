# 1

class UniqueNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.seen_once = set()
        self.seen_more_than_once = set()

    def find_unique(self):
        for num in self.numbers:
            if num in self.seen_more_than_once:
                continue
            if num in self.seen_once:
                self.seen_once.remove(num)
                self.seen_more_than_once.add(num)
            else:
                self.seen_once.add(num)

        return next(iter(self.seen_once)) if len(self.seen_once) == 1 else None

test_cases = [
    [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8],
    [1, 3, 3],
    [9, 9, 4],
]

for case in test_cases:
    finder = UniqueNumberFinder(case)
    print(f"List: {case} number: {finder.find_unique()}")

# 2

from collections import defaultdict

class WordFrequencyCounter:
    def __init__(self, words):
        self.words = words
        self.freq = defaultdict(list)

    def count_frequencies(self):
        for word in self.words:
            sorted_word = ''.join(sorted(word))
            self.freq[sorted_word].append(word)

    def print_results(self):
        for group, word_list in self.freq.items():
            unique_words = set(word_list)
            if len(word_list) > 1:
                print(f"Words {tuple(unique_words)} appear {len(word_list)} times.")
            else:
                print(f"Word {tuple(unique_words)} appears {len(word_list)} time.")

words = ["java", "jjava", "vaj", "aavj", "j", "vjaa", "dan", "and", "ddan"]
counter = WordFrequencyCounter(words)
counter.count_frequencies()
counter.print_results()