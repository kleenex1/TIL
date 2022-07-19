def oven_clock(hour, minute, cooking_time):
    minute += cooking_time
    extra_hour = 0
    
    if minute > 59:
        extra_hour = minute // 60
        minute = minute % 60
        
    hour += extra_hour
    
    hour = hour % 24
    
    return f"{hour} {minute}"

if __name__ == "__main__":
    hour, minute = map(int, input().split())
    cooking_time = int(input())
    finish_time = oven_clock(hour=hour, minute=minute, 
                             cooking_time=cooking_time)
    print(finish_time)