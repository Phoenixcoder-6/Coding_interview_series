def goal_matching(A,B):
    result=[]
    for b in B:
        count= sum(1 for a in A if a<b)
        result.append(count)

    return result

teamA=[1,2,4,3]
teamB=[3,2]
res= goal_matching(teamA,teamB)
print(res)