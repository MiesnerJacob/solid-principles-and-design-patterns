# Uses Observer Design Pattern

class Grid:
    def __init__(self, cells):
        self.cells = cells

    def update(self):
        next_states = []
        for row in range(len(self.cells)):
            next_row = []
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                live_neighbors = self.count_live_neighbors(row, col)
                next_state = cell.next_state(live_neighbors)
                next_row.append(next_state)
            next_states.append(next_row)
        
        # Update the actual cell states
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.cells[row][col] = next_states[row][col]

    def count_live_neighbors(self, row, col):
        neighbor_positions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        live_neighbors = 0
        for dr, dc in neighbor_positions:
            r, c = row + dr, col + dc
            if 0 <= r < len(self.cells) and 0 <= c < len(self.cells[0]):
                if self.cells[r][c].is_alive():
                    live_neighbors += 1
        
        return live_neighbors
