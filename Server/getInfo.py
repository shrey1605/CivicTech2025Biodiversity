from collections import defaultdict
import json
import requests
import random
from collections import defaultdict

GBIF_API_URL = "https://api.gbif.org/v1/occurrence/search"

# Parameters for the API request
params = {
    "limit": 100000,  # Fetch a large number of records to filter from
    "offset": 0,     # Start from the first record
}

def func1():

    genus_subgenus_dict = defaultdict(lambda: defaultdict(set))

    response = requests.get(GBIF_API_URL, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
    
    data = response.json()
    results = data.get("results", [])
    
    for record in results:
        genus = record.get("genus")
        species = record.get("species")  # Treat species as subgenus
        country = record.get("country", "Unknown")  # Use country as distribution

        if genus and species:
            genus_subgenus_dict[genus][species].add(country)
    
    # Construct final JSON structure
    output_json = {"genuses": []}

    for genus, subgenus_data in list(genus_subgenus_dict.items())[:5]:  
        subgenena_list = []
        total_genus_occurrences = 0

        for subgenus, countries in list(subgenus_data.items())[:5]:  # Ensure 5 subgenera per genus
            occurrences = random.randint(1, 100)  # Random occurrences
            total_genus_occurrences += occurrences

            subgenena_list.append({
                "name": subgenus,
                "occurrences": occurrences,
                "distribution": ", ".join(countries)  # Join multiple country names
            })

        output_json["genuses"].append({
            "name": genus,
            "occurenceTotalGenus": total_genus_occurrences,
            "subgenena": subgenena_list
        })

    filename = "gottendata.json"

    with open(filename, 'w') as file:
        json.dump(output_json, file, indent=4)
    # Print formatted JSON output
    print(json.dumps(output_json, indent=4))


if __name__ == "__main__":
    func1()