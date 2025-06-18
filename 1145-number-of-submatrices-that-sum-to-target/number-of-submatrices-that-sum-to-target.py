

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Iterate over all pairs of rows
        for top in range(rows):
            # This array will accumulate column sums from row `top` to `bottom`
            col_sums = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                # Now, apply 1D subarray sum = target using prefix sum + hashmap
                prefix_sum = 0
                prefix_map = defaultdict(int)
                prefix_map[0] = 1

                for val in col_sums:
                    prefix_sum += val
                    count += prefix_map[prefix_sum - target]
                    prefix_map[prefix_sum] += 1

        return count


