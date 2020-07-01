
fileName = input("Enter fileName: ")

def getEmail(line):
   # return a list containing emails in the line
   words = line.split(" ")
   email = []
   for word in words:
      if '@' in word:
         email.append(word)
   return email

#open the file
file = open(fileName,"r")
emails = []
# get the 
for line in file:
   if '@' in line:
      email = getEmail(line) #get the string before the @
      emails.append(email)
print(emails)


file.close() #close the file