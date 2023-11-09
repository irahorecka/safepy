import sys
from pathlib import Path

import yaml

PYTHON_PATH = Path(__file__).resolve().parent.parent.parent.parent / "s_cerevisiae" / "s_cerevisiae" / "python"
sys.path.append(str(PYTHON_PATH))

from library import utils
from pipeline.gi.dataproc import (
    load_gi_data,
)
from scripts.webapp.export_corr_tsv_for_webapp import (
    get_valid_genes_from_loci,
    filter_corr_for_webapp_export,
    get_fm_term_from_id,
    load_and_filter_corr_tsv,
    get_gene_gene_corr,
    get_gene_fm_corr,
    get_fm_fm_corr,
    get_corr_score,
    is_overlapping_genes,
)

ROOT_PATH = PYTHON_PATH.parent
with open(ROOT_PATH / "config.yaml", "r", encoding="utf-8") as config:
    PATHS = yaml.safe_load(config)["paths"]
