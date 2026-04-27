def permute(nums):
    result=[]
    def backtrack(path,used):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            backtrack(path,used)
            path.pop()
            used[i]=False
    backtrack([],[False]*len(nums))
    return result
nums=[1,2,3]
print("permutations:",permute(nums))
print("permutations:",permute([0,1]))
print("permutations:",permute([1]))
