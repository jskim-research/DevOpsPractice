"""python profiling 관련 코드

python 기본 profiler는 profile과 cProfile이 있는데 cProfile이 오버헤드가 적으므로 사용 권장

참고 사이트:
- https://jh-bk.tistory.com/18 (cProfile, pStats 관련)
- https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/ (시각화 관련)
"""
import pstats
from cProfile import Profile
from pstats import Stats
import numpy as np
import io
import pandas as pd


def a():
    for i in range(100):
        print(i)
    b()


def b():
    for i in range(1000):
        print(i)
        temp = i * i
        print(temp)
        temp = np.array(temp)


profiler = Profile()
profiler.runcall(a)
result = io.StringIO()
stats = pstats.Stats(profiler, stream=result).sort_stats('ncalls')
stats.print_stats()

stats.dump_stats("./profile_data/dump.prof")  # 이후 command line에서 snakeviz dump.prof 치면 됨

# make csv file
stat_result = result.getvalue()
stat_result = 'ncalls' + stat_result.split('ncalls')[-1]
stat_result = '\n'.join([','.join(line.rstrip().split(None, 6)) for line in stat_result.split('\n')])

with open("./profile_data/cProfileExport.csv", "w+") as f:
    f.write(stat_result)

pd.set_option("display.max_columns", 6)
profile_df = pd.read_csv("./profile_data/cProfileExport.csv", sep=",")
print(profile_df.head())

