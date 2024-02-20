import json
import requests


with open('listfile.json', encoding="utf8") as filehandle:
    identifier_list = json.load(filehandle)

    # view list contents
    print(identifier_list)

    """enumerating and filtering for the first ten entries in the identifier_list"""
    for i, entry in enumerate(identifier_list[0:10]):
        # print(i)
        # print(entry)
        if entry['type'] == 'csmiles':
            csmiles = entry['value']

            """prints the URL to the pubchem rest API for the compound"""
            API_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/" + csmiles + "/"
            print(API_URL)

            """prints the URL to the pubchem rest API for the synonyms of that compound"""
            # API_URL_synonyms_json = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/synonyms/json"
            # print(API_URL_synonyms_json)

            """Use the request package to access the data at that URL as json"""
            # synonym_query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/synonyms/json").json()
            # print(synonym_query_json)
            #
            # synonyms = synonym_query_json["InformationList"]["Information"][0]["Synonym"]
            # print(synonyms)

            """Get the hydrogen bond donor count for that compound as text"""
            # HBD_query = requests.get(
            #     "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/" + csmiles + "/property/HBondDonorCount/txt")
            # print(HBD_query.text)