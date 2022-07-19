from __future__ import annotations

from typing import TYPE_CHECKING, List


from openmapflow.config import PROJECT_ROOT
from openmapflow.config import DataPaths as dp

if TYPE_CHECKING:
    from openmapflow.labeled_dataset import LabeledDataset


def create_features(datasets: List[LabeledDataset]):
    report = "DATASET REPORT (autogenerated, do not edit directly)"
    for d in datasets:
        text = d.create_features(disable_gee_export=True)
        report += "\n\n" + text

    with (PROJECT_ROOT / dp.DATASETS).open("w") as f:
        f.write(report)
