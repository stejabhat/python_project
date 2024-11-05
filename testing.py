import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import json

url = 'https://storage.googleapis.com/kagglesdsdata/datasets/2594075/4429121/intents.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240909%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240909T151208Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=96ff2f37806f49565a1f9422df1356b421fe8c966a37dcc4c487884e4d373389acb1a6092ac26afe00a7715590074e94ee2dd567284390858fffb2560f98c48042a73d2f85914ea10768c4c3213ff0b770046ddcbc9e2a36bda983a7654385fb8ada1811915f2e6029d7dc5650014a7a2f358e200fdeb8f1566d4b29ad55e0a67c895efc277d5d604402a25a5089eba3cf65dc5759e49189e0875445d6d8012c1598e6898006d58109bcb459d6498451355eee272cb4fefb89eb1bdfba726b77c3000fda6e45c07c7888b31e3053fe7fc7ef42604a20d393d0f181dd9699fc0cc76bdc06dd254da97168c1f55eb5bfc6fb2aeb9f08afe6219619468eb65e4387'

data = pd.read_json(url)

df = pd.DataFrame(data['intents'])
df