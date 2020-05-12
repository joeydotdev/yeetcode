"""
[
	[1,1,1],
	[1,1,0],
	[1,0,1]
]

1
1
2

"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]: 
    	def out_of_bounds(row, col):
    		print(len(image))
    		print(len(image[row]))
    		return row < 0 or len(image) <= row or col < 0 or len(image[row]) <= col

    	def dfs(row, col):
    		if out_of_bounds(row, col):
    			print("activated")
    			print("row {0}, col {0}".format(row, col))
    			return

    		old_color = image[row][col]
    		if old_color == newColor:
    			dfs(row+1, col)
    			dfs(row-1, col)
    			dfs(row, col+1)
    			dfs(row, col-1)
    		else:
    			image[row][col] = newColor
   
		image[sr][sc] = newColor
    	dfs(sr, sc)	
    	return image 
