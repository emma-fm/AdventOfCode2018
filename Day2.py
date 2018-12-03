'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import EntryProcessor as ep
# Same as day 1: get input and remove any unnecessary commas
id_string = input(">Enter the list of IDs, for challenge input type 'challenge': ")
if id_string == "challenge":
    ids = ep.EntryProcessor.getEntryArray(r"input/Day2.txt")
else:
    ids = id_string.split()
    ids = [s.replace(",", "") for s in ids]

# We get the number of times a letter is repeated 3 times, so we can discard
# them when we count the times a letter is repeated twice.
# Two booleans are made so you don't count more than once if a letter is repeated 2/3 times
three_times = 0
two_times = 0
for i in ids:
    values = []
    counted_twice = []
    counted_thrice = []
    already_counted_three = False
    already_counted_two = False
    for n in i:
        if n in values and n in counted_twice and n not in counted_thrice:
            three_times += 1
            counted_thrice.append(n)
            if already_counted_three:
                three_times -= 1
            else:
                already_counted_three = True
        elif n in values and n not in counted_twice:
            counted_twice.append(n)
        else:
            values.append(n)
    for t in counted_twice:
        if t not in counted_thrice:
            two_times += 1
            if already_counted_two:
                two_times -= 1
            else:
                already_counted_two = True

# Get checksum
print("Your checksum is: " + str(two_times * three_times))   

# Part 2: we compare each ID to everyone in the array and get the most similar ID (mostcoincident)
# as well as the "index of coincidence" (coincidence), which means the nº of common letters
coincidence = []
mostcoincident = []
for i in ids:
    coincidence.append(0)
    mostcoincident.append("")
    for n in ids:
        if i is not n: #The same box
            currentcoincidence = 0
            for l in range(0, len(i)):
                if i[l] == n[l]:
                    currentcoincidence += 1
            if currentcoincidence > coincidence[-1]:
                mostcoincident[-1] = n
                coincidence[-1] = currentcoincidence

# The biggest value of coincidence[] will be the correct box, and its correspondent
# value of mostcoincident[] the other one. We only have to compare them and voilà
maximum = max(coincidence)
box1 = ids[coincidence.index(maximum)]
box2 = mostcoincident[coincidence.index(maximum)]
result = ""
for q in range(0, len(box1)):
    if box1[q] == box2[q]:
        result += box1[q]
print("Common letters: " + result)