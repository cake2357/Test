"""
2-opt デモ実行用のスクリプト

実行方法:
    python3 main.py

小さなサンプル点集合を用いて初期ルート（Nearest Neighbor）から 2-opt で改善します。
"""

from two_opt import nearest_neighbor, two_opt, route_length

def main():
    # サンプルの点集合 (x, y)
    points = [
        (0.0, 0.0),
        (1.0, 5.0),
        (5.0, 6.0),
        (7.0, 2.0),
        (6.0, -3.0),
        (2.0, -4.0),
        (-1.0, -1.0),
        (3.0, 1.0),
    ]

    # 初期ルート作成
    init_route = nearest_neighbor(points, start=0)
    init_len = route_length(init_route, points)

    print("初期ルート (Nearest Neighbor):", init_route)
    print(f"初期ルート長: {init_len:.4f}")

    # 2-opt で改善
    best_route, best_len = two_opt(init_route, points)

    print("改善後ルート:", best_route)
    print(f"改善後ルート長: {best_len:.4f}")

    # ルート順の座標表示
    ordered_points = [points[i] for i in best_route]
    print("改善後ルートの座標順:")
    for p in ordered_points:
        print(f"  {p}")

if __name__ == '__main__':
    main()
