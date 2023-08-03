import os
import requests
import json
from pathlib import Path
from .config import kg_endpoint, auth_token, stage

query_id = "c5db2cea-6b47-47fd-8264-5c1fde0d84af"

url = f"{kg_endpoint}/v3/queries/{query_id}/instances?stage={stage}&vocab=https://schema.hbp.eu/myQuery/"

def snap(path_to_snapshot: Path):
    path_to_snapshot.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, headers={
        "Authorization": f"bearer {auth_token}"
    })
    resp.raise_for_status()
    resp_json = resp.json()
    for item in resp_json.get("data"):
        _id: str = item.get("id")
        trimmed_id = _id.replace("https://kg.ebrains.eu/api/instances/", "")
        with open(path_to_snapshot / f"{trimmed_id}.json", "w") as fp:
            json.dump(item, fp=fp, indent="\t")
            fp.write("\n")

def main():
    path_to_snapshot=Path("ebrainsquery/v3/DatasetVersion")
    snap(path_to_snapshot)

if __name__ == "__main__":
    main()
