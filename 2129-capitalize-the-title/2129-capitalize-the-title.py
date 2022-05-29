class Solution:
    def capitalizeTitle(self, title: str) -> str:
        split_title=title.split()
        final=[]
        
        for i in range(len(split_title)):
            if len(split_title[i])<=2:
                final.append(split_title[i].lower())
            else:
                final.append(split_title[i].capitalize())
        return " ".join(final)
        
            
        