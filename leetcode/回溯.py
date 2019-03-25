class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        b = []
        def temp(yiyou,t,cand):
            if t in cand:
                b.append(yiyou+[t])
            if t > cand[0]:
                for i in range(len(cand)):
                    temp(yiyou+[cand[i]],t-cand[i],cand[i:])
        temp([],target,candidates)
        print(b)
        return b

if __name__=='__main__':
    a=Solution()

    b_list=a.combinationSum([2,3,6,7],7)
    print(b_list)