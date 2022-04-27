import requests
import yaml

if __name__ == "__main__":
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    key = config["key"]
    r = requests.post(f"https://maker.ifttt.com/trigger/Water_Bottle_Notification/with/key/{key}", json={"value1": "This is a manual test"})
    print(r.text)
