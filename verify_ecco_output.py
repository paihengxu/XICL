import json
from glob import glob
from collections import defaultdict
import numpy as np
from scipy import stats


def flip_label():
    average_decrease = []
    total_decrease = 0
    average_decrease_list_dict = {0: [], 1: []}
    for fn in glob("results/model_gpt2*flip*.jsonl"):
        print(fn)
        with open(fn, 'r') as inf:
            results = defaultdict(list)
            label_idx = []
            all_score = defaultdict(list)
            # accuracy = defaultdict(list)
            for p_idx, line in enumerate(inf):
                data = json.loads(line.strip())
                # accuracy[p_idx].append(data[''])
                for idx, (t, s) in enumerate(zip(data['tokens'][0], data['attributions'][0])):
                    results[idx].append(s)
                    if 'negative' in t or 'positive' in t:
                        all_score[p_idx].append(s)
                        if idx not in label_idx:
                            label_idx.append(idx)

        decrease_cnt = 0
        print(results)
        print(all_score)
        print(label_idx)
        # print(data['tokens'][0][300:308])
        assert len(label_idx) == 4, label_idx
        for ele in label_idx:
            if results[ele][0] > results[ele][1]:
                decrease_cnt += 1
        average_decrease.append(decrease_cnt)

        if np.mean(all_score[0]) > np.mean(all_score[1]):
            total_decrease += 1
        average_decrease_list_dict[0].append(np.mean(all_score[0]))
        average_decrease_list_dict[1].append(np.mean(all_score[1]))
        print(decrease_cnt)
    print(np.mean(average_decrease))
    print("total decrease", total_decrease)
    print(average_decrease_list_dict)
    print(stats.ttest_ind(average_decrease_list_dict[0], average_decrease_list_dict[1]))


def input_neutral():
    total_decrease = 0
    average_decrease_list_dict = {0: [], 1: []}
    # sentiment_idx_dict = {
    #     0: [2, 3, 4, 5, 6, 11, 12, 13, 14, 15,
    #         44, 45, 46, 55,
    #         66, 67, 68, 69, 70, 71, 72, 78, 80, 81, 82,
    #         100, 110, 111],
    #     1: [2, 3, 8,
    #         36,
    #         56, 57, 58, 59, 65, 67, 68,
    #         87, 97],
    # }

    sentiment_idx_dict = {
        0: [2, 3, 4, 5, 6, 11, 12, 14,
            44, 45, 46,
            67, 70, 72, 78, 80, 81, 82,
            100, 110, 111],
        1: [2, 3, 8,
            36,
            56, 57, 58, 59, 65, 67, 68,
            87, 97],
    }
    for fn in glob("results/model_gpt2*neutral*.jsonl"):
        print(fn)
        with open(fn, 'r') as inf:
            all_score = defaultdict(list)
            for p_idx, line in enumerate(inf):
                data = json.loads(line.strip())
                # print("="*100)
                for idx, (t, s) in enumerate(zip(data['tokens'][0], data['attributions'][0])):
                    if idx in sentiment_idx_dict[p_idx]:
                        all_score[p_idx].append(s)

        print(all_score)
        if np.mean(all_score[0]) > np.mean(all_score[1]):
            total_decrease += 1
        average_decrease_list_dict[0].append(np.mean(all_score[0]))
        average_decrease_list_dict[1].append(np.mean(all_score[1]))

    print("total decrease", total_decrease)
    print(average_decrease_list_dict)
    print(stats.ttest_ind(average_decrease_list_dict[0], average_decrease_list_dict[1]))


def complementary_explanations():
    more_review = 0
    average_proportion = []

    review_idx_list = list(range(2, 29)) + list(range(83, 104)) + list(range(151, 174)) + list(range(230, 265))
    explanation_idx_list = list(range(35, 76)) + list(range(110, 144)) + list(range(271, 310))
    for fn in glob("results/model_gpt2*explain*.jsonl"):
        print(fn)
        with open(fn, 'r') as inf:
            all_score = defaultdict(list)
            for p_idx, line in enumerate(inf):
                if p_idx == 0:
                    continue
                data = json.loads(line.strip())
                print("="*100)
                for idx, (t, s) in enumerate(zip(data['tokens'][0], data['attributions'][0])):

                    if idx in review_idx_list:
                        all_score['review'].append(s)

                    if idx in explanation_idx_list:
                        all_score['exp'].append(s)
        print(all_score)
        if np.mean(all_score['review']) > np.mean(all_score['exp']):
            more_review += 1
        average_proportion.append(np.mean(all_score['review']) / np.mean(all_score['exp']))
    #
    print("more_review", more_review)
    print(average_proportion)
    print("review / exp", np.mean(average_proportion))


if __name__ == '__main__':
    # flip_label()
    # input_neutral()
    complementary_explanations()
