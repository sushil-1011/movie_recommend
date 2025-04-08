import os
import gdown

def download_file(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(output):
        print(f"Downloading {output}...")
        gdown.download(url, output, quiet=False)
    else:
        print(f"{output} already exists. Skipping download.")

# Replace with actual file ID and file name
download_file("1aj-DdmlsKaNtnlivlKLao3lZmVFbUf_2", "movie_dict.pkl")
download_file("1ALMTziH1UNiAN5pjUEU3N4D1tayoYXVs", "similarity.pkl")
