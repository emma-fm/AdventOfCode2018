#Get input
frq_changes = input("> Enter the frequency changes: ")
string_array = frq_changes.split()

#Removes unnecessary commas, if there's any
string_array = [s.replace(",", "") for s in string_array]

#String to int
number_array = []
for f in string_array:
    number_array.append(int(f))

#Get result
result = 0
for n in number_array:
    result += n
print("The resulting frequency is: " + str(result))