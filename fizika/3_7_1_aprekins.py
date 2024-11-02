import pandas as pd

values = [3210, 3152, 2976, 2930, 2907, 2771, 2758, 2708, 2580, 2272, 2198, 2156, 1488, 1472, 1459, 995, 930]
err = 1/3 * 1.96
n = 1

for val in values:
    e = (err / val) / 100
    print(f"n{n} = ({val} ± {err:.3f}), e = {e:.7f}%, pie B = 0.95")
    n += 1