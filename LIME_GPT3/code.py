#GPT3
import numpy as np
import os
import openai
openai.api_key = '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'

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

import numpy as np
import lime
import torch
import torch.nn.functional as F
from lime.lime_text import LimeTextExplainer

class_names = ['positive','negative']

def predictor(texts):
    #print('text:', texts)

    #outputs = model(**tokenizer(texts, return_tensors="pt", padding=True))
    #tensor_logits = outputs[0]
    #probas = F.softmax(tensor_logits).detach().numpy()
    probas_tmp = ''
    num = 0
    for text in texts:
        response = openai.Completion.create(
            engine="davinci-instruct-beta-v3",
            prompt=text,
            temperature=0,
            max_tokens=500,
            logprobs=5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["12."]
        )
        text = response['choices'][0]['text']
        probs = response['choices'][0]['logprobs']['top_logprobs'][0]
    #print(probs)
        if 'positive' in text.lower():
            prob1 = 0
            prob2 = 0
            for key, value in probs.items():
                    if 'positive' in key.lower():
                        prob1 += value
                    else:
                        prob2 += value
            if 'negative' in text.lower():
                prob1 = 0
                prob2 = 0
                for key, value in probs.items():
                    if 'negative' in key.lower():
                        prob2 += value
                    else:
                        prob1 += value

        probas = softmax([prob1, prob2])
        probas = np.reshape(probas, (1,2))
        if num == 0:
            probas_tmp = probas
            num +=1
            continue
        probas_tmp = np.concatenate((probas_tmp, probas), axis=0)
        num +=1

    print(probas_tmp.shape)
    return probas_tmp
#prompt in demo.txt
with open('demo.txt') as f:
    contents = f.read()
text = contents

explainer = LimeTextExplainer(class_names=class_names)
exp = explainer.explain_instance(text, predictor, num_features=20, num_samples=6)
fig = exp.as_pyplot_figure()
exp.save_to_file('oi.html')
print(exp.as_list())
