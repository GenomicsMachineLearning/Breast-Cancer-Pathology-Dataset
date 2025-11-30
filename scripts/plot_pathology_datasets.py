#!/usr/bin/env python
"""
Plot summary figures for breast-cancer pathology datasets.

Input CSV (example path):
    data/pathology_datasets.csv

Expected columns (case sensitive):
    - "Dataset Name"  : dataset identifier
    - "Slides"        : number of slides / images (proxy for patients)
    - "Source type"   : e.g. Public / Institutional / Control / Internal

Outputs:
    images/pathology_slides_per_dataset.png
    images/pathology_slides_by_source.png
    images/pathology_datasets_by_source.png
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    # -------- paths --------
    data_path = Path("data/pathology_datasets.csv")
    out_dir = Path("images")
    out_dir.mkdir(parents=True, exist_ok=True)

    # -------- load data --------
    df = pd.read_csv(data_path)

    # Rename columns to simpler names (if needed)
    df = df.rename(
        columns={
            "Dataset Name": "Dataset",
            "Source type": "SourceType",
        }
    )

    # Keep only columns we need
    df = df[["Dataset", "Slides", "SourceType"]]

    # Drop rows without slide info
    df = df.dropna(subset=["Slides"])

    # Convert Slides to numeric (in case it's read as string)
    df["Slides"] = pd.to_numeric(df["Slides"], errors="coerce")
    df = df.dropna(subset=["Slides"])

    # -------- 1) Slides per dataset --------
    df_sorted = df.sort_values("Slides", ascending=False)

    plt.figure(figsize=(12, 6))
    plt.bar(df_sorted["Dataset"], df_sorted["Slides"])
    plt.xticks(rotation=75, ha="right")
    plt.ylabel("Number of slides / images")
    plt.title("Slides per histopathology dataset")
    plt.tight_layout()
    plt.savefig(out_dir / "pathology_slides_per_dataset.png", dpi=300)
    plt.close()

    # (Optional) log-scale version if chênh lệch rất lớn
    plt.figure(figsize=(12, 6))
    plt.bar(df_sorted["Dataset"], df_sorted["Slides"])
    plt.yscale("log")
    plt.xticks(rotation=75, ha="right")
    plt.ylabel("Number of slides / images (log scale)")
    plt.title("Slides per histopathology dataset (log scale)")
    plt.tight_layout()
    plt.savefig(out_dir / "pathology_slides_per_dataset_log.png", dpi=300)
    plt.close()

    # -------- 2) Pie: total slides by source type --------
    src_agg = df.groupby("SourceType")["Slides"].sum().sort_values(ascending=False)

    plt.figure(figsize=(6, 6))
    plt.pie(
        src_agg.values,
        labels=src_agg.index,
        autopct="%.1f%%",
        startangle=90,
    )
    plt.title("Distribution of slides by source type")
    plt.tight_layout()
    plt.savefig(out_dir / "pathology_slides_by_source.png", dpi=300)
    plt.close()

    # -------- 3) Bar: number of datasets by source type --------
    count_agg = df.groupby("SourceType")["Dataset"].count().sort_values(ascending=False)

    plt.figure(figsize=(6, 4))
    plt.bar(count_agg.index, count_agg.values)
    for i, v in enumerate(count_agg.values):
        plt.text(i, v + 0.3, str(v), ha="center", va="bottom")
    plt.ylabel("Number of datasets")
    plt.title("Number of histopathology datasets by source type")
    plt.tight_layout()
    plt.savefig(out_dir / "pathology_datasets_by_source.png", dpi=300)
    plt.close()

    print("Saved figures to:", out_dir.resolve())


if __name__ == "__main__":
    main()
