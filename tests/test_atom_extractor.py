import unittest
from src.atom_extractor import extract_xyz_coordinates

class TestAtomExtractor(unittest.TestCase):
    def test_extract_xyz_coordinates(self):
        atom_lines = [
            '1MET      N    1   1.212   2.331   3.141',
            '1MET      CA   2   1.222   2.322   3.111'
        ]
        coordinates = extract_xyz_coordinates(atom_lines)
        self.assertEqual(coordinates, [(1.212, 2.331, 3.141), (1.222, 2.322, 3.111)])

if __name__ == '__main__':
    unittest.main()

