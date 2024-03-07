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
@InProceedings{forc4cl,
  author    = {Abu Ahmad, Raia and Borisova, Ekaterina and Rehm, Georg},
  title     = {FoRC4CL: A Fine-grained Field of Research Classification and Annotated Dataset of NLP Articles},
  booktitle      = {Proceedings of the Joint International Conference on Computational Linguistics, Language Resources and Evaluation},
  year           = {2024},
  comment = {Accepted at LREC-COLING 2024. Link will be provided when available.}
}
