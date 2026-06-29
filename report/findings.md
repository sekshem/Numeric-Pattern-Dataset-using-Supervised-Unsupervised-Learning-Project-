# Machine Learning Findings (Engineer 2)

## 1. Classification (Supervised Learning)

### Target Conversion
The original dataset contained a continuous `Target` variable. To apply classification models, it was converted into 3 balanced classes using quantile bins. This conversion is necessary because classification algorithms require discrete, categorical target labels to predict. 

**Class Distribution:**
- Low: 3350 (33.3%)
- Medium: 3350 (33.3%)
- High: 3350 (33.3%)

The classes are perfectly balanced (33.3% each), preventing the models from being biased toward a majority class.

### Model Comparison Table

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.9090 | 0.9087 | 0.9090 | 0.9088 | 0.9736 |
| **Decision Tree** | 0.9662 | 0.9661 | 0.9662 | 0.9661 | 0.9816 |
| **Random Forest** | 0.9706 | 0.9708 | 0.9706 | 0.9705 | 0.9848 |

### Best Classifier
**Random Forest** achieved an Accuracy of 0.9706, an F1 Score of 0.9705, and a weighted ROC-AUC of 0.9848, outperforming Logistic Regression by 6.16 percentage points in accuracy and Decision Tree by 0.44 percentage points. The ensemble tree-based structure of Random Forest captured the non-linear relationships and interactions in the data exceptionally well, making it unequivocally the best-performing model across all metrics.

---

## 2. Feature Importance

Extracting the true drivers from the optimal Random Forest model reveals the exact features influencing the target:

| Rank | Feature | Importance |
| :--- | :--- | :--- |
| 1 | Feature_2_Income | 0.5108 |
| 2 | Feature_3_Experience | 0.2258 |
| 3 | Feature_1_Age | 0.1859 |
| 4 | Feature_5_Skill | 0.0225 |
| 5 | Feature_6_Performance | 0.0148 |
| 6 | Feature_4_Education | 0.0098 |
| 7 | Feature_9_TrainingHours | 0.0088 |
| 8 | Feature_10_IQ | 0.0081 |
| 9 | Feature_8_Attendance | 0.0074 |
| 10 | Feature_7_Projects | 0.0061 |

**Interpretation:** 
The top three features (`Income`, `Experience`, and `Age`) are the dominant predictors, collectively accounting for over 92% of the predictive power. These core socioeconomic indicators heavily dictate the outcome of the `Target` variable, whereas features like `Skill` and `Performance` offer minimal predictive uplift.

---

## 3. Clustering (Unsupervised Learning)

### Linkage Comparison

| Linkage | Silhouette Score | Number of Clusters |
| :--- | :--- | :--- |
| Ward | 0.1398 | 3 |
| Complete | 0.5641 | 3 |
| Average | 0.5154 | 3 |
| Single | 0.4873 | 3 |

**Why Ward is better:**
While Complete, Average, and Single linkages technically scored higher Silhouette Scores (ranging from 0.4873 to 0.5641), evaluating their cluster sizes reveals an extreme chaining effect. They grouped roughly 10,000 samples into one massive cluster while isolating less than 50 outliers into the other two clusters (e.g., Single linkage clustered 10,000, 49, and 1). Ward linkage, despite a lower Silhouette Score (0.1398), provided highly meaningful, balanced segmentation that is actually actionable.

### Cluster Sizes & Interpretation (Ward Solution)

| Cluster | Samples | Mean Income | Mean Age | Mean Experience |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster 0** | 4944 | $138,198 | 30.7 | 8.5 years |
| **Cluster 1** | 5056 | $202,316 | 49.0 | 26.6 years |
| **Cluster 2** | 50 | $863,758 | 41.1 | 18.7 years |

**Interpretation:**
- **Cluster 0**: Represents the younger, early-career demographic with lower average income ($138k) and experience (8.5 years).
- **Cluster 1**: Captures the older, highly experienced professionals with significantly higher average income ($202k) and experience (26.6 years).
- **Cluster 2**: Identifies a tiny segment of 50 ultra-high-net-worth outliers, whose mean income ($863,758) massively skews away from the general population.

### Dendrogram Interpretation
Analyzing a sample of 100 observations via a dendrogram reveals long vertical branches before the final merges. The vertical height of the branches indicates distinct, well-separated macro-clusters, visually validating the natural cut point of 3 clusters.

### K-Means vs Hierarchical Comparison

| Metric | K-Means | Hierarchical (Ward) |
| :--- | :--- | :--- |
| **Silhouette** | 0.1691 | 0.1398 |
| **Davies-Bouldin** | 1.5795 | 1.7645 |
| **Calinski-Harabasz**| 1488.35 | 1246.27 |
| **Inertia** | 77529.79 | - |

**Discussion:**
K-Means produced slightly better clustering evaluation metrics (a higher Silhouette Score of 0.1691 and a lower Davies-Bouldin Index of 1.5795) compared to Hierarchical Ward. This is because K-Means directly optimizes spherical cluster variances. However, Hierarchical Clustering provides the dendrogram for superior interpretability and taxonomy generation without randomly initializing centroids. While K-Means performed slightly better quantitatively, Hierarchical was invaluable for mapping the structural relationships.

---

## 4. Final Conclusions
1. The conversion of the continuous `Target` variable into exactly equal terciles successfully established a robust classification baseline without class imbalance bias.
2. **Random Forest** proved to be the most accurate predictive model with a stellar Accuracy of 0.9706, heavily relying on `Income` and `Experience` to establish highly accurate non-linear predictions.
3. **Hierarchical Clustering (Ward)** successfully grouped observations into distinct, highly interpretable socioeconomic profiles (Early-Career, Experienced, and Ultra-High-Income Outliers). While K-Means offered slightly better spherical variance metrics, Ward linkage offered the most balanced structural insights.
