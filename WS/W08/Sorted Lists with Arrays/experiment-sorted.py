from array_list import *
from array_sorted_list import *
import matplotlib.pyplot as plt
import random
import resource
import gzip

def time():
    return resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + \
                resource.getrusage(resource.RUSAGE_SELF).ru_utime

def experiment(ListClass, words):
    l = ListClass(len(words) + 1)

    times1 = []
    times2 = []
    if ListClass is ArrayList:
        for w in words:
            t = time()
            l.append(w)
            times1.append(time() - t)
    else:
        for w in words:
            t = time()
            l.add(w)
            times1.append(time() - t)

    interval = list(range(len(words)))
    random.shuffle(interval)
    for i in interval:
        t = time()
        l.index(words[i])
        times2.append(time() - t)

    return sum(times1) / len(times1), sum(times2) / len(times2)

if __name__ == '__main__':
    # the file is obtained from https://github.com/dwyl/english-words
    with gzip.open('words.txt.gz', 'rt') as fp:
        words = fp.readlines()
    words = [w.strip() for w in words]

    random.seed()

    times11, times12, times21, times22 = [], [], [], []
    for n in range(1, 202, 3):
        random.shuffle(words)

        t1, t2 = experiment(ArrayList, words[:(10 * n)])
        times11.append(t1)
        times12.append(t2)

        t1, t2 = experiment(ArraySortedList, words[:(10 * n)])
        times21.append(t1)
        times22.append(t2)

    coords = []
    coords.append([10 * n for n in range(1, 202, 3)])
    coords.append(times11)
    coords.append([10 * n for n in range(1, 202, 3)])
    coords.append(times12)
    coords.append([10 * n for n in range(1, 202, 3)])
    coords.append(times21)
    coords.append([10 * n for n in range(1, 202, 3)])
    coords.append(times22)

    lines = plt.plot(*coords, zorder=3)
    ax = plt.gca()

    lgtext = ['standard append()', 'standard index()', 'sorted add()', 'sorted index()']
    lg = ax.legend(lines, lgtext, loc='best', fancybox=True, shadow=True)

    plt.grid(True, ls=':', lw=0.5, zorder=1)
    plt.xlabel('number of words n')
    plt.ylabel('time spent (seconds)')
    plt.savefig('./plot-lin.png', bbox_inches='tight')
    ax.set_yscale('log')
    plt.savefig('./plot-log.png', bbox_inches='tight')
    plt.close()

