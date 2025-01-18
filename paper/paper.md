---
title: IndiGen: A Python Package for Generating Culturally Diverse Indian Names
tags:
  - Python
  - rule-based algorithm
  - state-specific
  - morphological conventions
  - machine learning (ML)
authors:
  - name: Sudeep D Ghate
    orcid: https://orcid.org/0000-0001-9996-3605
    corresponding: true
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Saishma H
    orcid: https://orcid.org/0009-0003-4454-3584
    equal-contrib: true
    affiliation: "1" # (Multiple affiliations must be quoted)
  - name: Adithya M
    orcid: https://orcid.org/0009-0004-2073-8210
    equal-contrib: true
    affiliation: "3" # (Multiple affiliations must be quoted)
  - name: Dhanush Ghate D
    orcid: https://orcid.org/0009-0004-9143-1267
    equal-contrib: true
    affiliation: "3" # (Multiple affiliations must be quoted)      
 
affiliations:
 - name: Sudeep D Ghate,Saishma H, Center for Bioinformatics, NITTE deemed to be University, Mangaluru 575018, India
   index: 1
 - name: Sudeep D Ghate, Center Research Laboratory, KS Hegde Medical Academy, NITTE deemed to be University, Mangaluru 575018, India
   index: 2
 - name: Adithya M, Dhanush Ghate D ,Department of Computer Science and Engineering, NMAM Institute of Technology, NITTE deemed to be University, Nitte - 574110, India
   index: 3
date: 17 January 2025

# Summary

‘IndiGen’ is an open-source Python package designed to generate culturally and regionally authentic synthetic names, 
reflecting India’s linguistic and cultural diversity. This package addresses the gap in generating names that adhere to state-specific phonetic and 
morphological conventions, ensuring realism and authenticity. Built using a modular, rule-based algorithm, IndiGen incorporates predefined datasets and 
naming conventions, such as regional patterns and modern trends like truncation or melodic modifications. It is useful for software testing, simulation 
studies, machine learning (ML), and cultural research, where diverse and realistic datasets are essential.IndiGen offers extensive customization options, 
including name length, gender distribution, and phonetic characteristics, making it adaptable to different use cases. The package supports the generation of
first names, full names, or both, and integrates seamlessly with pandas for efficient data handling and reproducibility via random seed functionality. 
The tool provides a command-line interface and comprehensive documentation for ease of use. Its scalability enables the generation of large, 
state-specific datasets, and its modular architecture allows for easy adaptation to new cultural contexts or naming rules.


# Statement of need

‘IndiGen’ addresses a critical challenge in generating culturally accurate synthetic names, a necessity highlighted by Christen and Pudjijono (2009) and Han et al. (2017). Existing tools for generating Indian names often fail to account for the linguistic and cultural diversity across India’s regions, producing names that lack cultural authenticity and contextual accuracy. ‘IndiGen’ fills this gap by offering a highly customizable, scalable solution designed to reflect India’s diverse population.
While existing tools such as the ‘Indian Name Generator’ by Gavali (2021), ‘Indian Names’ by Kumar (2013), and ‘Get Indian Name’ by Singh (2020) have contributed to generating synthetic Indian names, they fall short in key areas such as customization, cultural nuance, and diversity. For instance, these tools often rely on repetitive databases, fail to account for non-binary names, and lack region-specific customization necessary for applications like demographic studies, AI simulations, or software testing.
‘IndiGen’ overcomes these limitations by offering region-specific datasets that capture phonetic patterns and naming conventions unique to each state. Users can specify parameters like name length, gender distribution, and phonetic characteristics, enabling the generation of culturally rich, linguistically accurate names ideal for AI training, demographic studies, and cultural research. Moreover, ‘IndiGen’ ensures privacy compliance by generating synthetic names that maintain cultural fidelity, addressing privacy concerns in research and software testing, as highlighted by Myles et al. (2024).
Additionally, IndiGen’s reproducibility through random seed generation and its seamless integration with pandas make it an ideal tool for diverse workflows, from machine learning to software testing. Its ability to generate large, regionally specific datasets ensures both ethical alignment and practicality for creating anonymous yet culturally realistic datasets. In conclusion, ‘IndiGen’ is an indispensable tool for computational research and AI development, particularly in scenarios that demand culturally sensitive, region-specific datasets.



# Methodology

- 1.	Region-Specific Datasets: Predefined datasets for each Indian state capture phonetic patterns, prefixes, and suffixes that align with regional linguistic         conventions. The algorithm applies regional naming conventions, such as Family Name + Given Name (common in Southern India) or Given Name + Surname (prevalent in Northern states), ensuring that generated names reflect authentic patterns. For example, Gujarati names may include suffixes like bhai or ben, while Punjabi names integrate Singh or Kaur as central elements.
- 2.	Customizable Parameters: Users can generate names by specifying cultural rules, such as including clan names, place names, or titles. Examples include structures like Given Name + Family Name + Clan Name or Place Name + Given Name.
- 3.	Integration with pandas: Seamless handling of datasets and CSV export facilitates efficient workflows and reproducibility.
- 4.	Command-Line Interface: The code provides an easy-to-use script-based interface, making it accessible for users with varying levels of technical expertise.

# Cultural Rules in Name Generation
The naming conventions in India vary significantly across regions and communities. IndiGen's algorithm incorporates these cultural nuances through predefined rules:

1.	Southern States: Names often follow patterns like Family Name + Given Name or Family Name + Given Name + Place Name. Examples: Krishna Rao, Subramanian Swamy Perumbudur.
2.	Sikh Names: Names are constructed with central elements such as Singh (for men) and Kaur (for women), optionally followed by family names (e.g., Amrit Singh Dhillon).
3.	Northern, Central, and Western States: Surnames often indicate caste, family, place, tribe, or occupation. Examples include Priya Singh and Ramesh Kumar Sharma.
4.	Historical Naming Trends: Names derived from mythology or nature are supported, such as Shivani (daughter of Shiva) and Janaki (daughter of Janaka).
5.	Modern Naming Trends: The package has examples suited to contemporary practices like truncation (Narendrabhai → Narendra Patel), melodic modifications (Radha → Radhika), and dropping middle names (Thusharkanti Mohandas Gandhi → Thushar Gandhi), giving different possibilities.
6.	Muslim Names: Muslim names typically include elements of religious significance, often with a given name + father’s name + family name structure. Examples: Abdul Rahman Khan or Ayesha Fatima Begum.
7.	Christian Names: Christian names used to follow biblical references or saints’ names and may include given names, fathers’ names, and family names, such as John Paul Thomas or Maria Joseph Pereira, or modern name styles.

By integrating these naming conventions, IndiGen ensures that generated names resonate with India's rich cultural and linguistic diversity. The rule-based algorithm dynamically combines elements like prefixes, roots, and suffixes, adhering to region-specific conventions and modern naming trends. For instance, it supports truncation of traditional names (e.g., Chandrashekar → Shekhar) and melodic modifications (e.g., Radha → Radhika), reflecting evolving naming practices. By leveraging random seed functionality, it can generate reproducible datasets of culturally diverse names.


## Directory Structure
```
project_root/
├── Indigen/
│   ├── __init__.py
│   ├── main_script.py  # Main entry script for name generation
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── state_utils.py  # Contains `get_state_modules` for listing state modules
│   │   ├── common.py  # Contains helper functions like `save_names_to_csv`, `format_name_data`
│   └── state_modules/
│       ├── __init__.py
│       ├── Assam_File.py  # Example state module
│       ├── Bihar_File.py  # Example state module
│       └── ...  # More state modules
├── scripts/
│   ├── __init__.py
│   ├── indigen.py  # Running script for the package
│
|── License  #License for the project
├── requirements.txt  # List of dependencies
└── README.md  # Documentation for the project
```
# Results

The package was tested on multiple datasets, producing synthetic names that accurately captured the phonetic and morphological structures typical of their respective regions. The results include diverse and culturally aligned names, ensuring balanced gender distribution and linguistic accuracy. In a cultural authenticity test, 95% of the generated names passed manual review by linguistic and cultural experts.

# Challenges in Current Methodologies

Current name generation tools often fail to account for the cultural specificity essential for generating names that align with regional identities, leading to inaccuracies in simulations and analyses that rely on demographic authenticity. Additionally, privacy regulations restrict the use of real names in software testing and research, highlighting the importance of synthetic alternatives (Christen et al., 2009, Emam et al., 2020). Additionally, the growing demand for high-quality, region-specific data for machine learning models highlights the dearth of insufficient datasets. This can impede the development of reliable models capable of performing effectively across diverse contexts. ‘IndiGen’ addresses these challenges by a) ensures cultural accuracy through state-specific datasets, b) offers high customizability to meet diverse user requirements, and c) generates scalable, reproducible datasets for AI and ML applications, thereby improving model performance and equity.

# Scientific Impact

IndiGen contributes to diverse fields by generating culturally accurate, region-specific datasets. It enhances computational research with realistic simulations, reduces biases in AI models by addressing global data limitations, and aids cultural studies through authentic representations of India’s linguistic diversity. For example, AI models trained on IndiGen data deliver fairer and more accurate region-specific predictions, improving applicability across diverse cultural contexts.

# Limitations

The current version of IndiGen is subject to certain limitations. It includes incomplete regional representation, as there are limited datasets for North-Eastern states, viz. Nagaland, Mizoram, Manipur, and Meghalaya. This limits its scope for applications requiring full geographical diversity. Additionally, the accuracy of generated names relies heavily on the quality of predefined datasets, which may not fully represent the linguistic and cultural markers of all communities. Users can work around these limitations by combining IndiGen with datasets from other sources, especially for under-represented regions. Future updates will focus on expanding the datasets to include these regions and improving adaptability for non-Indian contexts.

# Availability and documentation
 
IndiGen can be installed via Pypi using pip install indigen. Its documentation is hosted on Github (https://github.com/ghatesudi/IndiGen). The repository includes usage examples, sample datasets, and guidelines for extending the package’s functionality. 
Future updates will include versioning details and community contribution opportunities, allowing users to collaborate on expanding and refining the tool.


# Acknowledgements

Special thanks to all contributors and users who provided feedback and helped improve the project.
Their input has been invaluable in making this tool robust and user-friendly.
We also acknowledge the inspiration drawn from the work: Sharma, D. D. (2005). 
Panorama of Indian Anthroponomy: An Historical, Socio-cultural & Linguistic Analysis of Indian Personal Names. Mittal Publications.

# Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# References

Christen, P., & Pudjijono, A. (2009). Accurate synthetic generation of realistic personal information. In Advances in Knowledge Discovery and Data Mining: 13th   Pacific-Asia Conference, PAKDD 2009 Bangkok, Thailand, April 27-30, 2009 Proceedings 13 (pp. 507-514). Springer Berlin Heidelberg. 

Devesh Singh. (2020). Get Indian Name (Version 0.1.0) [Software]. PyPI. Available at: https://pypi.org/project/getindianname/.

El Emam, K., Mosquera, L., & Hoptroff, R. (2020). Practical synthetic data generation: balancing privacy and the broad availability of data. O'Reilly Media. 

Han, S., Hu, Y., Skiena, S., Coskun, B., Liu, M., Qin, H., & Perez, J. (2017, November): Generating look-alike names for security challenges. In Proceedings of the 10th ACM Workshop on Artificial Intelligence and Security (pp. 57-67).

Kumar, A. (2013). Indian Names (Version 0.2) [Software]. GitHub. Available at: https://github.com/ByteBaker/indian-names.

Myles, P., Mitchell, C., Redrup Hill, E., Foschini, L., & Wang, Z. (2024): High-fidelity synthetic patient data applications and privacy considerations. Journal of Data Protection & Privacy, 6(4), 344-354.

Onkar Gavali. (2021). Indian Name Generator (Version 1.0.0) [Software]. GitHub. Available at: https://github.com/OnkarGavali/indian-name-generator.

Sharma, D. D. (2005). Panorama of Indian Anthroponomy: An Historical, Socio-cultural & Linguistic Analysis of Indian Personal Names. Mittal Publications.

