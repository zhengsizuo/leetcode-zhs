"""超出时间限制，建图时复杂度为O(n*wordlen)"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList: return 0

        neighbour_dict = dict()

        def find_neighbour(word):
            # 查找与单词word编辑距离等于1的单词
            for w in wordList:
                if w == word: continue
                cnt = 0
                for i in range(len(w)):
                    if w[i] == word[i]:
                        cnt += 1

                if cnt == len(word) - 1:
                    neighbour_dict.setdefault(word, [])
                    neighbour_dict[word].append(w)

        find_neighbour(beginWord)
        for w in wordList:
            find_neighbour(w)

        # print(neighbour_dict)
        visited = set()
        queue = [(beginWord, 1)]
        while queue:
            # print(queue)
            head, level = queue.pop(0)
            visited.add(head)
            if head not in neighbour_dict:
                return 0
            for node in neighbour_dict[head]:
                if node == endWord:
                    return level + 1
                if node not in visited and (node, level) not in queue:
                    queue.append((node, level + 1))

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList: return 0

        neighbour_dict = dict()
        wordList = set(wordList)
        def find_neighbour(word):
            # 生成与单词word编辑距离等于1的单词，若该单词在字典中加入图
            word_list = list(word)
            for i in range(len(word)):
                word_copy = word_list.copy()
                for k in range(26):
                    word_copy[i] = chr(ord('a')+k)
                    next_word = ''.join(word_copy)
                    if next_word in wordList and next_word!=word:
                        neighbour_dict.setdefault(word, [])
                        neighbour_dict[word].append(next_word)

        find_neighbour(beginWord)
        for w in wordList:
            find_neighbour(w)

        # print(neighbour_dict)
        visited = set()
        queue = [(beginWord, 1)]
        while queue:
            # print(queue)
            head, level = queue.pop(0)
            visited.add(head)
            if head not in neighbour_dict:
                return 0
            for node in neighbour_dict[head]:
                if node == endWord:
                    return level + 1
                if node not in visited and (node, level) not in queue:
                    queue.append((node, level + 1))

        return 0


"""官方题解用h*t通配符作键"""
"""双向BFS"""

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
sl = Solution()
print(sl.ladderLength(beginWord, endWord, wordList))