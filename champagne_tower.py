def champagneTower( poured: int, query_row: int, query_glass: int) -> float:
    
    glasses = [poured]
    
    for _ in range(query_row):
        next_level = [0] * (len(glasses)+1)
        for i in range(len(glasses)):
            p = glasses[i]-1
            if p > 0:
                next_level[i] += p/2
                next_level[i+1] += p/2
        glasses = next_level
        
    return min(1,glasses[query_glass])

# Time Complexity : O(n²)
# Space Complexity : O(n)