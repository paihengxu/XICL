import json
from glob import glob
from collections import defaultdict
import numpy as np
from scipy import stats


if __name__ == '__main__':
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
