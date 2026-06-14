import os
from huggingface_hub import HfApi

def main():
    repo_id = "ByteDance/Bernini-Diffusers"
    api = HfApi(endpoint="https://hf-mirror.com")
    
    print("Fetching file list from HF mirror...")
    files = api.model_info(repo_id).siblings
    
    local_dir_base = os.path.abspath("models/Bernini_glut")
    
    input_file_path = "aria2_inputs.txt"
    with open(input_file_path, "w", encoding="utf-8") as f:
        for file_info in files:
            rpath = file_info.rfilename
            # Ignore git files
            if rpath.startswith(".git") or ".gitattributes" in rpath:
                continue
                
            url = f"https://hf-mirror.com/{repo_id}/resolve/main/{rpath}"
            
            # Target dir and out filename
            target_dir = os.path.join(local_dir_base, os.path.dirname(rpath))
            out_filename = os.path.basename(rpath)
            
            f.write(f"{url}\n")
            f.write(f"  dir={target_dir}\n")
            f.write(f"  out={out_filename}\n\n")
            
    print(f"Generated {input_file_path} successfully!")

if __name__ == "__main__":
    main()
