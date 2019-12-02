import sys
fd=open("logger.txt", "w")
sys.stdout=fd
True
print("test")
