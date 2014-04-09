import sys;

data = [
	[35864,6321569,23438191,639521,61235253],		#1             
	[8124861,1509,419347,32854,4792642],			#2              
	[1025,175346,4241932,368372,27629],				#3
	[431822,207835062,93528,7251382,61173824],		#4	
	[41257,38761533,234569,56149217,87762],			#5
	[5417693,49134256,32657,6532841,320736074],		#6
];

def canculate(p_groupNum,p_startPage,p_stopPage):
  result = 0;
  for i in xrange(p_startPage-1,p_stopPage):
    result += data[i][p_groupNum-1];
  return "result is :" + formate_num(result);

def formate_num(num):
  lessZero = False;
  if num < 0:
  	lessZero = True;
  	num = -num;
  numList = list(str(num));
  numList[-2:0] = ['.'];
  for i in xrange(len(numList)-6,0,-3):
  	numList[i:0] = [','];
  numStr = "".join(numList);
  if lessZero:
  	numStr = "-" + numStr;
  return numStr;

# canculate(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))