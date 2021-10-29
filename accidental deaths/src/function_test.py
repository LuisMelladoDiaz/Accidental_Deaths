from function import *
file = r'C:\Users\mella\OneDrive\Escritorio\accidental deaths\data\accidental_deaths.csv'
registers = read_data (file)
print ('Register read', len(registers))
print (registers[:3])
print (registers[-3:])