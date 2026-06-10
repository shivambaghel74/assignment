#!/usr/bin/env python3

import yaml
import os

manifest = "/opt/app/etc/default/model_manifest.yaml"

with open(manifest) as f:
    data = yaml.safe_load(f)

active = os.getenv("PROFILE", "balanced")

print()
print("Active Profile:", active)
print()

print("Available Profiles")
print("------------------")

for profile in data["profiles"]:
    print(profile)
