class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def recurse(i,j,sa,sb):
            if i > j:
                return sa > sb
            if (i,j,sa,sb) in dp:
                return dp[(i,j,sa,sb)]
            if (j - i)%2:
                dp[(i,j,sa,sb)] = (recurse(i+1,j,sa+piles[i],sb) or recurse(i,j-1,sa+piles[j],sb))
            else:
                dp[(i,j,sa,sb)] = (recurse(i+1,j,sa,sb+piles[i]) or recurse(i,j-1,sa,sb+piles[j]))
            return dp[(i,j,sa,sb)]
        
        return recurse(0,len(piles) - 1,0,0)
