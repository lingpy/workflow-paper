# Computer-Assisted Language Comparison: State of the Art
We present our computer-assisted language comparison workflow which starts with raw data and lifts up to a stage where sound correspondence patterns across multiple languages have been identified and can be readily presented, inspected, and discussed. Our workflow works with all the languages in general, however, we highly encourage linguists who work with Southeast Asian languages to try out this workflow. Because our workflow attempts to work with two major features of Southeast Asian langauges: 
 * high frequency of compund words.
 * a common template can be found in most of the morphemes. 
 
The workflow consists of 5 different stages and make use of several Python libraries that interact, one producing the data that can be used by the other. Since the data is available in different stages, each stage allows us to intervene by correcting errors manually that were made by the automated approach. Our illustration is accompanied by Python code and instructions on how to use additional web-based tools we developed so that users can apply our workflow for their own purposes.

The manuscript has been accepted for publication with the *Journal of Open Humanities Data*. When using the processed data or the code to process data in your research, please cite this study as:

> Wu, M.-S.; Schweikhard, N. E.; Bodt, T. A.; Hill, N. W. & List, J.-M. (forthcoming): "Computer-Assisted Language Comparison. State of the Art. *Journal of Open Humanities Data*. 

The corresponding BibTeX format is:

```
@Article{Wu2020,
  author     = {Wu, Mei-Shin and Schweikhard, Nathanael E. and Bodt, Timotheus A. and Hill, Nathan W. and List, Johann-Mattis},
  title      = {Computer-Assisted Language Comparison. State of the Art},
  journal    = {Journal of Open Humanities Data},
  year       = {forthcoming},
  howpublished = {Accepted for publication in 2020}
}
```
## The dataset 
We illustrate this workflow with the help of a newly prepared dataset on Hmong-Mien languages. The lexical data was drawn from the book: Chen, Qiguang (2013) : Miao and Yao language. Beijing: Ethnic Publishing House. 

The source of the dataset is archived on Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3741500.svg)](https://doi.org/10.5281/zenodo.3741500)

## Code Ocean Capsule
In order to facilitate it for users to quickly test our workflows without installing the software, we have set up a [Code Ocean Capsule] (https://codeocean.com/capsule/8178287/tree/v2) which users can use to run the code remotely. The [Tutorial.pdf] (https://github.com/lingpy/workflow-paper/blob/master/Tutorial.pdf) gives more information about the Code Ocean capsule and how to test the workflow on this platform.

## Tutorial
In the [Tutorial.pdf] (https://github.com/lingpy/workflow-paper/blob/master/Tutorial.pdf), we detail two ways to work with our workflow, one way is to use `cldfbench` commandline directly, the instructions are also given in the [NOTEs.md in the chenhmongmien repository] (https://github.com/lexibank/chenhmongmien/blob/master/NOTES.md). The other method is to use the Python scripts we provide here. 

## Python scripts

| Python script | Functions |Manuscript|
| -------------:|:----------|:----------|
| `1_lifting.py`|From raw data to tokenized data| 3.2.1 |
|`1_lifting_example.py`|From raw data to tokenized data, an example to take 25 varieties| tutorial|
| `2_partial.py`|From tokenized data to cognate sets| 3.2.2|
| `3_alignment.py`|From cognate sets to alignments| 3.2.3 |
| `4_crosssemantic.py`|From alignments to cross-semantic cognates| 3.2.4|
| `5_correspondence.py`|From ross-semantic cognates to sound correspondence patterns| 3.2.5|
| `P_validate.py` | The python script to generate a distance matrix |Discussion|

## Interactive web-based applications
To use our workflow, there are two web-based applications that are particularly important regarding the data preparation and inspection.
- Profile : http://calc.digling.org/profile/
- EDICTOR : http://edictor.digling.org/

Especially, EDICTOR is used for inspecting the data in different stages. The [Tutorial.pdf] (https://github.com/lingpy/workflow-paper/blob/master/Tutorial.pdf) gives detail on how to work with the EDICTOR application.  
