
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    maxcandies = max(candies)
    extracandies = 3
    boolarray = []
    totalcandies = []
    for i in range(0,len(candies)):
        totalcandies = candies[i] + extraCandies
        if totalcandies >= maxcandies :
            boolarray.append("true")
        else:
            boolarray.append("false")
    return boolarray


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
        