public class Solution
{
    public int ClimbStairs(int n)
    {
        Dictionary<int, int> memo = new Dictionary<int, int>();
        return TotalWaysPossible(0, n, memo);
    }

    private int TotalWaysPossible(int cS, int tS, Dictionary<int, int> memo)
    {
        if (cS == tS)
        {
            return 1;
        }
        if (cS > tS)
        {
            return 0;
        }

        int currentKey = cS;

        if (memo.ContainsKey(currentKey))
        {
            return memo[currentKey];
        }

        int oneJump = TotalWaysPossible(cS + 1, tS, memo);
        int twoJumps = TotalWaysPossible(cS + 2, tS, memo);

        memo[currentKey] = oneJump + twoJumps;
        return oneJump + twoJumps;
    }
}


