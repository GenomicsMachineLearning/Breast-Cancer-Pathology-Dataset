3 Dataset DescriptionThe HISTAI dataset is a comprehensive, open-source resource for computational pathology research, designed to
address the limitations identified in existing public datasets. The dataset provides extensive Whole Slide Images (WSIs)
accompanied by detailed clinical and pathological metadata, enabling diverse applications ranging from diagnostic
modeling to multimodal analyses.
The HISTAI dataset serves as a foundational resource within the broader research ecosystem. Notably, the SPIDER
dataset [8], a collection of patch-level annotated pathological datasets, utilizes slides from the HISTAI dataset. Additionally, the Hibou foundation models [9], have been trained on a larger, encompassing dataset, of which HISTAI forms
a subset.3.1 Structure and OrganizationThe dataset is organized into specialized subsets based on tissue types and pathology specializations. These subsets are
independently accessible on the Hugging Face platform, allowing researchers targeted access to relevant cases. The
general naming structure for slides within each case is as follows:
2HISTAI: AN OPEN-SOURCE, LARGE-SCALE WSI DATASET• <dataset_name>/case_<case_id>/slide_<stain>_<slide_number>.tiff• <dataset_name>/case_<case_id>/slide_<magnification>_<stain>_<slide_number>.tiffMost slides are digitized at a standard magnification of 20X using Hematoxylin and Eosin (H&E) staining. Slides
captured at alternative magnifications (primarily 40X) explicitly note the magnification in their filenames, ensuring
clarity for downstream tasks. The majority of the slides were digitized using Leica Aperio GT450 and AT2 scanners,
though some were scanned with Hamamatsu or 3DHISTECH systems. However we can’t determine the exact model of
the scanner for individual slides.3.2 MetadataA master metadata repository accompanies the image subsets, providing extensive clinical, pathological, and technical
annotations for each case. The metadata includes:
• Diagnosis: Clinical diagnostic information and notes.
• Conclusion: Detailed pathological conclusions.
• Differential Diagnosis: Alternative diagnostic considerations.
• Micro Protocol: Detailed microscopic examination descriptions.
• Additional Information: Supplementary clinical or pathological details.
• Patient Demographics: Age and gender of the patient.
• ICD-10 Codes: Standardized diagnostic codes.
• Gross Examination Details: Descriptions from macroscopic analysis.
Each metadata entry directly references the corresponding WSIs, ensuring seamless integration of clinical and imagebased data.3.3 Available Specialized DatasetsCurrently, HISTAI comprises the following specialized subsets:
• HISTAI-hematologic• HISTAI-gastrointestinal• HISTAI-breast• HISTAI-thorax• HISTAI-skin-b1• HISTAI-skin-b2• HISTAI-colorectal-b1• HISTAI-colorectal-b2
3.4 Dataset StatisticsThe HISTAI dataset currently contains a substantial number of WSIs and cases, summarized in Table 1.
Further breakdowns of the dataset include:
• Magnification:
– Slides at 20X magnification: 57,647– Slides at 40X magnification: 2,463
• Staining protocols:
– H&E slides: 58,282– Other staining protocols: 1,828
3HISTAI: AN OPEN-SOURCE, LARGE-SCALE WSI DATASETTable 1: HISTAI Dataset StatisticsDataset Total Slides Total CasesHISTAI-hematologic 214 214
HISTAI-gastrointestinal 202 120
HISTAI-breast 1,925 1,692
HISTAI-thorax 829 657
HISTAI-skin-b2 43,757 20,621
HISTAI-skin-b1 7,710 1,778
HISTAI-colorectal-b1 5,379 998
HISTAI-colorectal-b2 94 62Total 60,110 26,142
3.5 Intended Uses and Potential ApplicationsThe extensive variety and detailed annotation of the HISTAI dataset facilitate a wide range of potential research
applications, including but not limited to:
• Development and benchmarking of diagnostic models.
• Studies on generalization across tissue types and clinical contexts.
• Investigation into multimodal pathology models integrating clinical metadata.
• Exploration of domain adaptation and transfer learning in digital pathology.
By releasing the HISTAI dataset, we aim to significantly contribute to ongoing research, enhance reproducibility, and
encourage the development of robust, clinically applicable AI solutions in digital pathology.4 ConclusionThe HISTAI dataset represents a significant advancement in addressing the current limitations of publicly available WSI
datasets in digital pathology. By providing a comprehensive, multimodal, and richly annotated collection of over 60,000
slides across diverse tissue types, HISTAI facilitates a wide array of computational pathology research opportunities. Its
open accessibility and detailed metadata not only promote reproducibility but also support the development of more
robust, generalizable, and clinically relevant AI solutions, ultimately advancing the broader field of digital pathology
