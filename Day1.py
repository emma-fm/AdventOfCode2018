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

#Get input
frq_changes = input("> Enter the frequency changes: ")
string_array = frq_changes.split()

#Removes unnecessary commas, if there's any
string_array = [s.replace(",", "") for s in string_array]

#String to int
number_array = []
for f in string_array:
    number_array.append(int(f))

#Get result frequency (Part 1)
result = 0
for n in number_array:
    result += n
print("The resulting frequency is: " + str(result))

#Get first repeated frequency (Part 2)
#NOTE: Might take a while! (i'm sure this can be optimized, currently does ~140000 loops for the challenge input)
result = 0
any_frequency_repeated = False
repeated_frequency = 0
old_frequencies = [0]
loop = 0
while (any_frequency_repeated == False):
    for n in number_array:
        result += n
        loop = loop + 1
        if result in old_frequencies:
            repeated_frequency = result
            any_frequency_repeated = True
            break
        else:
            old_frequencies.append(result)
print("The first repeated frequency is: " + str(repeated_frequency))