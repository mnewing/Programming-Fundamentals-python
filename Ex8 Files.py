# open a file for writting and wriet some text to it
# close it
# open the same file for reading and print out the contents

# =================
# Possible Solution

f = open(r"C:\\dev\temp\demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open(r"C:\\dev\temp\demofile2.txt", "r")
print(f.read())# Write your code here :-)
