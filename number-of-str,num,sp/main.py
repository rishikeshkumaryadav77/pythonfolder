##find num, str, sp witout methods
a = "10kcoders@gmail.com"
num = "1234567890"
alp = "abcdefghijklmnopqrstuvwxyz"
count_num = 0
count_alp = 0
count_sp = 0
for i in a:
  if i in num:
    count_num += 1
  elif i in alp:
    count_alp += 1
  else:
    count_sp += 1
print("number", count_num)
print("alp", count_alp)
print("sp", count_sp)

##or
input = "10kcoders@gmail.com"
num,alpha,sp=0,0,0
for i in input:
  if i>= "0" and i<= "9":
    num += 1
  elif (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
    alpha += 1
  else:
    sp += 1
print("num", num)
print("alp", alpha)
print("sp", sp)