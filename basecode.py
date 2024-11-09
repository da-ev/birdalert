from datasets import load_dataset
import os

# Setting so dataset saves to harddrive folder instead of personal device
dataset = load_dataset("auniquesun/AirBirds", cache_dir="D:/airbirds_dataset")
