from Bio.PDB import PDBParser

parser = PDBParser()

initial = parser.get_structure('initial', '../PDBFiles/1N3W_ALIGNED_1PEB.pdb')
final = parser.get_structure('final', '../PDBFiles/1PEB_ALIGNED_1N3W.pdb')

for model in initial:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom)

for model in final:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom)