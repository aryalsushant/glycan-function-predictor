# Glycan Function Predictor

A machine learning-powered tool that leverages the OpenAI GPT-4 API to predict potential biological functions of glycan structures based on their IUPAC sequences. This project demonstrates the application of artificial intelligence in glycobiology research and molecular function prediction.

## Overview

The Glycan Function Predictor uses natural language processing to analyze glycan sequences and predict their biological roles, focusing on:

- Immune system signaling
- Cell adhesion mechanisms
- Disease-related processes
- Protein-glycan interactions

## Features

- **IUPAC glycan sequence input support**
- **AI-powered function prediction using GPT-4**
- **Detailed explanations of predicted biological roles**
- **Environment variable management for secure API key handling**
- **User-friendly command-line interface**

## Technical Stack

- **Python 3.8+**
- **OpenAI GPT-4 API**
- **python-dotenv for environment management**
- **Natural Language Processing for biological sequence analysis**

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/glycan-function-predictor.git
cd glycan-function-predictor
```

Install required packages:

```bash
pip install openai python-dotenv
```

Create a `.env` file in the project root and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:

```bash
python glycan_predictor.py
```

Enter your glycan sequence when prompted using IUPAC notation.

Example input:

```plaintext
Enter a glycan sequence in IUPAC format: Neu5Ac(α2-3)Gal(β1-4)GlcNAc
```

## How It Works

1. The program takes a glycan sequence in IUPAC format as input.
2. Constructs a detailed prompt for the GPT-4 model.
3. Analyzes the sequence using natural language processing.
4. Returns predicted biological functions and explanations.

## Applications

- Research in glycobiology and glycomics
- Drug development and disease research
- Understanding protein-glycan interactions
- Molecular biology research
- Bioinformatics analysis

## Future Enhancements

- Integration with glycan databases
- Batch processing capabilities
- Web interface development
- Extended validation for IUPAC sequences
- Integration with molecular visualization tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

