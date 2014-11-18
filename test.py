from nutritionix import Nutritionix

nix = Nutritionix(app_id="0acff812", api_key="fe3234b8d467860ae368067d62ae5600")

result =  nix.item(id="513fc9e73fe3ffd40300109f").json()

num = result['nf_protein']
den = result['nf_serving_weight_grams']

proRatio = float(num)/float(den)

print proRatio


### Iteration for 100 most protein filled
ff = nix.search().nxql(
    filters={
        "nf_protein": {
            "gte": 120
        }
    },
    fields=["item_name", "item_id"]
).json()

print ff