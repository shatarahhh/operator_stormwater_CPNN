#!/usr/bin/env python3
"""
Download the full training / validation / test arrays (~6 GB) from Google Drive.

Usage
-----
python scripts/download_full_data.py         # downloads to data/
python scripts/download_full_data.py -d /tmp # custom folder

Requires:  pip install gdown tqdm
"""

import argparse, pathlib, subprocess, sys

FILES = {
    # Google‑Drive file‑ID : local filename
    "1z4d1BKm1VBcbiPyVdHyups8a1XSiwH-u": "branch_concentration_d2.npz",
    "1F6Pyw8WyZMqmIJ9lblP33na6cGs_jClz": "branch_loading_620_cases.npz",
    "14eoU4aetH7DwvXRxO6DEr_hxwh6P5TyJ": "sol_c_620_cases_8000_points_filtered_d2.npz",
    "1sBj758-8QU8eeSuimx-dHnWeZkjLUwO4": "trunk_coordinates_620_cases_8000_points.npz",
    "1AatP2FSEhyDVJrIlCfxR1feQGNFBLsLV": "trunk_time.npz",
}

def main(target_dir: pathlib.Path):
    target_dir.mkdir(parents=True, exist_ok=True)
    for fid, fname in FILES.items():
        dest = target_dir / fname
        if dest.exists():
            print(f"✓ {fname} already present")
            continue
        url = f"https://drive.google.com/uc?id={fid}"
        print(f"↓ {fname}  …")
        # gdown retries automatically on flaky Drive responses
        subprocess.check_call([sys.executable, "-m", "gdown",
                            "--no-cookies", "--id", fid, "-O", dest])    
        print("All files downloaded.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-d", "--dir", type=pathlib.Path,
                   default=pathlib.Path("data"),
                   help="target directory (default: data/)")
    main(p.parse_args().dir)
