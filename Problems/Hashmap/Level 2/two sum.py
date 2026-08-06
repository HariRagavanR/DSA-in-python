nums = [1,2,7,11,15]

target = 9

hashmap = {}

for i in range(len(nums)):
    complement = target - nums[i]

    if complement in hashmap:
        print([hashmap[complement],i])

    hashmap[nums[i]] = i