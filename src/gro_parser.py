def read_gro_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def split_into_molecules(gro_content):
    molecules = {}
    current_molecule = None
    for line in gro_content:
        if line.startswith('Mol'):
            current_molecule = line.split()[0]
            molecules[current_molecule] = []
        elif current_molecule:
            molecules[current_molecule].append(line)
    return molecules

def split_into_atoms(molecule_content):
    atoms = []
    for line in molecule_content:
        if not line.startswith('Mol'):
            atoms.append(line)
    return atoms

