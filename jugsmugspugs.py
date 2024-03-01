number = int(input("Enter the number :"))
res=""
if  number %3 ==0:
  res+="jugs"
if  number %5 ==0:
  res+="mugs"
if number %7 ==0:
  res+="pugs"
print(res)

number = int(input("Enter the number :"))
string = str(number)
result =[]
res=""
if  number %3 ==0:
  result.append("jugs")
if  number %5 ==0:
  result.append("mugs")
if number %7 ==0:
  result.append("pugs")

for i in range(len(result)):
  res += result.pop()
print(res)
