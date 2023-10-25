import math

def sum_sorted(num1, num2=math.pi, verbose=False):
  num_sum = num1 + num2
  sorted_nums = sorted([num1, num2])

  if verbose:
    print(f'Parameters: num1={num1}, num2={num2}')
    print(f'Results: sum={num_sum}, Sorted Numbers={sorted_nums}')

  return num_sum, sorted_nums

result1 = sum_sorted(5, verbose=True)
result2 = sum_sorted(2,7)

if __name__=='__main__':
  
  print(sum_sorted(13))
  print(sum_sorted(1,2))
  assert sum_sorted(13, verbose=True) == (16.141592653589793, [3.141592653589793, 13])
  assert sum_sorted(1,2) == (13)