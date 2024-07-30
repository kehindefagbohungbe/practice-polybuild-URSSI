def extract_xyz_coordinates(atom_lines):
    coordinates = []
    for line in atom_lines:
        parts = line.split()
        x, y, z = float(parts[3]), float(parts[4]), float(parts[5])
        coordinates.append((x, y, z))
    return coordinates

