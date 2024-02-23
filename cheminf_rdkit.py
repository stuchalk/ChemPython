from rdkit import Chem, DataStructs
from rdkit.Chem import Descriptors
import requests
import json

"""
Section 1
"""

"""Create a carbon dioxide molecule"""
rdkit_molecule_carbondioxide = Chem.MolFromSmiles('O=C=O')

"""Populate a dictionary with carbon dioxide data using cheminformatics toolkits"""
carbondioxide_data = {}

print(rdkit_molecule_carbondioxide)
molecule_inchi = Chem.MolToInchi(rdkit_molecule_carbondioxide)
print(molecule_inchi)
carbondioxide_data.update({"InChi": molecule_inchi})
print(carbondioxide_data)

molecule_InChiKey = Chem.MolToInchiKey(rdkit_molecule_carbondioxide)
carbondioxide_data.update({"InChiKey": molecule_InChiKey})
print(carbondioxide_data)

SMARTS_heavy_atom = Chem.MolFromSmarts("[!#1]")  # not equal to hydrogen
heavy_atom_count = rdkit_molecule_carbondioxide.GetSubstructMatches(SMARTS_heavy_atom)
print(heavy_atom_count)
print(len(heavy_atom_count))

carbondioxide_data.update({"heavy_atoms": len(heavy_atom_count)})
print(carbondioxide_data)


SMARTS_carbon_atom = Chem.MolFromSmarts("[#6]")  # not equal to hydrogen
carbon_atom_count = rdkit_molecule_carbondioxide.GetSubstructMatches(SMARTS_carbon_atom)
print(carbon_atom_count)
print(len(carbon_atom_count))

carbondioxide_data.update({"carbon_atoms": len(carbon_atom_count)})
print(carbondioxide_data)

"""
Section 2
"""

with open('listfile.json', 'r') as filehandle:
    identifier_list = json.load(filehandle)

    for x in identifier_list[0:10]:
        print(x['value'])

    """Make a carbon dioxide molecule"""
    rdkit_molecule_carbondioxide = Chem.MolFromSmiles('O=C=O')

    """Populate a dictionary with carbon dioxide data using cheminformatics toolkits"""
    carbondioxide_data = {}

    print(rdkit_molecule_carbondioxide)
    molecule_inchi = Chem.MolToInchi(rdkit_molecule_carbondioxide)
    print(molecule_inchi)
    carbondioxide_data.update({"InChi": molecule_inchi})
    print(carbondioxide_data)

    molecule_InChiKey = Chem.MolToInchiKey(rdkit_molecule_carbondioxide)
    carbondioxide_data.update({"InChiKey": molecule_InChiKey})
    print(carbondioxide_data)

    SMARTS_heavy_atom = Chem.MolFromSmarts("[!#1]")  # not equal to hydrogen
    heavy_atom_count = rdkit_molecule_carbondioxide.GetSubstructMatches(SMARTS_heavy_atom)
    print(heavy_atom_count)
    print(len(heavy_atom_count))

    carbondioxide_data.update({"heavy_atoms": len(heavy_atom_count)})
    print(carbondioxide_data)

    SMARTS_carbon_atom = Chem.MolFromSmarts("[#6]")  # not equal to hydrogen
    carbon_atom_count = rdkit_molecule_carbondioxide.GetSubstructMatches(SMARTS_carbon_atom)
    print(carbon_atom_count)
    print(len(carbon_atom_count))

    carbondioxide_data.update({"carbon_atoms": len(carbon_atom_count)})
    print(carbondioxide_data)

    """
    Generate a list of dictionaries containing the InChiKey, heavy atom count, and 
    carbon atoms for all entries in the identifier_list of type csmiles
    """

    csmiles_all = []
    for x in identifier_list:
        if x['type'] == 'csmiles':
            csmiles_all.append(x)

    slist = []
    for entry in csmiles_all[0:10]:
        sdict = {}
        rdkit_molecule = Chem.MolFromSmiles(entry['value'])
        SMARTS_heavy_atom = Chem.MolFromSmarts("[!#1]")
        heavy_atom_count = rdkit_molecule.GetSubstructMatches(SMARTS_heavy_atom)
        dict.update({"heavy_atoms": len(heavy_atom_count)})
        slist.append(sdict)

    """
    Generate a list of dictionaries containing pairs of molecules and their similarity 
    score as calculated from their fingerprint
    """

    csmiles_fingerprint = []
    for x in csmiles_all:
        mol = Chem.MolFromSmiles(x['value'])
        fp = Chem.RDKFingerprint(mol)
        csmiles_fingerprint.append({"csmiles": x['value'], "fingerprint": fp})

    matches = []
    for x in csmiles_fingerprint[0:9]:
        for y in csmiles_fingerprint[0:9]:
            similarity = DataStructs.TanimotoSimilarity(x['fingerprint'], y['fingerprint'])
            if similarity >= 0.5:
                matches.append({"csmiles1": x['csmiles'], "csmiles2": y['csmiles'], "similarity": similarity})

    for x in matches:
        print(matches)

    filehandle.close()

"""
Section 3
"""

with open('listfile.json', 'r') as filehandle:
    identifier_list = json.load(filehandle)

    """
    Generate a list of dictionaries containing the InChiKey, heavy atom count,
    and carbon atoms for all entries in the identifier_list of type csmiles
    """

    clist = []
    for entry in identifier_list:
        if entry['type'] == 'csmiles':
            # print(entry['value'])
            rdkit_molecule = Chem.MolFromSmiles(entry['value'])
            InChiKey = Chem.MolToInchiKey(rdkit_molecule)
            SMARTS_heavy_atom = Chem.MolFromSmarts("[!#1]")
            SMARTS_carbon_atom = Chem.MolFromSmarts("[#6]")
            heavy_atoms = len(rdkit_molecule.GetSubstructMatches(SMARTS_heavy_atom))
            carbon_atoms = len(rdkit_molecule.GetSubstructMatches(SMARTS_carbon_atom))
            item = {"InChiKey": InChiKey, "heavy_atoms": heavy_atoms, "carbon_atoms": carbon_atoms}
            clist.append(item)
    for x in clist:
        print(x)

    """Calculate molecular fingerprint from each csmiles"""

    csmiles_fingerprint = []
    for entry in identifier_list:
        if entry['type'] == 'csmiles':
            mol = Chem.MolFromSmiles(entry['value'])
            fp = Chem.RDKFingerprint(mol)
            csmiles_fingerprint.append({"csmiles": entry['value'], "fingerprint": fp})

    """Calculate similarity between molecules using fingerprint"""

    matches = []
    for x in csmiles_fingerprint[0:49]:
        for y in csmiles_fingerprint:
            similarity = DataStructs.TanimotoSimilarity(x['fingerprint'], y['fingerprint'])
            if .85 <= similarity < 1:
                matches.append({"csmiles1": x['csmiles'], "csmiles2": y['csmiles'], "similarity": similarity})
    for x in matches:
        print(x)

    """Calculate fingerprint, molecular weight, and carbon atoms. Then output to file."""

    SMARTS_carbon_atom = Chem.MolFromSmarts("[#6]")
    csmiles_fingerprint = []
    for entry in identifier_list:
        if entry['type'] == 'csmiles':
            mol = Chem.MolFromSmiles(entry['value'])
            HBD_query = requests.get(
                "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/" + entry['value'] +
                "/property/HBondDonorCount/txt")
            HBDs = HBD_query.text
            carbon_atoms = len(mol.GetSubstructMatches(SMARTS_carbon_atom))
            molwt = Chem.Descriptors.MolWt(mol)
            fp = Chem.RDKFingerprint(mol)
            csmiles_fingerprint.append(
                {"csmiles": entry['value'], "fingerprint": fp, "mol2_molweight": molwt,
                 "mol2_carbon_atoms": carbon_atoms})

    matches = []
    for x in csmiles_fingerprint[0:1]:
        for y in csmiles_fingerprint:
            similarity = DataStructs.TanimotoSimilarity(x['fingerprint'], y['fingerprint'])
            if similarity < 1:
                matches.append({"csmiles1": x['csmiles'], "csmiles2": y['csmiles'], "similarity": similarity,
                                "mol2_molweight": y["mol2_molweight"], "mol2_carbon_atoms": y['mol2_carbon_atoms']})

    with open('fingerprintfile.json', 'w') as filehandle2:
        json.dump(matches, filehandle2, default=str)

    filehandle.close()
