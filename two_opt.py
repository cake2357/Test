"""
2-opt アルゴリズム（TSP の局所探索改善）

関数:
 - euclidean(a, b): 2点間のユークリッド距離
 - route_length(route, points): ルート長を計算
 - nearest_neighbor(points, start=0): 貪欲で初期ルートを作成
 - two_opt(route, points): 2-opt 最適化を実行し改善されたルートを返す

このファイルは他のスクリプトからインポートして使えます。
"""

import math
from typing import List, Tuple

Point = Tuple[float, float]

def euclidean(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def route_length(route: List[int], points: List[Point]) -> float:
    total = 0.0
    n = len(route)
    for i in range(n):
        a = points[route[i]]
        b = points[route[(i + 1) % n]]
        total += euclidean(a, b)
    return total

def nearest_neighbor(points: List[Point], start: int = 0) -> List[int]:
    n = len(points)
    if n == 0:
        return []
    unvisited = set(range(n))
    route = [start]
    unvisited.remove(start)
    while unvisited:
        last = route[-1]
        next_node = min(unvisited, key=lambda j: euclidean(points[last], points[j]))
        route.append(next_node)
        unvisited.remove(next_node)
    return route

def two_opt(route: List[int], points: List[Point]) -> Tuple[List[int], float]:
    n = len(route)
    if n <= 2:
        return route[:], route_length(route, points)

    best = route[:]
    best_len = route_length(best, points)

    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_route = best[:i] + best[i:k + 1][::-1] + best[k + 1:]
                new_len = route_length(new_route, points)
                if new_len + 1e-12 < best_len:
                    best = new_route
                    best_len = new_len
                    improved = True
                    break
            if improved:
                break

    return best, best_len

__all__ = ["euclidean", "route_length", "nearest_neighbor", "two_opt"]
