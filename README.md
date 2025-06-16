# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Health Insurance Cost Analysis

## Overview
This project provides a comprehensive analysis of a health insurance dataset to uncover the primary factors influencing insurance charges. Leveraging Python and a suite of data analysis and visualisation libraries, the project investigates how variables such as BMI and smoking status impact insurance costs. The analysis is designed to offer actionable insights for both individuals and insurance providers.

## Objectives
- Identify and evaluate the variables that most significantly affect health insurance charges through exploratory data analysis and visualisation.
- Compare insurance charges between smokers and non-smokers to assess the impact of smoking status.
- Examine the relationship between BMI and insurance charges by grouping BMI values and visualising average costs.
- Utilise both interactive (Plotly) and static (Matplotlib) visualisations to effectively communicate findings.

## Data
- **Source:** `data/cleaned_insurance.csv`
- **Key Features:**  
  - `age`: Age of the policyholder  
  - `sex`: Gender of the policyholder  
  - `bmi`: Body Mass Index  
  - `children`: Number of dependents  
  - `smoker`: Smoking status  
  - `region`: Residential region  
  - `charges`: Annual insurance charges

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed. The following packages are required:
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- kaleido
You can install them using:
GitHub Copilot
pip install pandas numpy matplotlib seaborn plotly kaleido

### Running the Analysis
1. **Clone the repository** to your local machine.
2. **Navigate to the project directory** and open the Jupyter notebook located in the `jupyter_notebooks` folder.
3. **Run the notebook cells** sequentially to perform the analysis and generate the visualisations.

## Results and Insights
- **Smoking status** is the most significant factor, with smokers incurring substantially higher insurance charges than non-smokers.
- **BMI** is also a key variable; higher BMI values are associated with increased insurance costs, particularly for smokers.
- The combination of being a smoker and having a high BMI results in the highest insurance charges observed in the dataset.
- All findings are supported by clear visualisations and detailed insights within the notebook.

## Challenges and Solutions

**Challenge 1: Handling Missing or Duplicate Data**  
*Solution:*  
Careful data cleaning steps were implemented to check for and remove any missing values or duplicate records, ensuring the integrity of the analysis.

**Challenge 2: Displaying Interactive Visualisations on GitHub**  
*Solution:*  
GitHub does not support interactive Plotly plots in notebook previews. To address this, static images of the interactive plots were generated and embedded in the notebook, allowing the visual insights to be shared effectively.

**Challenge 3: Package and Environment Issues**  
*Solution:*  
Some required packages (such as `kaleido` for saving Plotly images) were not initially installed, leading to errors. These were resolved by installing the necessary packages and restarting the Jupyter kernel to ensure all dependencies were correctly loaded.

**Challenge 4: File Path and Directory Management**  
*Solution:*  
Issues with file paths and working directories were resolved by programmatically setting the working directory at the start of the notebook, ensuring data files could be accessed regardless of the notebook’s location.


## Conclusion and Next Steps

This project provided clear insights into the main factors influencing health insurance charges. Smoking status emerged as the strongest predictor, with smokers consistently facing much higher charges than non-smokers. BMI also plays a significant role—higher BMI leads to higher average charges, and the effect is even greater for smokers with high BMI. Both factors together result in the highest insurance costs in the dataset.

If I were to extend this project, I would:
- Investigate additional variables, such as medical history or lifestyle factors, to gain deeper insights.
- Analyse how insurance charges change over time, if longitudinal data becomes available.
- Compare findings with other datasets or regions to see if similar patterns exist elsewhere.



## Reflection

Working on this project, my first data analysis project, has deepened my understanding of data analysis and visualisation in Python. I learned how to approach a real-world dataset, clean and prepare the data, and use different libraries to uncover meaningful insights. Overcoming technical challenges, such as troubleshooting errors and managing my coding environment, has improved my problem-solving skills. I also gained confidence in presenting findings clearly through both code and visualisations. Overall, this experience has strengthened my analytical abilities and prepared me for more advanced data projects in the future.


## Credits & References

- **ChatGPT (OpenAI):**  
  I relied on ChatGPT for guidance throughout the project, especially when I faced challenges. For example, it helped me:
  - Structure my markdown cells and clearly write out hypotheses and objectives.
  - Troubleshoot errors, such as resolving Plotly issues caused by missing `nbformat`, fixing unexplained SyntaxErrors by restarting VS Code, and sorting out virtual environment activation problems in the terminal.
  - Format my visualisations, like removing error bars from seaborn plots and customising legends in Plotly scatter plots.
  - Understand technical concepts, including how `groupby().mean().reset_index()` works, the difference between `sns.barplot()` and `plt.bar()`, and the role of legends and trendlines in data visualisation.

- **GitHub Copilot:**  
  GitHub Copilot in VS Code was helpful for autocompleting repetitive code and suggesting clean, efficient syntax, particularly during data visualisation and data transformation steps.

- **External Dataset Sources:**  
  I reviewed exploratory analysis notebooks from other Kaggle users to understand common approaches. I adapted some initial code for loading and inspecting the data (such as using `.info()`, `.describe()`, and `.isnull().sum()`) from these examples.

## Acknowledgements
***Thanks to:***
- Code Institute for guidance on project structure
- Kaggle for providing access to the dataset
- ChatGPT and GitHub Copilot for coding assistance
- Fellow Code Institute students for their support and encouragement