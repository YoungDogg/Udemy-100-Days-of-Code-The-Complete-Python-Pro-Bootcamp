import pstats


def analyze_profile():
    stats = pstats.Stats('game_profile.prof')
    stats.strip_dirs()
    stats.sort_stats('cumtime')
    stats.print_stats(10)  # Print the top 10 results


if __name__ == '__main__':
    analyze_profile()
