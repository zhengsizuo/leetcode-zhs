class Solution():
    def __init__(self):
        self.ret = ''
        self.count = 0
    def solution(self, N, M, K):
        choices = ['a', 'b']
        def backtrack(N, M, K, path):
            if self.count == K:
                self.ret = path
            if N==0 and M==0:
                return

            for i in range(len(choices)):
                if N==0 and choices[i]=='a':
                    continue
                if M==0 and choices[i]=='b':
                    continue
                path += choices[i]
                # result.append(path)
                self.count += 1

                if choices[i] == 'a':
                    N -= 1
                if choices[i] == 'b':
                    M -= 1
                backtrack(N, M, K, path)
                if path[-1] == 'a': N += 1
                if path[-1] == 'b': M += 1
                path = path[:-1]

        backtrack(N, M, K, '')
        return self.ret



N, M, K = [int(i) for i in input().split()]
sl = Solution()
print(sl.solution(N, M, K))
