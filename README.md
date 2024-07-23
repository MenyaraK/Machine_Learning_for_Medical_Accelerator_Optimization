# Machine Learning for Medical Accelerator Optimization

## Project Overview
This project, developed as part of the end-of-year project at the National Institute of Applied Sciences and Technology, University of Carthage, is titled "Development of a Computer Model Based on Learning Methods to Automate Planning for External Radiotherapy Treatment". It has been crafted under the supervision of Dr. Youssef El Mahroug, with contributions from distinguished academics and professionals within the field.

### Background
External beam radiation therapy is an established method for treating various types of cancer, utilizing high-energy ionizing radiation to destroy cancer cells. The precision in delivering a targeted dose of radiation while minimizing exposure to surrounding healthy tissues is paramount for the success of this treatment. Traditional methods for determining beam parameters, while effective, are often slow and susceptible to human error, underscoring the need for enhancements through automation.

### Objective
The primary goal of this project is to automate the process of determining initial beam parameters for the Varian 2100 linear accelerator using machine learning techniques. This involves using a trained neural network model to predict initial beam energy parameters based on data generated from extensive simulations with PRIMO software— a tool based on the Monte Carlo statistical method.

### Innovation
By integrating artificial intelligence into the planning phase of external radiotherapy, the project aims to significantly enhance treatment efficiency and accuracy. This model provides a pivotal step towards dose optimization, crucial for improving patient treatment outcomes. Additionally, the flexibility of the model allows for future adaptations to include a broader range of beam parameters, potentially revolutionizing the approach to radiotherapy treatment planning.

### Methodology
The approach is rooted in the application of artificial neural networks, specifically Multilayer Perceptrons (MLP), to model and predict the necessary radiation dose distributions. Data for training the model is sourced from simulated outputs of the PRIMO software, ensuring a robust foundation for the neural network's learning process.

For more information or to contribute to this project, please refer to the contact and contribution sections of this document.


## Features

- Data loading and preprocessing from CSV files.
- Visualization of energy distributions and relationships.
- Training of a neural network to predict energy outputs.
- Evaluation of model performance and visualization of prediction accuracy.

## Prerequisites

Before you run this project, you need to have the following installed:
- Python 3.9 or later
- pip (Python package installer)

## Installation
To set up this project, follow these steps:

1. Clone the repository:
   git clone https://github.com/MenyaraK/Machine_Learning_for_Medical_Accelerator_Optimization.git
2. Install the required dependencies: 
    pip install -r requirements.txt

## Usage
To run this project, follow these steps:
- Run the main script:python main.py

## Structure
data/: Directory for dataset storage.
models/: Directory where trained models are saved.
src/: Python scripts for loading data, preprocessing, training, and testing.
outputs/: Storage for outputs like plots and results text files.


## Contributions and Acknowledgments
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.
This project not only contributes to the academic field by linking advanced machine learning techniques with practical medical applications but also serves as a testament to the collaborative efforts between students and experts in the medical and engineering communities. Special thanks are extended to Dr. Youssef El Mahroug for his invaluable guidance, as well as to Mrs. Hella Adouni and Mrs. Rania Maktouf for their roles as examiners.

## Conclusion
"Machine Learning for Medical Accelerator Optimization" sets a precedent for future research and development in the intersection of technology and healthcare. It exemplifies how machine learning can be applied to enhance precision in cancer treatment, paving the way for more adaptive and efficient therapeutic techniques.
