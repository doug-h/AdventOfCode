
import functools
import re


with open('data.txt') as file:
    seeds, *maps = file.read().split("\n\n")[:-1]
    seeds = [int(s) for s in seeds.split()[1:]]

    in_start, length, offset = 0, 1, 2
    maps = [[map(int, r.split())
            for r in m.split('\n')[1:]]
            for m in maps]
    maps = [sorted([(in_start, length, out_start-in_start)
            for out_start, in_start, length in _map])
            for _map in maps]

    def complete_map(_map):
        extra_ranges = []
        start = 0
        for r in _map:
            if (start < r[in_start]):
                extra_ranges.append((start, r[in_start]-start, 0))
            start = r[in_start]+r[length]
        extra_ranges.append((start, float('inf'), 0))
        _map += extra_ranges

    for m in maps:
        complete_map(m)

    def map_range(_map, _range):
        results = []
        for _r in _map:
            x1 = _r[in_start]
            x2 = _r[in_start] + _r[length] - 1
            y1 = _range[in_start]
            y2 = _range[in_start] + _range[length] - 1
            if (x1 <= y2 and y1 <= x2):
                t1 = max(x1, y1)
                t2 = min(x2, y2)
                results.append((t1+_r[offset], t2-t1+1))
        return results

    def project_forwards(_range, map_index=0):
        if (map_index >= len(maps)):
            return _range[in_start]
        else:
            ranges = map_range(maps[map_index], _range)
            results = [project_forwards(r, map_index+1) for r in ranges]
            return min(results)

    answer1 = min(project_forwards((s, 1)) for s in seeds)
    answer2 = min(project_forwards((s1, s2))
                  for s1, s2 in zip(seeds[::2], seeds[1::2]))

    print(f"Part one: {answer1}")
    print(f"Part two: {answer2}")
