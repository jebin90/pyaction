import unittest
import main

class TestBeamAnalysis(unittest.TestCase):
    def test_calculate_forces(self):
        result = main.calculate_forces(2, 10, 5)
        self.assertEqual(result, (20, -50, 30))
    
    def test_calculate_displacements(self):
        result = main.calculate_displacements(2, 10, 5, 20, -50)
        self.assertAlmostEqual(result, (0.4, -2.0), places=1)

if __name__ == '__main__':
    unittest.main()
