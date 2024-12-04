# import os
from collections import Counter
from threading import Thread, Lock
import re


def split_file(file_path, num_parts):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    chunk_size = len(content) // num_parts
    chunks = [
        content[i * chunk_size: (i + 1) * chunk_size]
        for i in range(num_parts)
    ]

    # чтобы не терять последний кусочек
    if len(content) % num_parts != 0:
        chunks[-1].extend(content[num_parts * chunk_size:])
    return chunks


def count_words(lines):
    word_counts = Counter()
    for line in lines:
        words = re.findall(r'\w+', line.lower())
        word_counts.update(words)
    return word_counts


class WordCounterThread(Thread):
    def __init__(self, lines, results, lock):
        super().__init__()
        self.lines = lines
        self.results = results
        self.lock = lock

    def run(self):
        local_count = count_words(self.lines)
        with self.lock:
            self.results.append(local_count)


def merge_counters(counters):
    total_counts = Counter()
    for counter in counters:
        total_counts.update(counter)
    return total_counts


def process_file_in_parallel(file_path, num_threads):
    chunks = split_file(file_path, num_threads)

    results = []
    lock = Lock()

    threads = [WordCounterThread(chunk, results, lock) for chunk in chunks]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    final_counts = merge_counters(results)
    return final_counts


file_path = 'input.txt'
num_threads = 4

word_frequencies = process_file_in_parallel(file_path, num_threads)

print("Частота слов:")
print(word_frequencies.most_common())
# for word, count in word_frequencies.most_common():
#     print(f"{word}: {count}")

