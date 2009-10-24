# -*- coding: utf-8 -*-

import time
import codecs
import bisect


test_list = [u'', u'meag', u'mea_', u'é', u'á' ]
test_list_str = [S.encode('iso-8859-2') for S in test_list]


def get_index(path):
    word_list = []
    for line in codecs.open(path, encoding='iso-8859-2'):
        word, position, offset = line.split()
        word_list.append(word)
    return word_list

def get_index_str(path):
    word_list = []
    for line in open(path):
        word, position, offset = line.split()
        word_list.append(word)
    return word_list


def select(index, word):
    """select a word from a list, if the element starts with that word"""
    if len(word):
        return [key for key in index if key.startswith(word)]
    else: return []



def select_bisect(index, word):
    """select a word from a list, if the element starts with that word"""
    result = []
    if not word:
        return result
    
    i = bisect.bisect_left(index, word)
    n = len(index)
    while i < n:
        key = index[i]
        if not key.startswith(word):
            break
        result.append(key)
        i += 1
    
    return result
    


index = get_index('eng-hun.index')
index_str = get_index_str('eng-hun.index')
index_sorted = list(sorted(index))

index_sorted_str = list(sorted(index))


index = get_index('eng-hun.index')
index_str = get_index_str('eng-hun.index')

t1 = time.time()
for word in test_list_str:
        L1 = select(index_str, word)
t2 = time.time()

print 'Benchmark result with str is %0.3f ms' % ((t2-t1)*1000.0)

t1 = time.time()
for word in test_list:
        L1 = select(index, word)
t2 = time.time()

print 'Benchmark result with unicode is %0.3f ms' % ((t2-t1)*1000.0)

t1 = time.time()
for word in test_list:
        L2 = select_bisect(index_sorted, word)
t2 = time.time()

print 'Benchmark result with unicode and bisect is %0.3f ms' % ((t2-t1)*1000.0)

print L1, L2

assert list(sorted(L1)) == L2


