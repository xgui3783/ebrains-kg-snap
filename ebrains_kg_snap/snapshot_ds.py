import os, requests, json
from pathlib import Path

def snap(path_to_snapshot: Path):
    from .config import kg_endpoint, auth_token, stage
    url = f"{kg_endpoint}/v3/queries/bd7127eb-9559-44d3-a004-7db63b0f8495/instances?stage={stage}&vocab=https://schema.hbp.eu/myQuery/"
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
    path_to_snapshot=Path("ebrainsquery/v3/Dataset")
    snap(path_to_snapshot)

if __name__ == "__main__":
    main()
