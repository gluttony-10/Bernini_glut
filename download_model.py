import os
import sys
from huggingface_hub import snapshot_download

def main():
    repo_id = "ByteDance/Bernini-Diffusers"
    local_dir = os.path.abspath("models/Bernini-Diffusers")
    print(f"Starting download of {repo_id} to {local_dir}...")
    
    # Configure HuggingFace Mirror for fast download
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    
    try:
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            local_dir_use_symlinks=False,
            ignore_patterns=["*.git*", "*.gitattributes"],
        )
        print("Model downloaded successfully!")
    except Exception as e:
        print(f"Error downloading model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
