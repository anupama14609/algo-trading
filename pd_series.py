import pandas as pd 
import numpy as np 

series_data = pd.Series([1, 2, 3,4,5,6,7,8,9,10], index=list('abcdefghij'))
print(series_data)

print(f'value at index a: {series_data.a}\n')
print(f'value at index b: {series_data.b}\n')
print(f'value at index c: {series_data.c}\n')
print(f'value at index d: {series_data.d}\n')
print(f'value at index e: {series_data.e}\n')
print(f'value at index f: {series_data.f}\n')
print(f'value at index g: {series_data.g}\n')
print(f'value at index h: {series_data.h}\n')
print(f'value at index i: {series_data.i}\n')
print(f'value at index j: {series_data.j}\n')