#https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28


def a_n_k(a, n, k, depth, used, curr, ans):
    '''
    Implement permutation of k items out of n items
    :param a: List of items
    :param n: len of a
    :param k: permutation of k items out of n items
    :param depth: start from 0 and represent the depth of the search
    :param used: track what items are in the partial solution from the set of n
    :param curr: the current partial solution
    :param ans: collect all the valide solutions
    :return:
    '''
    if depth == k: # end condition
        ans.append(curr[::]) # use deepcopy because curr is tracking all partial solution
        # print('ans: ', ans)
        return

    for i in range(n):
        if not used[i]:
            # generate the next solution from curr
            curr.append(a[i])
            used[i] = True
            print('current: ', curr)
            # move to the next solution
            a_n_k(a, n, k, depth+1, used, curr, ans)

            #backtrack to previous partial state
            print('current after recursion: ', curr)
            curr.pop()
            print('backtrack: ', curr)
            used[i] = False
    return


a = [1, 2, 3]
n = len(a)
# ans = [[None]]
used = [False] * len(a)
ans = []
a_n_k(a, n, n, 0, used, [], ans)
print(ans)