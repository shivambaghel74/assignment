import yaml

from app.config import PROFILE
from app.config import MANIFEST_PATH

with open(MANIFEST_PATH) as f:
    manifest = yaml.safe_load(f)

profiles = manifest["profiles"]

if PROFILE not in profiles:
    raise Exception(
        f"Invalid PROFILE={PROFILE}. "
        f"Valid profiles={list(profiles.keys())}"
    )

ACTIVE_PROFILE = profiles[PROFILE]

MODEL_ID = manifest["model"]["id"]
