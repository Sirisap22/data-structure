print(' *** Summation of each digit ***')
s_nums = input('Enter a positive number : ')
nums = list(map(lambda x: int(x), [ char_num for char_num in s_nums]))
print(f'Summation of each digit =  {sum(nums)}')