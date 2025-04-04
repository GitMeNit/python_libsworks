import numpy as np

def calculate(nums:list):
    if len(nums)!=9:
        raise ValueError and print("enter more than or equal to 9 numbers")
    else:
        mat1= np.array(nums).reshape(3,3)
        calculations= {"mean":[mat1.mean(axis=0).tolist(),mat1.mean(axis=1).tolist(),mat1.mean().tolist()],
                       "var":[mat1.var(axis=0).tolist(),mat1.var(axis=1).tolist(),mat1.var().tolist()],
                       "std":[mat1.std(axis=0).tolist(),mat1.std(axis=1).tolist(),mat1.std().tolist],
                       'max': [mat1.max(axis=0).tolist(), mat1.max(axis=1).tolist(), mat1.max().tolist()],
                       'min': [mat1.min(axis=0).tolist(), mat1.min(axis=1).tolist(), mat1.min().tolist()],
                       'sum': [mat1.sum(axis=0).tolist(), mat1.sum(axis=1).tolist(), mat1.sum().tolist()],
                       }
        print(calculations)
calculate([2,3,4,5,6,7,8,9,10])