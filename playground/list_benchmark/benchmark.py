import time

def _open(path_index):
    fobj = open(path_index, mode='r', buffering=-1);
    index = []
    for line in fobj.readlines():
        a, b = line.strip().split('\t')
        position, offset = b.split(' ')
        index.append(a)
    fobj.close()
    return index

def select(index, word):
    """select a word from a list, if the element starts with that word"""
    if len(word):
        return [key for key in index if unicode(key, "iso-8859-2").encode("utf8").startswith(word)]
    else: return []

index = _open("eng-hun.index")
t1 = time.time()
select(index, "")
select(index, "meag")
select(index, "mea_")
select(index, "\xE9")
select(index, "\x9C")
t2 = time.time()

print 'Benchmark result is %0.3f ms' % ((t2-t1)*1000.0)
