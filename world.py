from voxel import Voxel


class World:
    def __init__(self, size):
        voxels = []
        for i in range(size):
            row = []
            for j in range(size):
                col = []
                for z in range(size):
                    col.append(Voxel(0))
                row.append(col)
            voxels.append(row)
        self.voxels = voxels
