# coding=utf-8
import random

team = []

#read teams' name
f = open('Contestants.txt','r')
for name in f.readlines():
	team.append(name)
f.close()

#before shuffle
print('參賽隊伍:')
for i in range(len(team)):
	print(i)
	print(team[i])

print('---------------------------')

#suffle
print('抽籤結果:')
random.shuffle(team)
for i in range(1,len(team)):
	print(i)
	print(team[i])