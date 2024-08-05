# https://leetcode.com/problems/prefix-and-suffix-search/

# 사전에서 접두가 pref와 접미사가 있는 단어의 인덱스를 반환
# 유효한 인덱스가 두 개 이상 있는 경우 가장 큰 인덱스를 반환
# 사전에 해당 단어가 없는 경우 -1 반환
# apple 입력 후 a, e를 입력하면 0 반환

# 각 요소 중 접두사와 접미사가 같이 일치하는 항목중 가장 인덱스가 큰 것을 반환

# words의 길이는 최소 1 이상 100,000 이하
# words의 요소의 길이는 1 이상 7 이하

from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_map = defaultdict(list)
        self.suffix_map = defaultdict(list)
        self.cache = {}  # 캐시를 위한 딕셔너리 추가
        
        # 각 단어의 인덱스를 접두사와 접미사 해시맵에 저장
        for index, word in enumerate(words):
            prefix = ''
            for char in word:
                prefix += char
                self.prefix_map[prefix].append(index)
                
            suffix = ''
            for char in reversed(word):
                suffix = char + suffix
                self.suffix_map[suffix].append(index)

    def f(self, pref: str, suff: str) -> int:
        # 캐시에 저장된 결과가 있는지 확인
        if (pref, suff) in self.cache:
            return self.cache[(pref, suff)]
        
        if pref not in self.prefix_map or suff not in self.suffix_map:
            self.cache[(pref, suff)] = -1
            return -1
        
        prefix_indices = self.prefix_map[pref]
        suffix_indices = self.suffix_map[suff]
        
        # 두 리스트의 공통된 최대 인덱스 찾기
        prefix_set = set(prefix_indices)
        max_index = -1
        
        for index in suffix_indices:
            if index in prefix_set and index > max_index:
                max_index = index
        
        # 결과를 캐시에 저장
        self.cache[(pref, suff)] = max_index
        
        return max_index

# 사용 예시
# words = ["apple", "banana", "app"]
# obj = WordFilter(words)
# print(obj.f("a", "e"))  # 예시 결과: 0
# print(obj.f("b", "a"))  # 예시 결과: 1
