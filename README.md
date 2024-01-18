# <img src="https://upload.wikimedia.org/wikipedia/zh/thumb/d/db/Tamkang_University_logo.svg/630px-Tamkang_University_logo.svg.png" alt="Editor" width="50"> Master's Thesis
## Biomedical literature mining - graph kernel based on distant supervision for extracting gene-gene interactions
### _*109 Academic year －Tamkang University Department of Statistics  Graduation Thesis － Tsai Chen Yu_

Github:<https://github.com/TSAI-CHEN-YU/tku-stat-608650213>

## The program in the paper  

### Data in PubMed

- **data from KEGG**  
`KEGG.ipynb`

- **data from MeSH Keywords**  
`PubMed data by Mesh Term Search.ipynb`

### Preproccenig

- **data preproccenig**  
`DS_Pre.ipynb`

### Classification in different training set

- **data ratio(1:3) & graph weight(0.3)**  
`DS_Classifier(0.3)_R_3.ipynb`

- **data ratio(1:3) & graph weight(0.1)**  
`DS_Classifier(0.1)_R_3.ipynb`

- **data ratio(1:10) & graph weight(0.3)**  
`DS_Classifier(0.3)_R_10.ipynb`

- **data ratio(1:10) & graph weight(0.1)**  
`DS_Classifier(0.1)_R_10.ipynb`

- **data ratio(1:100) & graph weight(0.3)**  
`DS_Classifier(0.3)_R_100.ipynb`

- **data ratio(1:100) & graph weight(0.1)**  
`DS_Classifier(0.1)_R_100.ipynb`

### Result analysis

- **McNemar test**  
`McNemar.ipynb`

- **result validation**  
`result_validation.ipynb`

### Test example

To test the operation of the code in the paper, you can use the files in the example folder. Please read the precautions in `(example.zip)example/readMeToTestExample.md` before using.

### PubMed

The `PubMed/Pubtator_all_result.txt` file is obtained from the [pubTator API](https://www.ncbi.nlm.nih.gov/research/pubtator/api.html) and contain PMID, abstract titles, abstract content, and the entities included in them. The data covers the period from January 1, 1946, to January 1, 2021.
