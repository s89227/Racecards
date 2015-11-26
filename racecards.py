# coding=utf-8
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

team = []
mid_lane = []

#read teams' name
f = open('Contestants_Team.txt','r')
for name in f.readlines():
	team.append(name)
f.close()

#read mids' name
f = open('Contestants_MidLane.txt','r')
for name in f.readlines():
	mid_lane.append(name)
f.close()


#suffle
random.shuffle(team)
random.shuffle(mid_lane)

#print result
print('抽籤結果:')
print('團隊賽:')
for i in range(0,len(team)):
	print(i+1)
	print(team[i])

print('--------------------------------------')
print('中路單挑賽:')
for i in range(0,len(mid_lane)):
	print(i+1)
	print(mid_lane[i])


#write result to file
f = open('Result_Team.txt','a')
for i in range(len(team)):
	f.write(team[i])
f.close()

f = open('Result_MidLane.txt','a')
for i in range(len(mid_lane)):
	f.write(mid_lane[i])
f.close()