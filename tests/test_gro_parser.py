import unittest
from src.gro_parser import read_gro_file, split_into_molecules, split_into_atoms

class TestGroParser(unittest.TestCase):
    def test_read_gro_file(self):
        content = read_gro_file('sample.gro')
        self.assertIsInstance(content, list)

    def test_split_into_molecules(self):
        content = read_gro_file('sample.gro')
        molecules = split_into_molecules(content)
        self.assertIsInstance(molecules, dict)

    def test_split_into_atoms(self):
        content = read_gro_file('sample.gro')
        molecules = split_into_molecules(content)
        for molecule, lines in molecules.items():
            atoms = split_into_atoms(lines)
            self.assertIsInstance(atoms, list)

if __name__ == '__main__':
    unittest.main()

