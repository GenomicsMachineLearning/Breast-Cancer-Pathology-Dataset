# Breast Cancer Imaging Datasets 

This is the summary of breast cancer imaging datasets I use in my PhD  
(WSIs, patch–level datasets, segmentation / nuclei labels, clinical & drug–response data, etc.).


> ⚠️ This is **not** a redistributable dataset repo.  
> Links point to the original sources. Local paths are specific to my HPC (QRISdata / scratch).

---

## Table of Contents

- [Quick Overview Table](#quick-overview-table)
- [Dataset Notes](#dataset-notes)
  - [BreakHis](#breakhis)
  - [ACROBAT](#acrobat)
  - [REG2025](#reg2025)
  - [HISTAI-breast](#histai-breast)
  - [CAMELYON](#camelyon)
  - [HTAN-BRCA](#htan-brca)
  - [TCGA-BRCA](#tcga-brca)
  - [SPIDER-breast](#spider-breast)
  - [GTEx (Breast)](#gtex-breast)
  - [BRACS](#bracs)
  - [TUPAC16](#tupac16)
  - [BACH](#bach)
  - [DROID-Breast](#droid-breast)
  - [Drug Response dataset](#drug-response-dataset)
  - [Breast Histopathology Images (Kaggle)](#breast-histopathology-images-kaggle)
  - [BCSS](#bcss)
  - [CPTAC-BRCA](#cptac-brca)
  - [HEST subset](#hest-subset)
  - [NuCLS](#nucls)
  - [YH-BRCA](#yh-brca)
  - [MBC](#mbc)
  - [BNCB](#bncb)
  - [BWH-BRCA](#bwh-brca)
  - [PLCO-BRCA](#plco-brca)
  - [SMCH-BRCA](#smch-brca)
  - [DFCI-BRCA](#dfci-brca)
  - [CUCH-BRCA](#cuch-brca)
  - [Prov-Path 1](#prov-path-1)
  - [Prov-Path 2](#prov-path-2)

---

## Quick Overview Table

| Dataset | Model / Project | Source type | Usage in study | Slides / Images | Task (rough) | Access |
|--------|-----------------|-------------|----------------|-----------------|--------------|--------|
| BreakHis | BEPH | Public | – | 9,109 images | Cancer / patch classification | [Link](http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz) |
| ACROBAT | CHIEF | Public | Pretrain | 4,212 WSIs | Biomarker / ER, PR, HER2, Ki67 | [Portal](https://researchdata.se/sv/catalogue/dataset/2022-190-1/1) |
| REG2025 | – | Public | – | 2,143 | WSI + clinical | [GC challenge](https://reg2025.grand-challenge.org/reg2025-traindataset/) |
| HISTAI-breast | – | Public | – | 1,925 | Patch/WSI classification | [HF dataset](https://huggingface.co/datasets/histai/HISTAI-breast) |
| CAMELYON | BEPH | Public | – | 1,399 WSIs | Cancer / metastasis | [GigaDB](http://gigadb.org/dataset/100439) |
| HTAN-BRCA | – | Public | – | 982 H&E | Multi-omics atlas | [HTAN portal](https://humantumoratlas.org/explore) |
| TCGA-BRCA | CHIEF | Public | Held-out survival | 963 WSIs | Subtype / prognosis | [GDC](https://portal.gdc.cancer.gov/projects/TCGA-BRCA) |
| SPIDER-breast | – | Public | – | 912 | Patch + context | [HF dataset](https://huggingface.co/datasets/histai/SPIDER-breast) |
| GTEx (Breast) | THREAD | Public | Pretrain | 894 | Normal breast | [GTEx histology](https://www.gtexportal.org/home/histologyPage) |
| BRACS | UNI | Public | – | 547 WSIs | Subtype | [BRACS site](https://www.bracs.icar.cnr.it/download/) |
| TUPAC16 | – | Public | – | 500 | Proliferation / biomarker | [Challenge](https://tupac.grand-challenge.org/) |
| BACH | BEPH | Public | – | 400 | 4-class patch classification | [ICiar 2018](https://iciar2018-challenge.grand-challenge.org/Dataset/) |
| DROID-Breast | CHIEF | Public | Val (cell det.) | 361 WSIs | Cancer cell detection | Email: claes.lundstrom@liu.se |
| Drug Response | – | Public | Train & Val | 204 | Drug response | [Zenodo](https://zenodo.org/records/6337925#.Y30d1y-l1Ls) |
| Breast Histopathology Images | – | Public | – | 162 | Patch classification | [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images) |
| BCSS | – | Public | – | 151 | Tissue segmentation | [GitHub](https://github.com/PathologyDataScience/BCSS) |
| CPTAC-BRCA | CHIEF | Public | Origin ID | 134 cases | Subtype / origin | [TCIA collection](https://www.cancerimagingarchive.net/collection/cptac-brca/) |
| HEST subset | – | – | Val | 125 | Biomarker | – |
| NuCLS | – | Public | – | 124 WSIs | Nuclei labels | [NuCLS site](https://sites.google.com/view/nucls/multi-rater?authuser=0) |
| YH-BRCA | CHIEF | Institutional | Pretrain | 98 | Mixed | Email: Kun-Hsing_Yu@hms.harvard.edu |
| MBC | THREAD | Public | – | 99 WSIs (77 pts) | Metastatic BC | [Synapse](https://www.synapse.org/Synapse:syn59490671/wiki/628046) |
| BNCB | CHIEF | Public | Pretrain | 58 | Biopsy WSIs | [Drive folder](https://drive.google.com/drive/folders/1HcAgplKwbSZ7ZZl2m6PZdvVF70QJmVuR) |
| BWH-BRCA | CHIEF | Institutional | Cell det. | 104 WSIs | Cancer cell detection | Email: Kun-Hsing_Yu@hms.harvard.edu |
| PLCO-BRCA | CHIEF | Control | Cell det. | 647 WSIs | Control cohort | [CDAS](https://cdas.cancer.gov/datasets/plco/19/) |
| SMCH-BRCA | CHIEF | Institutional | Cell det. | 52 | Cancer cell detection | Email: Kun-Hsing_Yu@hms.harvard.edu |
| DFCI-BRCA | CHIEF | Institutional | Survival | 48 WSIs | Survival prediction | Email: Kun-Hsing_Yu@hms.harvard.edu |
| CUCH-BRCA | CHIEF | Institutional | Cell det. | 42 | Cancer cell detection | Email: Kun-Hsing_Yu@hms.harvard.edu |
| Prov-Path 1 | Prov-GigaPath | Public | – | 15 | GigaPath cohort | [Zenodo](https://zenodo.org/records/10909922) |
| Prov-Path 2 | Prov-GigaPath | Public | – | 15 | GigaPath cohort | [Zenodo](https://zenodo.org/records/10909616) |

> ✅ You can gradually refine “Task” and “Usage in study” as your experiments become fixed.

---

## Dataset Notes

*(This is the “note” part – feel free to add bullet points, TODOs, caveats, QC info, etc.)*

### BreakHis

- **Model / project:** BEPH  
- **Type:** Public, microscopic images (40X, 100X, 200X, 400X)  
- **Size:** 9,109 images from 82 patients  
- **Source / access:**  
  - Download: <http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz>  
  - Info page: <https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/>
- **Local path:** `/scratch/project_mnt/S0010/Hao/BreakHis`
- **Typical tasks:** Benign vs malignant, multi-class tumour subtype (patch-level)  
- **My notes:**  
  - TODO: write how I split magnifications / train-val-test.  
  - TODO: note any preprocessing steps (stain norm, patch filtering, etc.).

---

### ACROBAT

- **Model / project:** CHIEF  
- **Type:** Public WSIs (H&E + IHC ER/PR/HER2/Ki67)  
- **Size:** 4,212 WSIs from 1,153 primary BC patients  
- **Usage in my study:** Pretraining for biomarker / ER-PR-HER2 Ki67  
- **Access:** <https://researchdata.se/sv/catalogue/dataset/2022-190-1/1>  
- **Local path:** `/QRISdata/Q2051/Hao/ACROBAT`
- **Task:** Biomarker, stain-aware pretraining  
- **My notes:**  
  - TODO: record which stain subsets I actually downloaded.  
  - TODO: mapping from IHC labels to training targets (ER status, etc.).

---

### REG2025

- **Model / project:** –  
- **Type:** Public challenge dataset, WSI + clinical pairs  
- **Size:** ~2,143 slides  
- **Access:** <https://reg2025.grand-challenge.org/reg2025-traindataset/>  
- **Task:** Risk prediction / clinical outcome (depending on challenge track)  
- **My notes:**  
  - TODO: document which split / track I use.  
  - TODO: clinical variables I care about (e.g. survival, grade, receptor status).

---

### HISTAI-breast

- **Type:** Public  
- **Size:** 1,925 entries (HISTAI-breast dataset)  
- **Access:** <https://huggingface.co/datasets/histai/HISTAI-breast>  
- **My notes:**  
  - TODO: clarify if used for contrastive / self-supervision or supervised.  

---

### CAMELYON

- **Model / project:** BEPH  
- **Type:** Public, lymph node WSIs  
- **Size:** 1,399 WSIs of sentinel lymph nodes  
- **Access:**  
  - Download: <http://gigadb.org/dataset/100439>  
  - DOI: `10.5524/100439`
- **Task:** Metastasis detection (cancer vs normal)  
- **My notes:**  
  - TODO: whether I use pixel-level annotations or slide-level only.  

---

### HTAN-BRCA

- **Type:** Public, multi-omics tumor atlas  
- **Size:** 982 H&E slides (Breast + H&E filter)  
- **Access:**  
  - HTAN explorer (filtered breast + H&E):  
    <https://humantumoratlas.org/explore?...>  <!-- full URL in original table -->
- **Local path:** `/QRISdata/Q1851/Hao/htan`
- **My notes:**  
  - TODO: how I link H&E to spatial / single-cell data (if any).  

---

### TCGA-BRCA

- **Model / project:** CHIEF  
- **Type:** Public, TCGA breast  
- **Size:** 963 WSIs (IDC ≈ 767, ILC ≈ 196)  
- **Usage in my study:** Held-out validation for survival prediction, subtype tasks  
- **Access:** <https://portal.gdc.cancer.gov/projects/TCGA-BRCA>  
- **Task:** Subtype, survival  
- **My notes:**  
  - TODO: list exact TCGA barcodes used.  
  - TODO: mapping between slide IDs and clinical table.

---

### SPIDER-breast

- **Type:** Public, supervised patch + context dataset  
- **Size:** 912 composite samples  
- **Description:**  
  - Central 224×224 patch with class label  
  - 24 surrounding context patches (total region 1120×1120 at 20X)  
- **Access:** <https://huggingface.co/datasets/histai/SPIDER-breast>  
- **Local path:** `/QRISdata/Q1851/val_data`
- **My notes:**  
  - TODO: how I use this to probe context modeling or attention.

---

### GTEx (Breast)

- **Model / project:** THREAD  
- **Type:** Public normal breast histology  
- **Size:** 894 images  
- **Access:** <https://www.gtexportal.org/home/histologyPage>  
- **Task:** Normal-tissue pretraining / domain adaptation  
- **My notes:**  
  - TODO: note which slides used as “normal controls”.

---

### BRACS

- **Model / project:** UNI  
- **Type:** Public WSIs  
- **Size:** 547 labeled WSIs  
- **Access:** <https://www.bracs.icar.cnr.it/download/>  
- **Extra:** `wget –no-parent -r ftp://histoimage.na.icar.cnr.it/`  
- **Task:** Subtype classification  
- **My notes:**  
  - TODO: internal split vs official split.

---

### TUPAC16

- **Type:** Public challenge dataset  
- **Size:** 500 slides  
- **Access:** <https://tupac.grand-challenge.org/>  
- **Task:** Proliferation / biomarker-related tasks  
- **My notes:**  
  - TODO: whether I use mitosis labels or only slide-level scores.

---

### BACH

- **Model / project:** BEPH  
- **Type:** Public patch dataset  
- **Size:** 400 images  
- **Classes:** normal, benign, in situ, invasive carcinoma  
- **Access:** <https://iciar2018-challenge.grand-challenge.org/Dataset/>  
- **My notes:**  
  - TODO: mapping BACH labels to BEPH labels (if any).

---

### DROID-Breast

- **Model / project:** CHIEF  
- **Type:** Public WSIs  
- **Size:** 361 H&E slides  
- **Usage in my study:** Cancer cell detection validation  
- **Access:** Email `claes.lundstrom@liu.se`  
- **My notes:**  
  - TODO: how to get annotations & license details.

---

### Drug Response dataset

- **Type:** Public  
- **Size:** 204 samples  
- **Usage:** Train & validate for drug-response modeling  
- **Access:**  
  - Zenodo: <https://zenodo.org/records/6337925#.Y30d1y-l1Ls>  
  - Paper: <https://www.nature.com/articles/s41586-021-04278-5>  
- **Local path:** `/QRISdata/Q1851/val_data`
- **My notes:**  
  - TODO: which cell lines or patient-derived samples I actually use.

---

### Breast Histopathology Images (Kaggle)

- **Type:** Public patch dataset  
- **Size:** 162 images (plus patch structure in Kaggle description)  
- **Access:** <https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images>  
- **My notes:**  
  - TODO: whether I use full dataset or subset.

---

### BCSS

- **Type:** Public segmentation dataset  
- **Size:** 151 slides, >20k tissue-region segmentations  
- **Access:** <https://github.com/PathologyDataScience/BCSS>  
- **Task:** Tissue-region segmentation (stroma, tumour, etc.)  
- **My notes:**  
  - TODO: which classes are relevant for my TME analysis.

---

### CPTAC-BRCA

- **Model / project:** CHIEF  
- **Type:** Public WSIs with multi-omics (proteomics etc.)  
- **Size:** 134 primary tumor slides (~328 BRCA cases)  
- **Access:** <https://www.cancerimagingarchive.net/collection/cptac-brca/>  
- **Task:** Subtype, tumour-origin identification  
- **My notes:**  
  - TODO: link to proteomics table, if needed for multimodal aim.

---

### HEST subset

- **Model / project:** HEST  
- **Type:** Internal subset (details TBD)  
- **Size:** 125 slides  
- **Usage in my study:** Biomarker validation  
- **My notes:**  
  - TODO: specify which collection this subset came from.

---

### NuCLS

- **Type:** Public, nuclei-level annotations  
- **Size:** >220k labeled nuclei from TCGA breast images  
- **Access:** <https://sites.google.com/view/nucls/multi-rater?authuser=0>  
- **Task:** Nuclei detection / classification  
- **My notes:**  
  - TODO: whether I use this for training cell detectors (CellViT / CellPose-SAM etc.).

---

### YH-BRCA

- **Model / project:** CHIEF  
- **Type:** Institutional  
- **Size:** 98 cases (details not clearly stated)  
- **Access:** Email `Kun-Hsing_Yu@hms.harvard.edu`  
- **Usage in my study:** Pretraining / internal validation  
- **My notes:**  
  - TODO: summary once I get the data.

---

### MBC

- **Model / project:** THREAD  
- **Type:** Public, metastatic breast cancer  
- **Size:** 77 patients, 99 WSIs  
- **Access:** <https://www.synapse.org/Synapse:syn59490671/wiki/628046>  
- **My notes:**  
  - TODO: endpoints I care about (site of metastasis, survival, etc.).

---

### BNCB

- **Model / project:** CHIEF  
- **Type:** Public, biopsy WSIs (core needle)  
- **Size:** 58 patients  
- **Description:** Tumour annotations partially provided; clinical metadata included  
- **Access:** <https://drive.google.com/drive/folders/1HcAgplKwbSZ7ZZl2m6PZdvVF70QJmVuR>  
- **Task:** Cancer detection / core biopsy analysis  
- **My notes:**  
  - TODO: note annotation format (XML / JSON / etc.).

---

### BWH-BRCA

- **Model / project:** CHIEF  
- **Type:** Institutional  
- **Size:** 104 WSIs  
- **Usage:** Cancer cell detection  
- **Access:** Email `Kun-Hsing_Yu@hms.harvard.edu`  
- **My notes:**  
  - TODO: if/when I manage to get access.

---

### PLCO-BRCA

- **Model / project:** CHIEF  
- **Type:** Control cohort  
- **Size:** 52 patients, 647 WSIs  
- **Usage:** Cancer cell detection controls  
- **Access:** <https://cdas.cancer.gov/datasets/plco/19/> (via CDAS)  
- **My notes:**  
  - TODO: exactly how controls are used in CHIEF-style training.

---

### SMCH-BRCA

- **Model / project:** CHIEF  
- **Type:** Institutional  
- **Size:** 52 cases (details not stated)  
- **Usage:** Cancer cell detection  
- **Access:** Email `Kun-Hsing_Yu@hms.harvard.edu`  
- **My notes:**  
  - TODO: fill in details once available.

---

### DFCI-BRCA

- **Model / project:** CHIEF  
- **Type:** Institutional  
- **Size:** 48 WSIs  
- **Usage:** Survival prediction  
- **Access:** Email `Kun-Hsing_Yu@hms.harvard.edu`  
- **My notes:**  
  - TODO: confirm clinical endpoints (OS/DFS etc.).

---

### CUCH-BRCA

- **Model / project:** CHIEF  
- **Type:** Institutional  
- **Size:** 42 cases  
- **Usage:** Cancer cell detection  
- **Access:** Email `Kun-Hsing_Yu@hms.harvard.edu`  
- **My notes:**  
  - TODO: dataset details.

---

### Prov-Path 1

- **Model / project:** Prov-GigaPath  
- **Type:** Public  
- **Size:** 15 slides  
- **Access:** <https://zenodo.org/records/10909922>  
- **Usage:** GigaPath pretraining / evaluation  
- **My notes:**  
  - TODO: which splits / labels.

---

### Prov-Path 2

- **Model / project:** Prov-GigaPath  
- **Type:** Public  
- **Size:** 15 slides  
- **Access:** <https://zenodo.org/records/10909616>  
- **Usage:** GigaPath pretraining / evaluation  
- **My notes:**  
  - TODO: link + compare with Prov-Path 1 (different cohort?).

---

## How I Use This Repo

- As a **memory** of where things live on HPC.
- To track which datasets I actually used in:
  - Aim 1 (spatial characterization),
  - Aim 2 (gene-expression prediction from H&E),
  - Aim 3 (multimodal integration).
 
--- 

## Contributing & Contact
- **Contributions:**  
  Suggestions for new datasets, updates, or corrections are welcome. Please open an issue or submit a pull request.

- **Contact:**  
  For specific dataset access, follow the provided links or contact dataset maintainers directly.  For repository-related questions or inquiries, feel free to email me at [hao.nguyen@uq.edu.au](mailto:hao.nguyen@uq.edu.au).
