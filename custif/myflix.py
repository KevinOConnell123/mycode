#!/usr/bin/env python3
#message = 'The movie is about to begin, we recommend '
#print('What is your connection speed in Mbps?')
#connection = float(input())
#if connection >= 25:
#    message = message + 'setting video to 4k.'
#elif connection >= 5:
#    message = message + 'setting video to 1080p.'
#elif connection >= 2:
#    message = message + 'setting video to 720p.'
#else:
#    message = message + 'finding another access network.'
#print(message)


### Own script

message = 'Is your letter grade for this class is '
print('What is you numeric score?')
numeric_score = float(input())
if numeric_score >= 90:
    message = message + 'A'
elif numeric_score >= 80:
    message = message + 'B'
elif numeric_score >= 70:
    message = message + 'C'
elif numeric_score >= 60:
    message = message + 'D'
elif numeric_score <= 59:
    message = message + 'F'
print(message)
