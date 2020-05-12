class Solution:
    def get_coord(self, coord):
    	return coord[0]

    def calc_scope(self, first_coord, second_coord):
    	return (second_coord[1] - first_coord[1]) // (second_coord[0] - first_coord[0])	

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key=self.get_coord)
        first_coord, second_coord = coordinates[0], coordinates[1]

        slope = self.calc_scope(first_coord, second_coord)

        for i in range(2, len(coordinates) - 1):
	        first_coord, second_coord = coordinates[i], coordinates[i+1]
	        cur_slope = self.calc_scope(first_coord, second_coord)
	        if cur_slope != slope:
	        	return False

	    return True