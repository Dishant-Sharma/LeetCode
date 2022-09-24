class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		if len(set(s)) != len(set(t)):
			return False
		dict = {}
		for i in range(len(t)):
			if t[i] not in dict:
				dict[t[i]] = s[i]
			elif dict[t[i]] != s[i]:
				return False
		return True