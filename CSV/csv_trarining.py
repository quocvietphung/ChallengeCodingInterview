import csv

f = open("my.csv","a",newline="")
tup = ("bob", 19)
writer = csv.writer(f)
writer.writerow(tup)
f.close()
