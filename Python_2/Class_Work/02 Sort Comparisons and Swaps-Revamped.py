######################################################################
##Name: Broady Rivet                                                ##
##Date: 12/12/18                                                    ##
##Description: Code sorts given list using bubble, optimized bubble,##
##             insertion, and selection sorts                       ##
######################################################################


# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]


## Set names ##
Orig = getList()
nums = getList()
Sorted = getList()
Sorted.sort()

# the bubble sort function
# input: a list of integers
def BubbleSort(nums):
    Compcount, Swapcount = 0, 0
    for i in range (1, len(nums)):
        for j in range (1, len(nums)-i + 1):
            Compcount += 1
            if nums[j] < nums[j - 1]:
                Swapcount += 1
                temp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = temp
# output: a number of comparisons and swaps
    return Compcount, Swapcount


# the optimized bubble sort function
# input: a list of integers
def OptBubble(nums):
    OptComp, OptSwap = 0, 0
    nums = getList()
    changed = False
    for i in range(1, len(nums)):
        changed = False
        for j in range(1, len(nums) - i + 1):
            OptComp += 1
            if nums[j] < nums[j - 1]:
                sub = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = sub
                OptSwap += 1
                changed = True
        if changed != True:
            break
# output: a number of comparisons and swaps
    return OptComp, OptSwap

# the Selection sort function
# input: a list of integers
def Selection(nums):
    SelComp, SelSwap = 0, 0
    for i in range(len(nums) - 1):
        miny = i
        for j in range (i + 1, len(nums)):
            SelComp += 1
            if nums[miny] > nums[j]:
                miny = j
        SelSwap += 1
        temp = nums[i]
        nums[i] = nums[miny]
        nums[miny] = temp
# output: a number of comparisons and swaps
    return SelComp, SelSwap

# the Insertion sort function
# input: a list of integers
def Insertion(nums):
    InsertComp, InsertSwap = 0, 0
    nums = getList()
    x = 0
    while x + 1 <= len(nums)-1:
        i = x + 1
        curr_val = nums[i]
        InsertComp += 1
        InsertComp += 1
        while 0<i and nums[i-1] > curr_val:
            nums[i] = nums[i-1]
            i=i-1
            InsertComp += 1
            InsertSwap += 1
        nums[i] = curr_val
        x = x + 1
# output: a number of comparisons and swaps
    return InsertComp, InsertSwap
        
#########################
##    The Main Part    ##
##    of the Program   ##
#########################
compbub, swapbub = BubbleSort(nums)
print "The Original List: {}".format(Orig)
print "After bubble Sort: {}".format(Sorted)
print "{} comparisons; {} swaps".format(compbub, swapbub)
print

OptComp, OptSwap = OptBubble(nums)
print "The Original List: {}".format(Orig)
print "After optimized bubble Sort: {}".format(Sorted)
print "{} comparisons; {} swaps".format(OptComp, OptSwap)
print

SelComp, SelSwap = Selection(nums)
print "The Original List: {}".format(Orig)
print "After selection Sort: {}".format(Sorted)
print "{} comparisons; {} swaps".format(SelComp, SelSwap)
print

InsertComp, InsertSwap = Insertion(nums)
print "The Original List: {}".format(Orig)
print "After insertion Sort: {}".format(Sorted)
print "{} comparisons; {} swaps".format(InsertComp, InsertSwap)
print
