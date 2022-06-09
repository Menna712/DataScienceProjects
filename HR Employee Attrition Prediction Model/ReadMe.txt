This is a Machine Learning based Model to Predict if an employee is going to leave an organization based on their attrition(Y/N).

since there is a labeled dependent variable (Attrition) i considered this as a Supervised Model.
also since the question to be answered and dependeing on the label is (Y/N) i consider this a classification Model.
....

now that i understand the Question and what answer i need to solve i start understanding the data.
i Read the DataSet of 1470 Rows of Employee Information in an Organization.
I start Plotting and comapring data to understand this data and it's distribution in aim to remove the unwanted Columns.
Removing unwanted data(Dimensional reduction) is a very important step that contributes in the Training Time and accuracy percentage.

After dimensional Reduction , i use many techniques to furthermore remove any unwanted features(Pearson , Logistic Regression)

And this is how i Extracted the Features i will use in the Machine Learning Models.
....

The Machine Learning Models i applied:
1)Logistic Regression that resulted in accuracy of approximately 85%
2)Random Forest that resulted in accuracy of approximately 95%

i have many other ideas to be done in Enhancement phase.
as an example : SMOTE can be used on training data to generate synthetic minority samples with respect to noisy samples outside the borderlines
thus, producing useless synthetic samples
