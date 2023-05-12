from datasets import load_dataset
import json
import random


if __name__ == '__main__':
    sst2 = load_dataset("sst2")
    test = random.sample(list(sst2['validation']), 20)
    with open('data/saliency_test.jsonl', 'w') as outf:
        for ele in test:
            outf.write(f"{json.dumps(ele)}\n")