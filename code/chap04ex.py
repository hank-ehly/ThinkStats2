import nsfg


def eval_percentile_rank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100 * (count / len(scores))
    return percentile_rank


def exercise_4_1():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    # my prglngth was 40 weeks
    overall_percentile_rank = eval_percentile_rank(live.prglngth, 40)
    print(overall_percentile_rank)  # 87

    firsts_percentile_rank = eval_percentile_rank(firsts.prglngth, 40)
    print(firsts_percentile_rank)  # 84

    others_percentile_rank = eval_percentile_rank(others.prglngth, 40)
    print(others_percentile_rank)  # 90


if __name__ == '__main__':
    exercise_4_1()
