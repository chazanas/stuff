
import datetime as dt
j = []
now1 = dt.datetime.now()
for i in range(1000):
	j.append(i)
now2 = dt.datetime.now()
print((now2 - now1).microseconds)

now3 = dt.datetime.now()

j2 = list(map(lambda x: x, range(1000)))

now4 = dt.datetime.now()
print((now4 - now3).microseconds)

#print(j, j2)