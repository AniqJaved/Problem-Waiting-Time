
###########################################################################################################################################################
##Algorithm= So we want to get the waiting timme for eacch query. What we do is that first we sort it and then at each index we multiply that index's value
##           with remaining length. So at 0 index the waiting time for all the queries will take 1 second each resulting to 4 seconds. Similarly at 1 index
             the time taken by remaining queries will be 2 seconds + 1 second (from previous query) each.
###########################################################################################################################################################


queries = [3,2,1,2,6]
waiting_list = []
queries.sort()

for idx,val in enumerate(queries):
    remaining_length = len(queries) - (idx+1)
    waiting_time = queries[idx] * remaining_length
    waiting_list.append(waiting_time)

print(sum(waiting_list))


#####################################################################################################################################################
## Time Complexity = O(nlogn)
## Explanation: It is becuase we are sorting  and the time taken by sorting is nlogn.
## Space Complexity = O(1) or in our case O(n)
## Explanation: It is O(1) when we use a single variable to store the result instead of making list.
######################################################################################################################################################
