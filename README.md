<p align="center">
  <img src="https://github.com/esborisova/Taxonomy4CL/assets/77779090/01aed43a-8ecd-4644-b433-bd2e36cd6895" />
</p>

## Taxonomy4CL

This project introduces a fine-grained taxonomy of Computational Linguistics (CL) and Natural Language Processing (NLP) research topics and sub-topics. Our goal is to structure knowledge and research in CL/NLP to allow more efficient navigation of publications and assist developers working on scholarly information processing tools. 

Taxonomy4CL was used to annotate [the FoRC4CL corpus](https://zenodo.org/records/10777674), comprising 1500 publications from the ACL Anthology labelled according to their main contributions. The corpus was used in the Field of Research Classification (FoRC) shared task as part of the [Natural Scientific Language Processing (NSLP) 2024 Workshop](https://nfdi4ds.github.io/nslp2024/). 

## Versions and label definitions


We aim for Taxonomy4CL to be a growing resource based on community feedback. We will regularly check feedback on missing labels, hierarchy structures, and different phrasing of labels. 
You will find different versions of the taxonomy at:

```commandline
/data/Taxonomy4CL
```

The latest version of Taxonomy4CL can be viewed in a more intuitive way using an [interactive tree structure](https://huggingface.co/spaces/DFKI-SLT/Taxonomy4CL).


Certain labels in the taxonomy are not straightforward in terms of their definition and what type of contribution they describe. We provide definitions for such labels in [this document](https://docs.google.com/document/d/1kc19ecKBYxF9mtWTTeR8dHdkM12SI4REpfF4DlfBpoc/edit?usp=sharing). 

## Feedback

This resource grows based on your feedback! 

If you have any questions regarding labels or suggestions for new ones, please do not hesitate to open an issue in this repository. 

## Cite us

If you use our resources (Taxonomy4CL and FoRC4CL), please cite the following publication:

```commandline
@inproceedings{ahmad-etal-2024-forc4cl-fine,
    title = "{F}o{RC}4{CL}: A Fine-grained Field of Research Classification and Annotated Dataset of {NLP} Articles",
    author = "Ahmad, Raia Abu  and
      Borisova, Ekaterina  and
      Rehm, Georg",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italy",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.651",
    pages = "7389--7394",
    abstract = "The steep increase in the number of scholarly publications has given rise to various digital repositories, libraries and knowledge graphs aimed to capture, manage, and preserve scientific data. Efficiently navigating such databases requires a system able to classify scholarly documents according to the respective research (sub-)field. However, not every digital repository possesses a relevant classification schema for categorising publications. For instance, one of the largest digital archives in Computational Linguistics (CL) and Natural Language Processing (NLP), the ACL Anthology, lacks a system for classifying papers into topics and sub-topics. This paper addresses this gap by constructing a corpus of 1,500 ACL Anthology publications annotated with their main contributions using a novel hierarchical taxonomy of core CL/NLP topics and sub-topics. The corpus is used in a shared task with the goal of classifying CL/NLP papers into their respective sub-topics.",
}
```
