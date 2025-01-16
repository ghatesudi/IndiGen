
# IndiGen: A Python-Based Synthetic Name Generator for Indian States

This package is a dynamic state-based Indian name generator. It allows users to generate names (either first names or full names) for specific states or for all states of India at once. The system dynamically imports state-specific modules and their corresponding name generation functions.

## Need for an Indian Name Generator
India is a diverse country with a rich tapestry of cultures, languages, and traditions. Each state has unique naming conventions that reflect its cultural and linguistic identity. An Indian name generator addresses this diversity and caters to various applications requiring culturally specific names.

This project caters to various applications, including:

- **Diversity Representation**: Ensuring names reflect India's unique cultural tapestry.
- **Localization**: Supporting region-specific datasets for marketing, content creation, and more.
- **Research**: Facilitating analysis of naming trends across Indian states.

## Features

- Dynamically loads state-specific modules for name generation.
- Generates first names or full names for specific states or all Indian states.
- Customizable output: specify the number of names to generate.
- Implements random seed for reproducible results.
- Comprehensive error handling for invalid inputs or module issues.

## Installation

```bash
# Clone the repository
git clone https://github.com/ghatesudi/Indigen.git

# Navigate to the project directory
cd Indigen

# Install dependencies
pip install -r requirements.txt

# Install the package directly from source (optional)
pip install .
```

## Usage

To run the main program:

```bash
python indigen.py
```

## Contribution

Contributions are welcome! If you find bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Directory Structure

```plaintext
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
├── License  # License for the project
├── requirements.txt  # List of dependencies
└── README.md  # Documentation for the project
```

## Random Seed Implementation

To ensure reproducibility of the generated names, a random seed is implemented. Users can set a specific seed value to guarantee the same sequence of names across runs. This feature is particularly useful for testing and debugging purposes.

Example usage with a random seed:

```python
from Indigen.main_script import generate_names

# Set random seed
import random
random.seed(42)

# Generate names
names = generate_names(state="Assam", num_names=5)
print(names)
```

## Running Tests

To run tests, use the following command:

```bash
python indigen.py
```

## Authors

- [@sudeepghate](https://github.com/ghatesudi/)
- [@dhanushghate](https://github.com/ddhanush)
- [@adithyam](https://github.com/adithyammathrushree)
- [@saishma_h]

## License

[MIT](https://github.com/ghatesudi/Indigen/blob/main/LICENSE)

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Special thanks to all contributors and users who provided feedback and helped improve the project. Their input has been invaluable in making this tool robust and user-friendly. 

We also acknowledge the inspiration drawn from the work: Sharma, R. S. (2005). *Panorama of Indian Anthroponomy: An Historical, Socio-cultural & Linguistic Analysis of Indian Personal Names*. Mittal Publications.
