"""Print the IUPAC names of all compounds in a PubChem XML export."""
 
import sys 
from bs4 import BeautifulSoup
 
 
class PubChemParser:
    def __init__(self, filename):
        with open(filename, encoding="utf-8") as f:
            self.soup = BeautifulSoup(f, "xml")
 
    def get_iupac_names(self):
        """Returns a list of IUPAC names of all compounds in the XML file."""
        names = []
        for tag in self.soup.find_all("iupacname"):
            name = tag.get_text()
            names.append(name)
        return names
 
 
def main(argv):
    if len(sys.argv) < 2:
        print("Usage: python pubchem_parser.py pubchem_benzidine.xml")
        return
    parser = PubChemParser(argv[1])
    for name in parser.get_iupac_names():
        print(name)
 
 
if __name__ == "__main__":
    main(sys.argv)

