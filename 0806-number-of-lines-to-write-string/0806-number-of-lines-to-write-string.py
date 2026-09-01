class Solution(object):
    def numberOfLines(self, widths, s):
        l=0
        w=0
        j=0
        a="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            ind=a.index(i)
            w+=widths[ind]
            if w==100 :
                l+=1
                w=0
            elif w>100 :
                l+=1
                w=widths[ind]
        if w==0:
            w=100
            l-=1
        return [l+1,w]

        