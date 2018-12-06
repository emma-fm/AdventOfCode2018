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
'''
THIS CHALLENGE WON'T PROBABLY BE FINISHED IN A LONG TIME. SORRY.
'''
import EntryProcessor as ep

# Get input, remove commas
schedules_string = input(">Enter the list of IDs, sepparated by ','. For challenge entry, type 'challenge': ")
if schedules_string == "challenge":
    schedules_string = ep.EntryProcessor.getEntryArray(r"input/Day4.txt")
else:
    schedules_string = schedules_string.split(",")
    schedules_string = [s.replace(",", "") for s in schedules_string]

schedules = {}
asleep = {}
hour = 0
minute = 0
for i in range(0, len(schedules_string)):
    # The first 19 characters of an entry are useless (data, etc,). We read the 19th char:
    char = schedules_string[i][19:20]
    if char == "G": # It's a guard shift
        current_guard = int(schedules_string[i].split("#")[1].split()[0]) # Get guard ID
        if current_guard not in schedules:
            schedules[current_guard] = 0
        asleep[current_guard] = False
        for n in range(i + 1, len(schedules_string)):
            char2 = schedules_string[n][19:20]
            if char2 == "G": # Next guard
                if asleep[current_guard] == True:
                    current_h = int(schedules_string[n][12:14])
                    current_m =  int(schedules_string[n][15:17])
                    hour_diff = abs(current_h - hour)
                    minute_diff = abs(current_m - minute)
                    time = hour_diff * 60 + minute_diff
                    schedules[current_guard] += time
                    asleep[current_guard] = False
                break
            if char2 == "f" and asleep[current_guard] == False: # Falls asleep
                asleep[current_guard] = True
                hour = int(schedules_string[n][12:14])
                minute = int(schedules_string[n][15:17])
            if char2 == "w" and asleep[current_guard] == True: # Wakes up
                current_h = int(schedules_string[n][12:14])
                current_m =  int(schedules_string[n][15:17])
                hour_diff = abs(current_h - hour)
                minute_diff = abs(current_m - minute)
                time = hour_diff * 60 + minute_diff
                schedules[current_guard] += time
                asleep[current_guard] = False
# Get most sleepy guard
most_sleep = 0
guard = 0
for g in schedules:
    if schedules[g] > most_sleep:
        guard = g
        most_sleep = schedules[g]
print(str(guard) + "," + str(schedules[guard]))