class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} 
        for word in strs:
            sortedword = "".join(sorted(word))
                    
            if sortedword not in dict:
                dict[sortedword] = [word]
                    
            else:
                dict[sortedword].append(word)
                
        results = []
        for items in dict.values():
            results.append(items)
            
        return results

'''
 #1. Take empty dict
#2. loop through the given array
3.sort every word in array while looping adn check if sorted word is there in dict 
4.if not add to dict taking 
	sortedword as the key and
        word as the value 
5. if yes append the word to the values of sorted word 
6. loop through the dict

'''
