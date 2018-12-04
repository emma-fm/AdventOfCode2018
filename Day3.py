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

def isInClaimed(index, claim_array, twice_array):
        coord = claim_array[index].rsplit(":")[0]
        dimension = claim_array[index].rsplit(":")[1][1:]
        x = int(coord.rsplit(",")[0])
        y = int(coord.rsplit(",")[1])
        width = int(dimension.rsplit("x")[0])
        height = int(dimension.rsplit("x")[1])
        for i in range(0, width):
            for j in range(0, height):
                pos = str(x + i) + "," + str(y + j)
                if pos in twice_array:
                    return True
        return False


# Get input, remove commas
claims_string = input(">Enter the list of IDs, sepparated by ';'. For challenge entry, type 'challenge': ")
if claims_string == "challenge":
    claims = ep.EntryProcessor.getEntryArray(r"input/Day3.txt")
else:
    claims = claims_string.split(";")
    claims = [s.replace(";", "") for s in claims]

# The first 4 characters are unnecesary (index + # + space + @)
# The array index can be used as the claim index, BUT WITH ONE IMPORTANT NOTE:
# CLAIM INDEXES START AT 1, NOT 0! THAT MEANS WE NEED TO ADD 1!
for i in range(0, len(claims)):
    claims[i] = claims[i].rsplit("@", 1)[1][1:]

# For each value of the array, saves its used coordinates at a list ("claimed") as a string in the format "x,y"
# If the current value is already at "claimed" it is added to the list "twice" (but only once)
# The answer to the problem is the length of "twice"
# NOTE: takes A LOT of time for the challenge input!!! Up to 30 minutes for me. Definitely not the best approach.
claimed = []
twice = []
for c in claims:
    coord = c.rsplit(":")[0]
    dimension = c.rsplit(":")[1][1:]
    x = int(coord.rsplit(",")[0])
    y = int(coord.rsplit(",")[1])
    width = int(dimension.rsplit("x")[0])
    height = int(dimension.rsplit("x")[1])
    for i in range(0, width):
        for j in range(0, height):
            pos = str(x + i) + "," + str(y + j)
            if pos not in claimed:
                claimed.append(pos)
            elif pos not in twice:
                twice.append(pos)
print("The number of square inches claimed 2 or more times is: " + str(len(twice)))

# Part 2: For each claim, we check all its coordinates to see if they're in twice.
# If one coordinate is, we jump to the next claim
index = 0
for c in claims:
    if not isInClaimed(claims.index(c), claims, twice):
        index = claims.index(c) + 1
        break
print("The only claim without any square inch claimed by another is: " + str(index))