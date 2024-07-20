import unittest
import os
from cp30 import C3PO

class C3POTests(unittest.TestCase):
    def setUp(self):
        """Set up a C3PO instance for testing"""
        self.c3po = C3PO('test_examples/millennium-falcon.json')

    def test_1_load_json_invalid_file(self):
        """Test loading an invalid JSON file"""
        with self.assertRaises(ValueError):
            self.c3po._load_json('test_examples/invalid_mlf.json')

    def test_2_load_json_valid_file(self):
        """Test loading a valid JSON file"""
        data = self.c3po._load_json('test_examples/millennium-falcon.json')
        self.assertIsInstance(data, dict)
        self.assertIn('autonomy', data)
        self.assertIn('routes', data)

    def test_3_build_graph(self):
        """Test building the graph from routes data"""
        graph = self.c3po._build_graph()
        self.assertIsInstance(graph, dict)
        
        # Validate graph nodes
        self.assertIn('Tatooine', graph)
        self.assertIn('Endor', graph)
        self.assertIn('Dagobah', graph)
        self.assertIn('Hoth', graph)

        # Validate edges
        self.assertIn(('Dagobah', 4), graph['Endor'])
        self.assertIn(('Dagobah', 1), graph['Hoth'])
        self.assertIn(('Dagobah', 6), graph['Tatooine'])

        self.assertIn(('Tatooine', 6), graph['Dagobah'])
        self.assertIn(('Hoth', 6), graph['Tatooine'])

        self.assertIn(('Endor', 4), graph['Dagobah'])
        self.assertIn(('Hoth', 1), graph['Dagobah'])
        self.assertIn(('Tatooine', 6), graph['Hoth'])

class TestC3POExamples(unittest.TestCase):
    def test_example_1(self):
        """Testing Example 1 Data"""
        c3po = C3PO('examples/example1/millennium-falcon.json')
        odds = c3po.giveMeTheOdds('examples/example1/empire.json')
        expected_odds = 0.0
        self.assertEqual(odds, expected_odds)

    def test_example_2(self):
        """Testing Example 2 Data"""
        c3po = C3PO('examples/example2/millennium-falcon.json')
        odds = c3po.giveMeTheOdds('examples/example2/empire.json')
        expected_odds = 0.81
        self.assertEqual(odds, expected_odds)

    def test_example_3(self):
        """Testing Example 3 Data"""
        c3po = C3PO('examples/example3/millennium-falcon.json')
        odds = c3po.giveMeTheOdds('examples/example3/empire.json')
        expected_odds = 0.9
        self.assertEqual(odds, expected_odds)

    def test_example_4(self):
        """Testing Example 4 Data"""
        c3po = C3PO('examples/example4/millennium-falcon.json')
        odds = c3po.giveMeTheOdds('examples/example4/empire.json')
        expected_odds = 1.00
        self.assertEqual(odds, expected_odds)

if __name__ == '__main__':
    unittest.main(verbosity=2)
