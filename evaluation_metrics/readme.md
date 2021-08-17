# Evaluation metrics
If we talk about **classification** problems, the most common metrics used are:
- accuracy
- precision (p)
- recall (r)
- F1 score (f1)
- area under the ROC (Receveier Operating Characteristic) curve or simply AUC (area under the curve)
- log loss
- precision as k (P@K)
- average precision at k (AP@K)
- mean average precision at k (MAP@K)

When it comes to **regression**, the most commonly used evaluation metrics are: 
- mean absolute error (MAE)
- mean squared error (MSE)
- root mean squared error (RMSE)
- root mean squared logarithmic error (RMSLE)
- mean percentage error (MPE)
- mean absolute percentage error (MAPE)
- R^2

# Take home messages
- When we have an equal number of positive and negative samples in a binary classification metric, we generally use *accuracy*, *precision*, *recall*, and *f1*.
  - **true positive (TP)**: prediction corresponds to ground truth
  - **true negative (TG)**: prediciton corresponds to ground truth
  - **false positive (FP)**: prediction is positive while ground truth is negative
  - **false negative (FN)**: prediction is negative while ground truth is positive

## Precision
Precision is the ratio between the True Positives and all the Positives. For example, the measure of patients that we correctly identify having a heart disease out of all the patients actually having it.

$Precision = TP / (TP + FP)$
<br>
or
<br>
$Precision = Correct Positive Guesses / Total Positive Guesses$

<br>**A precise model is a CONSERVATIVE MODEL**<br>
Example: *House alarm: every time it rings, you can be sure it is a thief. But it won't ring all the time. It is conservative, and rings only when he is very sure.* 
Mnemonic: how precise is positive selection

## Recall (or  *True Positive Rate (TPR)* or *Sensitivity*)
The recall is the measure of our model correctly identifying True Positives. Thus, for all the patients who actually have heart disease, recall tells us how many we correctly identified as having a heart disease. Mathematically:

$Recall = TP / (TP + FN)$
<br>
or
<br>
$Recall = Correct Positive Guesses / All Positive Labels$

<br>**A high recall model is LIBERAL**<br>
Example: *House alarm: it rings often - it usually catches a thief, but sometimes even a cat can trigger it. It goes off very easily (sensible).* 
<br>
<br>
For a "good" model, our precision and recall values should be high. When precision is low and recall is high, our model produces a lot of false positives but less false negatives.

It is challenging to choose threshold values (x > t --> 1, x < t --> 0) that give both good precision and recall values. If the threshold is too high, you have a smaller number of true positives and a high number of false negatives. If you reduce the threshold too low, false positives will increase a lot and precision will be less.

Both precision and recall range from from 0 to 1 and a value closer to 1 is better. 

## F1 score
F1 score is a metric that combines both precision and recall. It is defined as a simple weighted average (harmonic mean) of precision and recall. If we denote precision using P and recall using R, we can represent F1 score as:

$F1 = 2PR / (P + R))$ <br>
or <br>
$F1 = 2TP/(2TP + FP + FN)$ 
<br>
<br>
Instead of looking at precision and recall individually, you can also just look at the f1 score. Same as for precision, recall and accuracy, f1 score also ranges from 0 to 1 and a perfect prediction model has f1 score of 1. 
<br><ins>When dealing with datasets that have skewed targets, we should look at f1 instead of accuracy.</ins>

## False Positive Rate 
False Positive Rate, also defined as:<br>
$FPR = FP / (TN + FP))$ <br>

## Specificity or True Negative Rate (TNR)
Also defined as $1 - FPR$ 

## Log loss
We define log loss as:
<br>
<br>
$Log Loss = -1.0 * (target *log(prediction) + (1-target)*log(1-prediction))$ 

There the target is either 0 or 1 and prediction is a probability of a sample belonging to class 1.

For multiple samples in the dataset, the log loss over all samples is a mere average of all individual log losses. One thing to remember is that log loss penalizes quite high for an incorrect or far-off prediction, i.e. log loss punishes you for being very sure or very wrong.

____
Most of the metrics discussed so far can be converted to a multi-class version. Let's take precision and recall for instance. We can calculate precision and recall for each class in a multi-class classification problem.

There are three different ways to calculate this which might get confusing from time to time. Let's assume we are interested in precision first. We know that precision depends on true positives and false positives. 
- **macro averaged precision**: calculate precision for all classes individually and then average them
- **micro averaged precision**: calculate class wise true positive and false positive and then use that to calculate overall precision
- **weighted precision**: same as macro but in this case it is weighted  depending on the number of items in each class

Similarly, we can implement recall metric for multi-class.

## Bonus: Cohen's Kappa (Quadratic Weighted Kappa, QWK)
QWK measures the "agreement" between two ratings. The ratings can be any real numbers in 0 to N. And predictions are also in the same range. An agreement can be defined as how close these ratings are to each other. So it's suitable for a classification problem with N different categories/classes. If the agreement is high, the score is closer to 1 (and viceversa 0). [Implementation in scikit-learn --> metrics.cohen_kappa_score]

# Multi-label classification
## Precision at k (P@k) & AP@k
One must not confuse this precision with the precision mentioned earlier. If you have a list of original classes for a given sample and list of predicted classes, precision is defined as the number of hits in the predicted list considering only the top k predictions, divided by k.
<br>
By extension, it AP@k is just the averaged precision at k. MAP@K is just the total average.
<br>
P@k, AP@k and MAP@k all range from 0 to 1 with 1 being the best.

## Log loss
You can convert the targets to binary format and then use a log loss for each column. In the end, you can take the average of log loss in each column. This is also known as column-wise log loss.

# Regression
## Error
Very easy to understand. 
<br>
$Error = True Value - Predicted Value$ 

## Absolute error
Absolute error is just the absolute of the above
<br>
$Absolute Error = Abs(True Value - Predicted Value)$

## Mean Absolute Error (MAE)
It is just the mean of all absolute errors.

## Mean Squared Error (MSE)
Similarly, we have squared error and mean squared error

## Root Mean Squared Error (RMSE)
MSE and Root Mean Squared Error (RMSE) are the most popular metrics used in evaluating regression models
<br>
$RMSE = SQRT(MSE)$

## Percentage Error
$Percentage Error = ((True Value - Predicted Value) / True Value) * 100$

## Coefficient of Determination $R^{2}$
R-Squared says how good your model fits the data. 