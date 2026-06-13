class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'emptylist'
        return '-x-'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'emptylist':
            return []
        return s.split('-x-')
