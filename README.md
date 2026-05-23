# Customer Segmentation Dashboard

## Overview

The Customer Segmentation Dashboard is an interactive data analytics application built using **Python**, **Machine Learning**, and **Streamlit**.
The project segments customers into distinct groups based on purchasing behavior, income, demographics, and shopping preferences to help businesses design targeted marketing strategies.

The application uses **KMeans Clustering** and **Principal Component Analysis (PCA)** to uncover hidden customer patterns and visualize them through an interactive dashboard.

---

## Project Files

### `app.py`

Main Streamlit application containing:

* Dashboard UI
* Cluster visualizations
* Business insights
* Interactive filtering and analysis

### `project 2.ipynb`

Jupyter Notebook containing:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature encoding
* Clustering model implementation
* PCA dimensionality reduction
* Cluster evaluation

### `customer_segments.csv`

Raw customer dataset used for analysis and segmentation.

### `df_enco`

Encoded and processed dataset used for clustering.

### `clus_mean`

Cluster-wise average values used for customer segment summaries.

---

## Objective

The main objective of this project is to:

* Identify distinct customer groups
* Understand customer behavior patterns
* Improve personalized marketing
* Enhance customer retention strategies
* Support data-driven business decisions

---

## Technologies Used

### Programming & Analysis

* Python
* Pandas
* NumPy
* Scikit-learn

### Visualization

* Plotly
* Matplotlib
* Seaborn
* Streamlit

### Machine Learning

* KMeans Clustering
* Principal Component Analysis (PCA)

---

## Features of the Dashboard

### 1. Customer Segment Overview

Provides a summary of all generated customer segments along with their behavioral characteristics.

### 2. Cluster Distribution Visualization

Displays customer distribution across segments using interactive pie charts.

### 3. PCA Scatter Plot

Visualizes customer clusters in a 2D PCA space for easier interpretation of segmentation patterns.

### 4. Segment-wise Trait Analysis

Shows average:

* Income
* Spending Score
* Purchase Frequency
* Last Purchase Amount
* Age Group

for selected customer segments.

### 5. Gender Distribution Analysis

Displays gender composition within each customer segment.

### 6. Preferred Product Category Analysis

Highlights the most preferred product categories among customers in each segment.

### 7. Age Group Distribution

Analyzes age demographics across customer segments.

### 8. Business Insights & Recommendations

Provides marketing recommendations and customer engagement strategies for each segment.

---

## Customer Segments Identified

| Segment                  | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| Young Budget Shoppers    | Young, low-spending customers interested in Home & Garden |
| Older Budget Enthusiasts | Older consumers with budget-conscious sports preferences  |
| Senior Premium Buyers    | High-income, frequent shoppers preferring groceries       |
| Budget Luxury Shoppers   | Lower-income but high-spending grocery shoppers           |
| Senior Premium Buyers 1  | Older electronics-focused premium shoppers                |
| Affluent Home Improvers  | Wealthy older customers preferring Home & Garden products |

---

## Machine Learning Workflow

### Step 1: Data Preprocessing

* Handled missing values
* Removed duplicates
* Encoded categorical variables
* Scaled numerical features

### Step 2: Exploratory Data Analysis

* Distribution analysis
* Correlation analysis
* Outlier detection
* Customer behavior exploration

### Step 3: Clustering

Applied **KMeans Clustering** to group customers based on:

* Income
* Spending behavior
* Purchase frequency
* Demographics
* Product preferences

### Step 4: Dimensionality Reduction

Used **PCA** to reduce dimensions and visualize clusters effectively.

---

## Business Use Cases

This project can help businesses:

* Create personalized marketing campaigns
* Improve customer retention
* Increase sales conversion
* Design loyalty programs
* Optimize product recommendations
* Understand customer purchasing patterns

---

## Sample Business Insights

* Young budget shoppers respond better to discounts and affordability-focused campaigns.
* Premium older customers prefer convenience and personalized experiences.
* Grocery-focused customers tend to have higher purchase frequency.
* Electronics buyers may respond well to financing and subscription services.

---

## How to Run the Project

### Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit scikit-learn
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

## Learning Outcomes

This project helped strengthen skills in:

* Machine Learning
* Customer Analytics
* Clustering Techniques
* Data Visualization
* Dashboard Development
* Business Insight Generation
* Streamlit Application Development

---

## Future Improvements

Possible future enhancements include:

* Real-time customer segmentation
* Recommendation system integration
* Predictive customer lifetime value analysis
* Deep learning-based segmentation
* Deployment on cloud platforms



## Conclusion

This Customer Segmentation Dashboard transforms raw customer data into actionable business insights using clustering techniques and interactive visualizations. It demonstrates how machine learning and analytics can support strategic decision-making and personalized customer engagement.


