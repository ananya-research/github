class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
    # Get the original matrix dimensions\
        m = len(mat)          # Number of rows
        n = len(mat[0])       # Number of columns

        # Check if the reshape operation is possible
        if m * n != r * c:
            return mat

        # Flatten the original matrix into a 1D list
        flat_list = [element for row in mat for element in row]
        print(flat_list)

        # Generate the new reshaped matrix
        reshaped_matrix = []
        for i in range(r):
            flat_list[i * c : (i + 1) * c]
            reshaped_matrix.append(flat_list[i * c : (i + 1) * c])

        return reshaped_matrix


        