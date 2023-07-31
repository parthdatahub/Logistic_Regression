# LogisticReg_Classification
Titanic_Dataset_Logistic_Regression_e2eModel

Logistic Regression is a widely used supervised machine learning algorithm for binary and multi-class classification problems. It models the relationship between the dependent variable (binary outcome) and one or more independent variables by estimating probabilities. This repository provides an overview of the Logistic Regression algorithm and its application in classification tasks.

## Logistic Regression Algorithm Interview Questions

1. **What is Supervised Machine Learning?**
   Supervised machine learning is a type of machine learning where the algorithm learns from a labeled dataset to make predictions or decisions on unseen data. The algorithm is provided with input-output pairs during training.

2. **What is Logistic Regression, and when is it used?**
   Logistic Regression is a statistical algorithm used for binary and multi-class classification problems. It predicts the probability that an instance belongs to a particular class. It is commonly used when the dependent variable is binary (e.g., Yes/No, True/False) or when performing multi-class classification tasks.

3. **What is the Logistic Function (Sigmoid Function) used in Logistic Regression?**
   The Logistic Function, also known as the Sigmoid Function, maps any real-valued number to a value between 0 and 1. It is used in Logistic Regression to transform the output of linear regression into a probability score.

4. **What are the key assumptions of Logistic Regression?**
   Some key assumptions of Logistic Regression include:
   - Linearity: The relationship between the independent variables and the log-odds of the dependent variable should be linear.
   - Independence: The observations should be independent of each other.
   - Lack of multicollinearity: The independent variables should not be highly correlated with each other.

5. **How is the cost function (log loss) used in Logistic Regression?**
   The cost function (log loss) is used to evaluate the performance of the Logistic Regression model. It measures the difference between the predicted probabilities and the actual class labels. The goal is to minimize the log loss during training.

6. **What are the performance metrics used to evaluate Logistic Regression models?**
   Common performance metrics for evaluating Logistic Regression models include accuracy, precision, recall, F1-score, and ROC-AUC (Receiver Operating Characteristic - Area Under the Curve).

7. **What are the advantages of Logistic Regression?**
   - Simple and easy to implement.
   - Interpretable results, providing the probability of belonging to each class.
   - Suitable for both binary and multi-class classification problems.
   - Works well with linearly separable data.

8. **What are some techniques to handle multicollinearity in Logistic Regression?**
   Techniques to handle multicollinearity include:
   - Removing one of the correlated variables.
   - Using regularization techniques like Lasso or Ridge regression.

9. **How do you interpret the coefficients in Logistic Regression?**
   The coefficients in Logistic Regression represent the change in log-odds (logit) of the dependent variable for a one-unit change in the corresponding independent variable. A positive coefficient indicates a positive relationship, while a negative coefficient indicates a negative relationship with the dependent variable.

10. **What is the impact of feature scaling in Logistic Regression?**
    Feature scaling is not a strict requirement for Logistic Regression, as the algorithm is not sensitive to the scale of the features. However, feature scaling may help improve convergence speed and performance in certain cases.

11. **What are some common regularization techniques used in Logistic Regression?**
    Common regularization techniques in Logistic Regression include L1 regularization (Lasso) and L2 regularization (Ridge). They help prevent overfitting and improve the model's generalization ability.

12. **When should you use Logistic Regression over other classification algorithms?**
    Logistic Regression is suitable for binary and multi-class classification problems when the relationship between the independent variables and the log-odds of the dependent variable is approximately linear. It is often used as a baseline model and can be a good starting point for classification tasks.

Feel free to explore the code and use this repository to gain a better understanding of Logistic Regression for classification. If you have any questions or suggestions, don't hesitate to ask.
