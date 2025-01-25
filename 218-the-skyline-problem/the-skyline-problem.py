class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def merge(left_building, right_building):
            i = j = 0
            x = 0
            h1 = h2 = 0
            result = []

            # merge the skylines
            while i < len(left_building) and j < len(right_building):

                # add the skylines from the smallest
                if left_building[i][0] < right_building[j][0]:
                    x = left_building[i][0]
                    h1 = left_building[i][1]
                    i+=1
                elif left_building[i][0] > right_building[j][0]:
                    x = right_building[j][0]
                    h2 = right_building[j][1]
                    j+=1    
                else:
                    # if x coordinates are same 
                    x = left_building[i][0]
                    h1 = left_building[i][1]
                    h2 = right_building[j][1]
                    i+=1
                    j+=1
                
                # Pick the greatest of the heights
                max_height = max(h1, h2)

                # add to the result skyline only if height changes
                if not result or max_height != result[-1][1]:
                     result.append([x, max_height])
                
            # Append remaining elements of left_building to result
            while i < len(left_building):
                result.append(left_building[i])
                i+=1

            # Append remaining elements of right_building to result
            while j < len(right_building):   
                result.append(right_building[j])
                j+=1

            return result

        def divide_n_conquer(buildings):

            # Base Case
            # Create skylines
            if len(buildings) == 1:
                # input: [[start, end, height]]
                # output: [[start, height], [end, 0]]
                return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

            # Divide
            mid = len(buildings) // 2
            left_buildings = divide_n_conquer(buildings[:mid])
            right_buildings = divide_n_conquer(buildings[mid:])
    
            # Conquer
            return merge(left_buildings,right_buildings)

        return divide_n_conquer(buildings)