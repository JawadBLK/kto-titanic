import unittest

"""
Count names with more than seven letters
"""
def count_long_names(prenoms: list[str], threshold: int = 7) -> int:
    long_names_count: int = 0
    
    for prenom in prenoms:
        # Pas de duplication (un seul print) & pas d'imbrication profonde
        comparison: str = "supérieur à" if len(prenom) > threshold else "inférieur ou égal à"
        print(f"{prenom} est un prénom avec un nombre de lettres {comparison} {threshold}")
        
        if len(prenom) > threshold:
            long_names_count += 1
            
    return long_names_count

class TestNamesMethod(unittest.TestCase):
    def test_count_long_names(self) -> None:
        prenoms: list[str] = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(count_long_names(prenoms, threshold=7), 4)

if __name__ == '__main__':
    unittest.main()