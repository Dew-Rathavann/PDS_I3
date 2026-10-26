total_seconds = 5401
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = (total_seconds % 3600) % 60
print(hour, minute, second)

print("Checkkkk: ", (hour * 3600) + (minute * 60) + second == total_seconds)