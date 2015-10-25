from Bio.PDB import PDBParser

parser = PDBParser()

structure = parser.get_structure('S0', '../PDBFiles/1G8W.pdb')

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom)