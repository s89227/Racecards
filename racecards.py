# coding=utf-8
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""team = []"""
mid_lane = []

"""#read teams' name
f = open('Contestants_Team.txt','r')
for name in f.readlines():
	team.append(name)
f.close()"""

#read mids' name
f = open('Contestants_MidLane.txt','r')
for name in f.readlines():
	mid_lane.append(name)
f.close()


#suffle
"""random.shuffle(team)"""
random.shuffle(mid_lane)


#write result to file
"""f = open('Result_Team.txt','a')
for i in range(len(team)):
	f.write('%d. %s' % (i+1, team[i]))
f.close()"""

f = open('Result_MidLane.txt','a')
for i in range(len(mid_lane)):
	f.write('%d. %s' % (i+1, mid_lane[i]))
f.close()

f = open('Time_MidLane.txt','a')
for i in range(len(mid_lane)):
	f.write('%d. %s' % (i+1, mid_lane[i]))
f.close()

print('抽籤完成!')