array = [1,4,7,10,5,2,3]

target = int(input("Enter the sum you want:"))

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num]=i
    return []

print(two_sum(array,target))