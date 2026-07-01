
Final Analysis

1. Which preprocessing technique improved model performance?
StandardScaler produced the most stable performance across the ensemble models by ensuring numerical features were on comparable scales.

2. Which supervised model performed the best and why?
HistGradientBoosting Classifier achieved the highest overall accuracy with strong generalization and efficient handling of numerical data.

3. Which clustering algorithm generated the most meaningful clusters?
Gaussian Mixture Model (GMM) generated more meaningful clusters because it models probability distributions rather than assigning hard cluster boundaries.

4. How were clusters interpreted?
Clusters were interpreted based on feature distributions, probability estimates, and PCA visualization, revealing groups of similar numerical patterns.

5. What hidden numerical patterns were discovered?
The dataset contained well-separated groups with overlapping boundary regions that were effectively captured by probabilistic clustering.

6. Which model would you recommend for deployment?
HistGradientBoosting Classifier is recommended due to its high accuracy, fast prediction capability, and strong robustness.

7. What improvements could further increase performance?
Hyperparameter tuning, feature engineering, feature selection, ensemble stacking, and larger datasets could further improve performance.
