def dataLine(line):
  tokens = line.split()
  return [int(tokens[1].replace('.','')),float(tokens[2]),float(tokens[3].replace(';',''))]

file_in = 'test1.txt'
raw = open(file_in, 'r')
data = []

line = raw.readline()
while line != "":
  data.append(dataLine(line))
  line = raw.readline()
  
raw.close()
