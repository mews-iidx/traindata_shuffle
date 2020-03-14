import random
import glob
import os
from shutil import move as mv

train = 0.7
files = glob.glob('*.tfrecord')
print(files)

random.shuffle(files)

os.mkdir('train')
os.mkdir('eval')

train_cnt = int(len(files) * train)
eval_cnt = len(files) - train_cnt
print(train_cnt, eval_cnt)

train
for  f in files[:train_cnt]:
    mv(f,  'train')

for  f in files[train_cnt:]:
    mv(f,  'eval')
