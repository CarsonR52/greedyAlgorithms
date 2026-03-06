import sys
from collections import deque, OrderedDict, defaultdict


def read_input(filename):
    with open(filename, "r") as f:
        fir = f.readline().split()
        k = int(fir[0])
        m = int(fir[1])
        reqs = list(map(int, f.readline().split()))

    if k < 1:
        raise ValueError("Cache size must be at least 1.")

    if len(reqs) != m:
        raise ValueError(f"Expected {m} requests, but found {len(reqs)}.")

    return k, reqs


def simulate_fifo(k, requests):
    cache = set()
    q = deque()
    mis = 0

    for x in requests:
        if x in cache:
            continue

        mis += 1

        if len(cache) == k:
            old = q.popleft()
            cache.remove(old)

        cache.add(x)
        q.append(x)

    return mis


def simulate_lru(k, requests):
    cache = OrderedDict()
    mis = 0

    for x in requests:
        if x in cache:
            # move to end since just used
            cache.move_to_end(x)
        else:
            mis += 1

            if len(cache) == k:
                cache.popitem(last=False)

            cache[x] = None

    return mis


def simulate_optff(k, requests):
    cache = set()
    mss = 0

    future = defaultdict(deque)
    for i, x in enumerate(requests):
        future[x].append(i)

    for i, x in enumerate(requests):
        # don't count cur pos as future anymore
        future[x].popleft()

        if x in cache:
            continue

        mss += 1

        if len(cache) < k:
            cache.add(x)
            continue

        vict = None
        far = -1

        for y in cache:
            if len(future[y]) > 0:
                nxt = future[y][0]
            else:
                nxt = float("inf")

            if nxt > far:
                far = nxt
                vict = y

        cache.remove(vict)
        cache.add(x)

    return mss


def main():

    if len(sys.argv) != 2:
        print("Usage: py src/cache_simulator.py <input_file>", file=sys.stderr)
        sys.exit(1)

    fileN = sys.argv[1]

    try:
        k, requests = read_input(fileN)

        fifo = simulate_fifo(k, requests)
        lru = simulate_lru(k, requests)
        optff = simulate_optff(k, requests)

        print(f"FIFO  : {fifo}")
        print(f"LRU   : {lru}")
        print(f"OPTFF : {optff}")

    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()