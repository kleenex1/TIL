def dice_prize(dice_numbers):
    price = 0
    if len(set(dice_numbers)) == 1:
        price = 10000 + dice_numbers[0] * 1000
    elif len(set(dice_numbers)) == 3:
        price = max(dice_numbers) * 100
    else:
        price = 1000 + (sum(dice_numbers)- sum(list(set(dice_numbers)))) * 100    

    return price


if __name__ == "__main__":
    dice_numbers = list(map(int, input().split()))
    print(dice_prize(dice_numbers))
    
    