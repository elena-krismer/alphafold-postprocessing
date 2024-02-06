import os
from pathlib import Path
from alphafold_postprocessing.utils import load_optional_pkl
from alphafold_postprocessing.postprocessing import main

def cli_main():
    import argparse

    _parser = argparse.ArgumentParser(description=os.path.basename(__file__))
    _parser.add_argument(
        "-o",
        dest="out_dir",
        default=None,
        type=Path,
        help="Output folder (none - plot directly to the screen)",
    )
    _parser.add_argument(
        "data",
        type=Path,
        help="Input folder containing alphafold2 output",
    )
    _cmd_args = _parser.parse_args()

    main(
        data_dir=_cmd_args.data,
        features=load_optional_pkl(_cmd_args.data / "features.pkl"),
        out_dir=_cmd_args.out_dir,
    )
