class Solution:
    def interpret(self, command: str) -> str:
        newString = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                newString += "G"
                i += 1
            elif command[i] == "(" and command[i + 1] == "a":
                newString += "al"
                i += 4
            else:
                newString += "o"
                i += 2
        return newString

        