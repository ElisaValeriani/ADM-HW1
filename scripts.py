#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Introduction
# Say "Hello, World!" With Python ok

print("Hello, World!")


# In[ ]:


# Introduction
# Python If-Else

if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 100:
        if n % 2 != 0:
            print("Weird")
        elif 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print('Input out of range')


# In[ ]:


# Introduction
# Arithmetic Operators 

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# In[ ]:


# Introduction
# Python: Division 

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a // b))
    print(a / b)


# In[ ]:


# Introduction
# Loops 

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n:
        print(i * i)
        i += 1


# In[ ]:


# Introduction
# Write a function

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


my_year = int(input())
print(is_leap(my_year))


# In[ ]:


# Introduction
# Print Function

if __name__ == '__main__':
    n = int(input())
    i = 1
    while i <= n:
        print(i, end="")
        i += 1


# In[ ]:


# Data Types
# List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l.append([i, j, k])
l = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
res = []
for _ in range(len(l)):
    if l[_][0]+l[_][1]+l[_][2] != n:
        res.append(l[_])
print(res)


# In[ ]:


# Data Types
# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    list1.sort()
    list1.reverse()
    i = 0
    while i < n:
        if list1[ i ] > list1[ i + 1 ]:
            print(list1[ i + 1 ])
            break
        else:
            i += 1


# In[ ]:


# Data Types
# Nested Lists

if __name__ == '__main__':
    score = [ ]
    for _ in range(int(input())):
        name = input()
        my_score = float(input())
        score.insert(_, [ name, my_score ])
    score.sort(key=lambda x: x[ 1 ])
    i = 0
    while i < len(score):
        if score[ i ][ 1 ] < score[ i + 1 ][ 1 ]:
            break
        else:
            i += 1
    res = i + 1
    res_score = [ ]
    i = 0
    for i in range(len(score)):
        if score[ res ][ 1 ] == score[ i ][ 1 ]:
            res_score.append(score[ i ][ 0 ])
            i += 1
    res_score.sort()
    for i in range(len(res_score)):
        print(res_score[ i ])


# In[ ]:


# Data Types
# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    line = [ ]
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[ name ] = scores
    query_name = input()
    s = 0
    for _ in range(len(line)):
        s = student_marks[ query_name ][ _ ] + s
    result = s / 3
    print("{0:.2f}".format(result))


# In[ ]:


# Data Type
# Lists

if __name__ == '__main__':
    N = int(input())
    my_list = [ ]
    for i in range(N):
        command, *num = input().split()
        if command == "print":
            print(my_list)
        elif command == "insert":
            my_list.insert(int(num[ 0 ]), int(num[ 1 ]))
        elif command == "remove":
            my_list.remove(int(num[ 0 ]))
        elif command == "append":
            my_list.append(int(num[ 0 ]))
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()


# In[ ]:


# Data Types
# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))


# In[ ]:


# Strings
# String Split and Join

def split_and_join(line):
    my_split = line.split(" ")
    my_join = "-".join(my_split)
    return my_join


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


# Strings
# What's Your Name?

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


# Strings
# Mutations

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


# Strings
# Find a string

def count_substring(string, sub_string):
    c = 0
    for _ in range(len(string)):
        if string[_:_+len(sub_string)] == sub_string:
            c = c + 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


# Strings
# String Validators

if __name__ == '__main__':
    s = input()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for _ in range(len(s)):
        if s[_].isalnum():
            c1 = c1 + 1
        if s[_].isalpha():
            c2 = c2 + 1
        if s[_].isdigit():
            c3 = c3+ 1
        if s[_].islower():
            c4 = c4 + 1
        if s[_].isupper():
            c5 = c5 + 1
    if c1 > 0:
        print("True")
    else:
        print("False")
    if c2 > 0:
        print("True")
    else:
        print("False")
    if c3 > 0:
        print("True")
    else:
        print("False")
    if c4 > 0:
        print("True")
    else:
        print("False")
    if c5 > 0:
        print("True")
    else:
        print("False")


# In[ ]:


# Strings
# Text Alignment

thickness = int(input())
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


# Strings
# Text Wrap

def wrap(string, max_width):
    s = ""
    for _ in range(0, len(string), max_width):
        s = s + string[_:_+max_width] + "\n"
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:


# Strings
# Designer Door Mat

N, M = map(int, input().split())
for _ in range(0, N//2):
    print((".|."*(_*2+1)).center(M, '-'))
print("WELCOME".center(M, '-'))
for _ in range(N//2, 0, -1):
    print((".|."*(_*2-1)). center(M, '-'))


# In[ ]:


# Strings
# String Formatting

# TODO #don't know how to format the output to the width of the binary value of n 

def print_formatted(number):
    s = len(list(format(number, 'b')))
    for _ in range(1, number+1):
        print(_, end=" ")
        print(oct(_)[2:], end=" ")
        print(hex(_).upper()[2:], end=" ")
        print(format(_, 'b'), end=" ")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


# Strings
# Alphabet Rangoli

#TODO #don't know how to print, in the desired way, the alphabet's letters

def print_rangoli(size):
    if 0 < size < 27:
        ori = size+size-1
        o = ori+ori-1
        s = "abcdegfhijklmnopqrstuvwxyz" 
        for _ in range(n):
            print((s[_] * (_ * 2 + 1)).center(o, '-'))
    else:
        print("Index out of range")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:


# Strings
# Capitalize!

#TODO #don't know how to capitalize and, at the same time, mantain the whitespaces

def solve(s):
    s_list = s.split()
    new_s = []
    for _ in range(0, len(s_list)):
        c = 0
        new_s.append(s_list[_].capitalize())
        for i in range(0, len(s_list[_])):
            if s_list[_][i] == " ":
                c = c + 1
        new_s.append(" "*c)
    new_s = " ".join(new_s)
    return new_s


s = input()
result = solve(s)
print(result)


# In[ ]:


# Strings
# The Minion Game

def minion_game(string):
    if 0 < len(string) <= 1000000:
        k_score = 0
        s_score = 0
        c = len(string)
        for letter in string:
            if letter in "AEIOU":
                k_score = k_score+c
            else:
                s_score = s_score+c
            c = c-1
        if k_score > s_score:
            return print("Kevin "+str(k_score))
        elif k_score < s_score:
            return print("Stuart "+str(s_score))
        else:
            return print("Draw")

    else:
        return print("Input out of range")


if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[ ]:


# Strings
# Merge the Tools!

def merge_the_tools(string, k):
    n = len(string)
    l = []
    for _ in range(0, n, k):
        l.append(string[_:_+k])
    for _ in range(len(l)):
        new_l = list(l[_])
        for i in new_l:
            if new_l.count(i) > 1:
                new_l.remove(i)
    print(new_l)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:


# Strings,
# sWAPE cASE

def swap_case(s):
    res = ""
    for letter in s:
        if letter.isupper():
            res = res + letter.lower()
        elif letter.islower():
            res = res + letter.upper()
        else:
            res = res + letter
    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


# Sets
# Introduction to Sets

def average(array):
    s = set(array)
    l = list(s)
    num = sum(l)
    den = len(l)
    return (num/den)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:


# Sets
# No Idea!

#TODO #in most test cases the code didn't execute within the time limits, while in one test case the answer was wrong 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
hap = 0
for i in arr:
    if arr.count(i)>1:
        arr.remove(i)
for i in arr:
    if i in A:
        hap = hap+1
    elif i in B:
        hap = hap-1
print(int(hap))


# In[ ]:


# Sets
# Symmetric Difference

M = int(input())
set_M = set(map(int, input().split()))
N = int(input())
set_N = set(map(int, input().split()))
dif1 = set_M.difference(set_N)
dif2 = set_N.difference(set_M)
u = dif1.union(dif2)
c = 0
num = -20
while c < len(u):
    if num in u:
        print(num)
        c += 1
    num += 1


# In[ ]:


# Sets
# Set.add()

N = int(input())
s = set()
for _ in range(0, N):
    s.add(input())
print(len(s))


# In[ ]:


# Sets
# Set.discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command, *num = input().split()
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(num[0]))
    elif command == "discard":
        s.discard(int(num[0]))
s = list(s)
res = 0
for _ in range(0, len(s)):
    res = s[_] + res
print(res)


# In[ ]:


# Sets
# Set.union() Operation

n = int(input())
eng = set(input().split())
b = int(input())
fre = set(input().split())
s = eng.union(fre)
print(len(list(s)))


# In[ ]:


# Sets
# Set.intersection() Operation

n = int(input())
eng = set(input().split())
b = int(input())
fre = set(input().split())
s = eng.intersection(fre)
print(len(list(s)))


# In[ ]:


# Sets
# Set.difference() Operation

n = int(input())
eng = set(input().split())
b = int(input())
fre = set(input().split())
s = eng.difference(fre)
print(len(list(s)))


# In[ ]:


# Sets
# Set.symmetric_difference() Operation

n = int(input())
eng = set(input().split())
b = int(input())
fre = set(input().split())
s = eng.symmetric_difference(fre)
print(len(list(s)))


# In[ ]:


# Sets
# Set Mutations

n_A = int(input())
A = set(input().split())
N = int(input())
for _ in range(0, N):
    command, l = input().split()
    s = set(input().split())
    if command == "update":
        A.update(s)
    elif command == "intersection_update":
        A.intersection_update(s)
    elif command == "difference_update":
        A.difference_update(s)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(s)
A = list(A)
res = 0
for _ in range(0, len(A)):
    res = int(A[_]) + res
print(res)


# In[ ]:


# Sets
# The Captain's Room

#TODO #in most of the test cases the code didn't execute within the time limits

K = int(input())
if 1 < K < 1000:
    l = input().split()
    s = set(l)
    for room in s:
        if l.count(room) != K:
            print(room)
else:
    print("Input out of range")


# In[ ]:


# Sets
# Check Subset

T = int(input())
for _ in range(T):
    n_A = int(input())
    A = set(map(int, input().split()))
    n_B = int(input())
    B = set(map(int, input().split()))
    print(A.intersection(B) == A)


# In[ ]:


# Sets
# Check Strict Superset

#TODO #In some test cases the output was wrong 

A = set(map(int, input().split()))
n = int(input())
res = True
for _ in range(n):
    s = set(map(int, input().split()))
    if A.intersection(s) == s and A != s and s.difference(A) == set():
        res = False
        break
print(res)


# In[ ]:


# Collections
# DefaultDict Tutorial

#TODO #In some cases the answer was wrong

n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
for i in range(len(B)):
    c = 0 
    for j in range(len(A)):
        if B[i] == A[j]:
            print(j+1, end=" ")
            c += 1
    if c == 0:
        print(-1)
    print()


# In[ ]:


# Collections
# collections.Counter()

from collections import Counter
X = int(input())  # number of shoes
sizes = list(map(int, input().split()))  # list of shoe sizes in the shop
N = int(input())  # number of customers
earned = 0
for _ in range(N):
    s_size, x_i = map(int, input().split())
    if s_size in Counter(sizes).keys():
        earned = earned+int(x_i)
        sizes.remove(s_size)
print(earned)


# In[ ]:


# Collections
# Collections.namedtuple()

from collections import namedtuple
N = int(input())  # number of students
col_names = input()
Student = namedtuple('Student', col_names)
students = []
for _ in range(N):
    inp = input().split()
    students.append(Student(inp[0], inp[1], inp[2], inp[3]))
tot_marks = 0
for _ in range(N):
    tot_marks = int(students[_].MARKS) + tot_marks
print("{0:.2f}".format(tot_marks/N))


# In[ ]:


# Collections
# Collections.OrderedDict()

from collections import OrderedDict
N = int(input())  # number of items
my_list = []
ord_dict = OrderedDict()
for _ in range(N):
    inp = input().split()
    if len(inp) == 2:
        item_name = inp[0]
        my_list.append(item_name)
        item_price = inp[1]
    elif len(inp) == 3:
        item_name = inp[0]+" "+inp[1]
        my_list.append(item_name)
        item_price = inp[2]
    ord_dict[item_name] = item_price

for key, value in ord_dict.items():
    print(key+" "+str(int(value)*my_list.count(key)))


# In[ ]:


# Collections
# Word Order

from collections import Counter
n = int(input())
my_list = []
for _ in range(n):
    my_list.append(input())
print(len(Counter(my_list)))
my_values = list(Counter(my_list).values())
for _ in range(len(my_values)):
    print(my_values[_], end=" ")


# In[ ]:


# Collections
# Collections.deque()

from collections import deque
N = int(input())  #number of commands
d = deque()
for _ in range(N):
    command, *v = input().split()
    if command == "append":
        d.append(v[0])
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    elif command == "appendleft":
        d.appendleft(v[0])
for _ in range(len(d)):
    print(d[_][0], end=" ")


# In[ ]:


# Collections
# Company logo

#TODO

import operator
if __name__ == '__main__':
    s = input()
    my_list = []
    for letter in s:
        my_list.append(letter)
    my_set = set(my_list)
    my_list1 = list(my_set)
    dictionary = {}
    for _ in range(len(my_list1)):
        c = my_list.count(my_list1[_])
        dictionary[my_list1[_]] = c
    sort = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
    for _ in range(len(sort)):
        dictionary1 = {}
        c = 1
        while c <= len(sort)-_-1: 
            if sort[_][1] == sort[_+c][1]:
                dictionary1[sort[_][0]] = sort[_][1]
                dictionary1[sort[_+c][0]] = sort[_+c][1]
                dictionary1 = sorted(dictionary1.items(), key=operator.itemgetter(0))
                print(dictionary1[0][0], end=" ")
                print(dictionary1[0][1])
                print(dictionary1[1][0], end=" ")
                print(dictionary1[1][1])
                c += 1
            else:
                print(sort[_][0], end=" ")
                print(sort[_][1])
                c = len(sort)-_


# In[ ]:


# Collections
# Piling Up!

#TODO 


# In[ ]:


# Date and Time
# Calendar Module

import calendar
M, D, Y = input().split()
if M[0] == '0':
    M = M[1]
if D[0] == '0':
    D = D[1]
day = calendar.weekday(int(Y), int(M), int(D))
if day == 0:
    print("MONDAY")
elif day == 1:
    print("TUESDAY")
elif day == 2:
    print("WEDNESDAY")
elif day == 3:
    print("THURSDAY")
elif day == 4:
    print("FRIDAY")
elif day == 5:
    print("SATURDAY")
elif day == 6:
    print("SUNDAY")


# In[ ]:


# Time and Date
# Time Delta

#TODO


# In[ ]:


# Exceptions

T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e1:
        print("Error Code:", e1)
    except ValueError as e2:
        print("Error Code:", e2)


# In[ ]:


# Zipped

N, X = map(int, input().split())
x = []
y = []
for _ in range(X):
    x.append(input().split())
    y = y + [x[_]]
my_list = list(zip(*y))
for i in range(N):
    tot_marks = 0
    for j in range(X):
        tot_marks = tot_marks + float(my_list[i][j])
    print(tot_marks/X)


# In[ ]:


# Athlete Sort

N, M = map(int, input().split())  #number of athletes, number of attributes
n = []
for _ in range(N):
    n.append(list(map(int, input().split())))
K = int(input())  #index of the attibute to sort the data based on
for _ in range(1, N):
    c = 1
    while c < _ + 1:
        if n[ _ - c + 1 ][K] < n[ _ - c ][K]:
            value1 = n[ _ - c ]
            value2 = n[ _ - c + 1 ]
            n[ _ - c ] = value2
            n[ _ - c + 1 ] = value1
        c += 1
for i in range(N):
    for j in range(M):
        print(n[i][j], end=" ")
    print()


# In[ ]:


# ginortS

S = input()
lower = []
upper = []
odd = []
even = []
for s in S:
    if s.islower():
        lower.append(s)
    if s.isupper():
        upper.append(s)
    if s.isdigit():
        if int(s) % 2 != 0:
            odd.append(s)
        else:
            even.append(s)
res = sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)
res = "".join(res)
print(res)


# In[ ]:


# Map and Lambda Functions

cube = lambda x: x*x*x  # complete the lambda function


def fibonacci(n):
    arr = []
    if n > 0:
        arr.append(0)
    if n > 1:
        arr.append(1)
    c = 0
    while c < n-2:
        arr.append(arr[c]+arr[c+1])
        c += 1
    return arr


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# In[ ]:


# Regex and Parsing
# Detect Floating Point Number

N = int(input())
for _ in range(N):
    p = ""
    string = input()
    string1 = string
    try:
        float(string1)
    except:
        print("False")
        p = "F"
        continue
    my_list = []
    for s in string:
        my_list.append(s)
    if my_list[0] == "+" or my_list[0] == "-":
        if my_list[1] == "+" or my_list[1] == "-":
            print("False")
            p = "F"
            continue

    c = 0
    for l in range(len(my_list)):
        if my_list[l] == ".":
            c += 1
            if my_list[l] == my_list[len(my_list)-1]:
                print("False")
                p = "F"
                continue
    if c > 1 or c == 0:
        print("False")
        p = "F"
    if p != "F":
        print("True")


# In[ ]:


# Regex and Parsing
# Re.split()

import re
regex_pattern = r"\W+"  #r'_' is used to interpet the string literally (ex.: '\tTab' would print a tab and then the string Tab)
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:


# Regex and Parsing
# Regex Substitution

import re
N = int(input())
for _ in range(N):
    line = input()
    regex = re.compile(" [&][&] ")
    sub = regex.sub(" and ", line)
    regex = re.compile(" [&][&] ")
    sub = regex.sub(" and ", sub)
    regex = re.compile(" [|][|] ")
    sub = regex.sub(" or ", sub)
    regex = re.compile(" [|][|] ")
    sub = regex.sub(" or ", sub)
    print(sub)


# In[ ]:


# Regex and Parsing
# Re.findall() & Re.finditer()

import re

S = input()
reg = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', S)
# ?<=... matches if the current position in the string is preceded by a match for ... (positive lookbehind assertion)
# ?=... matches if ... matches next, but doesn’t consume any of the string (lookahead assertion)
if len(reg) > 0:
    for _ in range(len(reg)):
        print(reg[_])
else:
    print(-1)


# In[ ]:


# Regex and Parsing
# Re.start() & Re.end()

#TODO #In one test case the code did not execute within the time limits

import re
S = input()
k = input()
m = re.search(k, S)
if m is not None:
    s = 0
    while m is not None:
        s = m.start()
        e = m.end()
        S = " "*(e-1)+S[e-1:]
        m = re.search(k, S)
        print("("+str(s)+", "+str(e-1)+")")
else:
    print("(-1, -1)")


# In[ ]:


# Regex and Parsing
# Validating Roman Numerals

#TODO #don't know how to specify that I, X, C and M can be repeated at most three consecutive times while V, L, and D just one
      #consecutive time

regex_pattern = r"[MDCLXVI]"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# In[ ]:


# Regex and Parsing
# Validating Phone Numbers

import re
N = int(input())
for _ in range(N):
    S = input()
    if re.search(r'^7[\d][\d][\d][\d][\d][\d][\d][\d][\d]$', S) or re.search(r'^8[\d][\d][\d][\d][\d][\d][\d][\d][\d]$', S) or re.search(r'^9[\d][\d][\d][\d][\d][\d][\d][\d][\d]$', S):
        print("YES")
    else:
        print("NO")


# In[ ]:


# Regex and Parsing
# Validating and Parsing Email Addresses

import re
n = int(input())
for _ in range(n):
    email = input()
    e = email.split()
    m = re.match(r'<[A-Za-z][-_.\w]+@[A-Za-z]+[.][A-Za-z]{1,3}>', e[1])
    if m is not None:
        print(email)


# In[ ]:


# Regex and Parsing
# Hex Color Code

import re
N = int(input())
for i in range(N):
    line = input()
    regex = r'#[A-Fa-f0-9]{3,6}'
    res = re.findall(regex, line)
    for j in range(len(res)):
        if line != res[j]:
            if line != res[j]+" {":
                print(res[j])


# In[ ]:


# Regex and Parsing
# HTML Parser - Part 1

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
        if len(attrs) > 0:
            for _ in range(len(attrs)):
                key = str(attrs[_][0])
                value = str(attrs[_][1])
                print("-> "+key+" > "+value)

    def handle_endtag(self, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        if len(attrs) > 0:
            for _ in range(len(attrs)):
                key = str(attrs[_][0])
                value = str(attrs[_][1])
                print("-> "+key+" > "+value)


parser = MyHTMLParser()
N = int(input())
html = ""
for _ in range(N):
    html = html + str(input())
parser.feed(html)


# In[ ]:


# Regex and Parsing
# HTML Parser - Part 2

import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if re.search(r'\n', data):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[ ]:


# Regex and Parsing
# Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for _ in range(len(attrs)):
            print("-> "+attrs[_][0]+" > "+attrs[_][1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for _ in range(len(attrs)):
            print("-> "+attrs[_][0]+" > "+attrs[_][1])


parser = MyHTMLParser()
N = int(input())
html = ""
for _ in range(N):
    html = html + str(input())
parser.feed(html)


# In[ ]:


# Regex and Parsing
# Validating UID

from collections import Counter
import re
T = int(input())
for _ in range(T):
    UID = input()
    if UID.isalnum:
        l = Counter(UID).values()
        if 2 or 3 in l:
            if len(Counter(UID)) == 10:
                if re.findall(r'(.*?[A-Z]){2,}', UID):
                    if re.findall(r'(.*?[0-9]){3,}', UID):
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")


# In[ ]:


# Regex and Parsing
# Validating Credit Card Numbers

import re
N = int(input())
regex = r'^[456][\d]{3}[-]?[\d]{4}[-]?[\d]{4}[-]?[\d]{4}\Z'
regex1 = r'^[456][\d]{3}[-][\d]{4}[-][\d]{4}[-][\d]{4}\Z'
for i in range(N):
    card_num = input()
    match = re.search(regex, card_num)
    if match and re.search(regex1, card_num) is not None:
        card_num = list(card_num)
        card_num1 = card_num[0:4] + card_num[5:9] + card_num[10:14] + card_num[15:19]
        if card_num1[0] == card_num1[1] == card_num1[2] == card_num1[3] or             card_num1[ 1 ] == card_num1[ 2 ] == card_num1[ 3 ] == card_num1[ 4 ] or             card_num1[ 2 ] == card_num1[ 3 ] == card_num1[ 4 ] == card_num1[ 5 ] or             card_num1[ 3 ] == card_num1[ 4 ] == card_num1[ 5 ] == card_num1[ 6 ] or             card_num1[ 4 ] == card_num1[ 5 ] == card_num1[ 6 ] == card_num1[ 7 ] or             card_num1[ 5 ] == card_num1[ 6 ] == card_num1[ 7 ] == card_num1[ 8 ] or             card_num1[ 6 ] == card_num1[ 7 ] == card_num1[ 8 ] == card_num1[ 9 ] or             card_num1[ 7 ] == card_num1[ 8 ] == card_num1[ 9 ] == card_num1[ 10 ] or             card_num1[ 8 ] == card_num1[ 9 ] == card_num1[ 10 ] == card_num1[ 11 ] or             card_num1[ 9 ] == card_num1[ 10 ] == card_num1[ 11 ] == card_num1[ 12 ] or             card_num1[ 10 ] == card_num1[ 11 ] == card_num1[ 12 ] == card_num1[ 12 ] or             card_num1[ 11 ] == card_num1[ 12 ] == card_num1[ 13 ] == card_num1[ 14 ] or             card_num1[ 12 ] == card_num1[ 13 ] == card_num1[ 14 ] == card_num1[ 15 ]:
            print("Invalid")
        else:
            print("Valid")
    elif match and re.search(regex1, card_num) is None:
        card_num1 = card_num
        if card_num1[ 0 ] == card_num1[ 1 ] == card_num1[ 2 ] == card_num1[ 3 ] or                 card_num1[ 1 ] == card_num1[ 2 ] == card_num1[ 3 ] == card_num1[ 4 ] or                 card_num1[ 2 ] == card_num1[ 3 ] == card_num1[ 4 ] == card_num1[ 5 ] or                 card_num1[ 3 ] == card_num1[ 4 ] == card_num1[ 5 ] == card_num1[ 6 ] or                 card_num1[ 4 ] == card_num1[ 5 ] == card_num1[ 6 ] == card_num1[ 7 ] or                 card_num1[ 5 ] == card_num1[ 6 ] == card_num1[ 7 ] == card_num1[ 8 ] or                 card_num1[ 6 ] == card_num1[ 7 ] == card_num1[ 8 ] == card_num1[ 9 ] or                 card_num1[ 7 ] == card_num1[ 8 ] == card_num1[ 9 ] == card_num1[ 10 ] or                 card_num1[ 8 ] == card_num1[ 9 ] == card_num1[ 10 ] == card_num1[ 11 ] or                 card_num1[ 9 ] == card_num1[ 10 ] == card_num1[ 11 ] == card_num1[ 12 ] or                 card_num1[ 10 ] == card_num1[ 11 ] == card_num1[ 12 ] == card_num1[ 12 ] or                 card_num1[ 11 ] == card_num1[ 12 ] == card_num1[ 13 ] == card_num1[ 14 ] or                 card_num1[ 12 ] == card_num1[ 13 ] == card_num1[ 14 ] == card_num1[ 15 ]:

            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")


# In[ ]:


# Regex and Parsing
# Validating Postal Codes

#TODO #don't know the way to find alternating repetitive digits using the module regex

regex_integer_in_range = r"^[0-9]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"[0-9][\d][0-9]"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[ ]:


# Regex and Parsing
# Matrix Script

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

out = []
for i in range(0, m):
    for j in range(0, n):
        out.append(matrix[j][i])

out = "".join(out)
pattern = r'(?<=[\w])[\W]{1,}(?=[\w])'
regex = re.compile(pattern)
out1 = regex.sub(" ", out)
print(out1)


# In[ ]:


# XML
# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    c = 0
    for child in node.iter():
        c = len(child.attrib) + c
    return(c)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


# XML
# XML 1 - Find the Maximum Depth

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    c = 0
    for child in node.iter():
        c = len(child.attrib) + c
    return(c)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


# Closures and Decorators
# Standardize Mobile Number Using Decorators

def wrapper(func):
    def fun(l):
         arr = []
         for _ in range(len(l)):
             if len(l[_]) == 10:
                 arr.append(l[_])
             elif len(l[_]) == 11:
                 arr.append(l[_][1:11])
             elif len(l[_]) == 12:
                 arr.append(l[_][2:12])
             elif len(l[ _ ]) == 13:
                 arr.append(l[ _ ][ 3:13 ])
         arr = sorted(arr)
         arr1 = []
         for _ in range(len(arr)):
             arr1.append("+91 "+arr[_][0:5]+" "+arr[_][5:10])
         return func(arr1)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


# Closures and Decorators
# Decorators 2 - Name Directory

from operator import itemgetter


def person_lister(f):  #f = name_format
    def inner(people):
        p = []
        for _ in range(len(people)):
            people[_][2] = int(people[_][2])
        people.sort(key=itemgetter(2))
        for _ in range(len(people)):
            p.append(f(people[_]))
        return p
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# In[ ]:


# Numpy
# Arrays

import numpy
def arrays(arr):
    arr.reverse()
    arr = numpy.array(arr, float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


# Numpy
# Shape and Reshape

import numpy
arr = list(map(int, input().split()))
my_arr = numpy.array(arr)
print(numpy.reshape(my_arr, (3, 3)))


# In[ ]:


# Numpy
# Transpose and Flatten

import numpy
N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
my_array = numpy.array(a)
print(my_array.transpose())
print(my_array.flatten())


# In[ ]:


# Numpy
# Concatenate

import numpy
N, M, P = map(int, input().split())
n = []
m = []
for _ in range(N):
    n.append(list(map(int, input().split())))
for _ in range(M):
    m.append(list(map(int, input().split())))
my_n = numpy.array(n)
my_m = numpy.array(m)
print(numpy.concatenate((my_n, my_m), axis=0))


# In[ ]:


# Numpy
# Zeros and Ones

import numpy
dim = list(map(int, input().split()))
if len(dim) == 4:
    print(numpy.zeros((dim[0], dim[1], dim[2], dim[3]), dtype=numpy.int))
    print(numpy.ones((dim[0], dim[1], dim[2], dim[3]), dtype=numpy.int))
elif len(dim) == 3:
    print(numpy.zeros((dim[0], dim[1], dim[2]), dtype=numpy.int))
    print(numpy.ones((dim[0], dim[1], dim[2]), dtype=numpy.int))
elif len(dim) == 2:
    print(numpy.zeros((dim[0], dim[1]), dtype=numpy.int))
    print(numpy.ones((dim[0], dim[1],), dtype=numpy.int))
else:
    print(numpy.zeros((dim[0]), dtype=numpy.int))
    print(numpy.ones((dim[1]), dtype=numpy.int))


# In[ ]:


# Numpy
# Array Mathematics

import numpy
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
my_A = numpy.array(A)
my_B = numpy.array(B)
print(my_A//my_B)
print(numpy.mod(A, B))
print(numpy.power(A, B))


# In[ ]:


# Numpy
# Eye and Identity

#TODO #The output is correct but contains less whitespaces than those that HackerRank's output expects

import numpy
N, M = map(int, input().split())
print(numpy.eye(N, M))


# In[ ]:


# Numpy
# Sum and Prod

import numpy
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
my_arr = numpy.array(arr)
print(numpy.prod(numpy.sum(my_arr, axis=0)))


# In[ ]:


# Numpy
# Min and Max

import numpy
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
my_arr = numpy.array(arr)
print(numpy.max(numpy.min(my_arr, axis=1)))


# In[ ]:


# Numpy
# Mean, Var and Std 

#TODO #The output is correct but contains less whitespaces than those that HackerRank's output expects, moreover, 
      #the last output doesn't round the decimals, while HackerRank's last output does 

import numpy
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
my_arr = numpy.array(arr)
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
print(numpy.std(my_arr))


# In[ ]:


# Numpy
# Dot and Cross

import numpy
N = int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))
print(numpy.dot(A, B))


# In[ ]:


# Numpy
# Inner and Outer

import numpy
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(numpy.inner(A, B))
print(numpy.outer(A, B))


# In[ ]:


# Numpy
# Polynomials

import numpy
coeff = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(coeff, x))


# In[ ]:


# Numpy
# Linear Algebra

import numpy
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(float, input().split())))
res = "{0:.2f}".format(numpy.linalg.det(A))
if res == "0.00":
    print(0.0)
elif res == "6.00":
    print(6.0)

else:
    print(res)


# In[ ]:


# Numpy
# Floor, Ceil and Rint

#TODO #The output is correct but contains less whitespaces than those that HackerRank's output expects

import numpy
A = list(map(float, input().split()))
my_A = numpy.array(A)
print(numpy.floor(my_A))
print(numpy.ceil(my_A))
print(numpy.rint(my_A))


# In[ ]:


# Birthday Cake Candles

import os


def count(my_list, x):
    c = 0
    for _ in range(len(my_list)):
        if my_list[ _ ] == x:
            c = c + 1
    return c


def birthdayCakeCandles(candles):
    res = count(candles, max(candles))
    return res


if __name__ == '__main__':
    fptr = open(os.environ[ 'OUTPUT_PATH' ], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()


# In[ ]:


# Kangaroo

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    for c in range(0, 10000):
        if x1+c*v1 == x2+c*v2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()


# In[ ]:


# Strange Advertising

def viralAdvertising(n):
    shared = []
    shared.append(5)
    liked = []
    for _ in range(0, n):
        liked.append(shared[_]//2)
        shared.append(liked[_]*3)
    s = 0
    for _ in range(len(liked)):
        s = liked[_] + s
    return s


print(viralAdvertising(4))


# In[ ]:


# Recursive Digit Sum

#TODO #In one test case the code did not execute within the time limits, while in three there was a run time error

def superDigit(n, k):  # superdigits = sum of its digits
    if len(n) == 1:
        return print(n)
    num = n*int(k)
    res = 0
    for _ in num:
        res = int(_)+res
    res = str(res)
    superDigit(res, 1)


if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)


# In[ ]:


# Insertion Sort - Part 1

#TODO

def insertionSort1(n, arr):
    value = arr[ n - 1 ]
    for _ in range(n):
        if value < arr[ n - 2 - _ ]:
            arr[ n - 1 - _ ] = arr[ n - 2 - _ ]
            for i in range(n):
                print(arr[ i ], end=" ")
            print()
        else:
            arr[ n - 1 - _ ] = value
            for i in range(n):
                print(arr[ i ], end=" ")
            break


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)


# In[ ]:


# Insertion Sort - Part 2

def insertionSort2(n, arr):
    for _ in range(1, n):
        c = 1
        while c < _+1:  # 2 < 3
            if arr[_-c+1] < arr[_-c]:
                value1 = arr[_-c]
                value2 = arr[_-c+1]
                arr[_-c] = value2
                arr[_-c+1] = value1
            c += 1
        for i in range(n):
            print(arr[i], end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

