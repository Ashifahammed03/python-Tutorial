total_seconds = int(input("Enter time in seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
