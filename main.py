import os

# Unreal asset prefixes
PREFIXES = {
    "staticmesh": "SM_",
    "texture": "T_",
    "material": "M_",
    "blueprint": "BP_",
    "animation": "AN_"
}

def rename_assets(folder_path, asset_type):
    if asset_type not in PREFIXES:
        print("Unknown asset type.")
        return

    prefix = PREFIXES[asset_type]

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        if os.path.isfile(old_path):
            new_name = prefix + filename
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    asset_type = input("Enter asset type (staticmesh, texture, material, blueprint, animation): ")
    rename_assets(folder, asset_type)
