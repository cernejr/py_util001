import sys
MIN_PYTHON = (3, 7)
#print(sys.version_info)
assert sys.version_info >= MIN_PYTHON, f"requires Python {'.'.join([str(n) for n in MIN_PYTHON])} or newer"

###main

if (len(sys.argv) != 3):
	print("Usage: comm.py <fn1> <fn2>")
	sys.exit(-1)

v1 = list()
with open('a002.txt') as f:
    v1 = f.readlines()

v2 = list()
with open('b002.txt') as f:
    v2 = f.readlines()
    
m1 = set(v1)    
m2 = set(v2)
mCommon = m1.intersection(m2)
md1 = m1.difference(mCommon)
md2 = m2.difference(mCommon)

vC = sorted(list(mCommon))
vLeftOnly = sorted(list(md1))
vRightOnly = sorted(list(md2))
  
with open('common.txt', mode='wt', encoding='utf-8') as fC:
	for sLine in vC:
		fC.write(sLine)
#
with open('LeftOnly.txt', mode='wt', encoding='utf-8') as fL:
	for sLine in vLeftOnly:
		fL.write(sLine)
#
with open('RightOnly.txt', mode='wt', encoding='utf-8') as fR:
	for sLine in vRightOnly:
		fR.write(sLine)
#
