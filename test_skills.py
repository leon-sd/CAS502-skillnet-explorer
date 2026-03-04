import unittest
import networkx as nx
import skills


class TestAddOccupation(unittest.TestCase):

    def setUp(self):
        self.skills_graph = nx.Graph()
        self.skills_graph.add_node("2.A.1.a", occupations=[])

    def test_adds_new_occupation(self):
        row = {"Title": "Mathematician", "Data Value": 4.5}

        skills.add_occupation(self.skills_graph, "2.A.1.a", row)

        self.assertEqual(
            self.skills_graph.nodes["2.A.1.a"]["occupations"],
            [("Mathematician", 4.5)]
        )

    def test_does_not_add_duplicate_occupation(self):
        row = {"Title": "Mathematician", "Data Value": 4.5}

        skills.add_occupation(self.skills_graph, "2.A.1.a", row)
        skills.add_occupation(self.skills_graph, "2.A.1.a", row)

        self.assertEqual(
            self.skills_graph.nodes["2.A.1.a"]["occupations"],
            [("Mathematician", 4.5)]
        )

    def test_adds_different_occupations(self):
        row1 = {"Title": "Mathematician", "Data Value": 4.5}
        row2 = {"Title": "Statistician", "Data Value": 4.8}

        skills.add_occupation(self.skills_graph, "2.A.1.a", row1)
        skills.add_occupation(self.skills_graph, "2.A.1.a", row2)

        self.assertEqual(
            self.skills_graph.nodes["2.A.1.a"]["occupations"],
            [("Mathematician", 4.5), ("Statistician", 4.8)]
        )


if __name__ == "__main__":
    unittest.main()