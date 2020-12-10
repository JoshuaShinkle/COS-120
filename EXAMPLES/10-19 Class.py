def main():
  inputFile = open("studentData.txt", 'r')
  outputFile = open("report.txt", 'w')
  for line in inputFile:
    lst = line.split()
    total = 0
    for i in range(2, len(lst)):
      total = total + int(lst[i])
    avg = total / (len(lst)-2)
    print("%6s %6s %5.1f" % (lst[0], lst[1], avg))

    outputFile.write("%6s %6s %5.1f \n" % (lst[0], lst[1], avg))

  inputFile.close()
  outputFile.close()
  
main()