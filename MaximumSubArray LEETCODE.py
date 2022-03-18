# USING SLIDING WINDOW
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray=nums[0]
maxCurSum=0
for element in nums:
    #print("cur",maxCurSum)
    #print("Max Sub",maxSubArray)
    if(maxCurSum<0):
        maxCurSum=0
    maxCurSum+=element
    maxSubArray=max(maxSubArray,maxCurSum)
print(maxSubArray)
