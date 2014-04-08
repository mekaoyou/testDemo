# coding=UTF-8

import string;
from math import *;


# l = [1,2,3,4,5,6];
# print l;
# l.reverse();
# print l;

# l = "123456";
# print l;
# nl = [];
# for i in range(len(l) - 1,-1,-1):
# 	nl.append(l[i]);
# print nl;

# ns = "".join(str(e) for e in nl);
# print ns;

# print '654321';

# a={1:'a',2:'b',3:'c'};
# print a;

# # l = [];
# # for i in a:
# # 	l.append(i);
# print ",".join(str(e) for e in a);

# a = '1234567890';
# l = [];
# # for i in xrange(0,len(a),2):
# # 	l.append(a[i]);
# print "".join(a[i] for i in xrange(0,len(a),2));

# for i in range(2,101):
#     fg = 0;
#     for j in range(2,i/2):
#         if (i % j ==0):
#             fg = 1;
#     if (fg == 0):
#         print str(i) + " ";

# s = [2];
# for i in xrange(3,100000):
# 	isS = True;
# 	for j in xrange(0,len(s)):
# 		if i%s[j] == 0:
# 			isS = False;
# 			break;
# 	if isS == True:
# 		s.append(i);
# print s;


#print [x for x in xrange(2,100) if not [y for y in xrange(2,x) if x % y == 0]];

# l = [0,1,2,3,5,5,6,7];
# l.sort();
# if len(l)%2 != 0:
# 	print l[len(l)/2];
# else:
# 	m = l[len(l)/2] + l[len(l)/2+1];
# 	if m%2 == 0:
# 		print m/2;
# 	else:
# 		print m/2.0;

# a = 10;
# print bin(a)
# print hex(a)
# print bin(a)[2:]
# print "0101010101010".count("1")
# print (bin(a)[2:]).count('1')
# print this.s;

# st = map(int,"00:00:01".split(":"));
# et = map(int,"01:34:20".split(":"));
# print st,et;
# dif = 0;
# for e,s in zip(et,st):
# 	print e,s;

def checkTriangle(a,b,c):
	if (a+b) > c:
		return True;
	else:
		return False;

# print checkTriangle(1,2,3);

def parseDatetime(p_dt):
	if len(p_dt) == 1:
		return '0'+str(p_dt);
	else:
		return p_dt;
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'};
# print t['year'] + "-" + parseDatetime(t['month']) + "-" + parseDatetime(t['day']) + " " + parseDatetime(t['hour']) + ":" + parseDatetime(t['minute']) + ":" + parseDatetime(t['second']);

def function1():
	l = [2,24,54,6,8,87];
	print [i/l[0] for i in l];

# function1();

def abDefinePos():
	l = [];
	for i in xrange(1,10):
		for j in xrange(1,10):
			if i%3 == j%3:
				continue;
			l.append('A' + str(i) + 'B' + str(j));
	return l;

# print abDefinePos();


def insert_sort(p_list):
  if len(p_list) <= 1:
  	return p_list;
  r_list = [p_list[0]];  
  for i in xrange(1,len(p_list)):
  	for j in xrange(len(r_list)-1,-1,-1):
  	  if p_list[i] >= r_list[j]:
  	  	r_list[j+1:0] = [p_list[i]];
  	  	break;
  	  if j == 0:
  	  	r_list[0:0] = [p_list[i]];
  return r_list;

# print insert_sort([0,1,1,0,9,2,-1,0.5,1.1,20,3,99,200]);

def insertion_sort(p_list):
  if len(p_list) <= 1:
    return p_list;
  b = insertion_sort(p_list[1:]);
  m = len(b);
  for i in xrange(m):
    if p_list[0] <= b[i]:
      return b[:i] + [p_list[0]] + b[i:];
  return b + [p_list[0]];

# print insertion_sort([1,2,0,4,5,6,7,23,4]);
# print insert_sort([1,2,0,4,5,6,7,23,4]);




def merge(p_list,p_start,p_mid,p_end):
  left_list = p_list[p_start:p_mid+1];
  right_list = p_list[p_mid+1:p_end+1];
  left_index = right_index = 0;
  for i in xrange(p_start,p_end+1):
    if left_index >= len(left_list) or right_index >= len(right_list):
      break;
    if left_list[left_index] <= right_list[right_index]:
      p_list[i] = left_list[left_index];
      left_index += 1;
    else:
      p_list[i] = right_list[right_index];
      right_index += 1;
  if left_index >= len(left_list):
    p_list[i:p_end+1] = right_list[right_index:len(right_list)];
  else:
    p_list[i:p_end+1] = left_list[left_index:len(left_list)];


def merge_sort(p_list,p_start,p_end):
  if p_start < p_end:
    mid = (p_start + p_end) >> 1;
    merge_sort(p_list,p_start,mid);
    merge_sort(p_list,mid+1,p_end);
    merge(p_list,p_start,mid,p_end);

a = [3,2,0];
l = len(a)
# merge_sort(a,0,len(a)-1);
# print l,a,len(a);

def bubble_sort(p_list):
  for i in xrange(len(p_list)-1,0,-1):
    for j in xrange(0,i):
      if p_list[j] > p_list[j+1]:
        p_list[j],p_list[j+1] = p_list[j+1],p_list[j];
  return p_list;

# print bubble_sort([4,25,52,2,5,6,0]);

def format_rmb(p_rmb):
  rmbList = list(str(p_rmb));
  for i in xrange(0,len(rmbList)-1):
    rmbList[i] = getNum(int(rmbList[i]));
  sbqw = ['万','仟','佰','拾','万','仟','佰','拾','圆'];
  rmbIndex = len(sbqw) - 1;
  for j in xrange(len(rmbList),0,-1):
    rmbList[j:0] = sbqw[rmbIndex];
    rmbIndex -= 1;
  rmbStr = "".join(rmbList);  
  return rmbStr;

def getNum(p_int):
  if p_int == 1:
    return "壹";
  elif p_int == 2:
    return "贰";
  elif p_int == 3:
    return "叁";
  elif p_int == 4:
    return "肆";
  elif p_int == 5:
    return "伍";
  elif p_int == 6:
    return "陆";
  elif p_int == 7:
    return "柒";
  elif p_int == 8:
    return "捌";
  elif p_int == 9:
    return "玖";

import math;
print math.sqrt((3**2 + 4**2));

print "test";









