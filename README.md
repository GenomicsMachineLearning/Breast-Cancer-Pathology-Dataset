# Breast-Cancer-Pathology-Dataset
Summary of pathology public dataset for Breast Cancer

# Breast Cancer Pathology Datasets

This repository collects breast cancer histopathology datasets used in my PhD work
(e.g. CHIEF, BEPH, THREAD, Prov-GigaPath, etc.). It is meant as a **catalog**:
where the data come from, what tasks they are used for, and where they live on
my HPC storage.

The main catalog is in [`data/datasets.csv`](data/datasets.csv).

> ⚠️ **Note:** Local storage paths (e.g. `/QRISdata/...`, `/scratch/...`) are
> specific to my HPC environment (Bunya / QRISdata) and will not exist elsewhere.

---

## File structure

- `data/datasets.csv` — one row per dataset, with metadata (organ, slides,
  usage, access link, local storage dir, task, etc.).

### Columns in `datasets.csv`

- `No` – internal ID.
- `DatasetName` – short dataset name.
- `Model` – foundation model / project that mainly uses it (e.g. CHIEF, BEPH, THREAD).
- `Organ` – here always `Breast`.
- `SourceType` – `Public` or `Institutional data` / `Control`.
- `UsageInStudy` – how I use it (pretrain, validation, survival, etc.).
- `Slides` – number of slides / images (approx if not exact).
- `Description` – short description of the dataset.
- `HowToAccess` – URL or contact info.
- `DOI` – DOI if available.
- `StorageDir` – local path on my HPC (if applicable).
- `Task` – high-level task (Subtype / Cancer / Biomarker, etc.).
- `TrainValidate` – role in experiments (Train / Validate / Test).

---

## Quick usage

### Python

```python
import pandas as pd

df = pd.read_csv("data/datasets.csv")
print(df.head())
