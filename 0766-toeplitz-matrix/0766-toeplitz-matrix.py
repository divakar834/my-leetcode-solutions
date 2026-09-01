class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        def get_n_rows() : return len(m)
        def get_n_cols() : return len(m[0])
        def get_val(i,j) : return m[i][j]  
        nr = get_n_rows()
        nc = get_n_cols()
        def diag_indices(d):
            if d >= 0 : i0, j0, k0 = 0,      d, min(nr, nc-d)
            else      : i0, j0, k0 = abs(d), 0, min(nc, nr-abs(d))
            for k in range(k0):
                yield (i0+k, j0+k)
        for d in range(-nr+1,nc):
            v = -1
            for i, j in diag_indices(d):
                if v < 0             : v = get_val(i,j)
                if get_val(i,j) != v : return False
        return True