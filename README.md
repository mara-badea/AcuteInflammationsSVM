## A python project using a database and ML algorithms to assess whether a person has inflammation of urinary bladder or nephritis of renal pelvis origin
### Used algorithm
I used the Support Vector Machine (SVM) Supervised Machine Learning algorithm and I used it for classification purposes.

### Dataset: <br/>
https://archive.ics.uci.edu/ml/datasets/acute_inflammations <br/>
Data dimension: 120x6

### -- Attribute lines of the database: <br/>
For example, '35,9 no no yes yes yes yes no' <br/>
Where:<br/>
'35,9' Temperature of patient<br/>
'no' Occurrence of nausea<br/>
'no' Lumbar pain<br/>
'yes' Urine pushing (continuous need for urination)<br/>
'yes' Micturition pains<br/>
'yes' Burning of urethra, itch, swelling of urethra outlet<br/>
'yes' decision: Inflammation of urinary bladder<br/>
'no' decision: Nephritis of renal pelvis origin<br/>

### Used libraries
1. numpy 
2. sklearn
3. sklearn.model_selection
4. os

### Data usage
The data is randomly divided into 75% train data and 25% test data ***train_test_split*** function.

### Parameters

The kernel (it is linear) and gamma parameter (it is 1) are always the same in my code and I am varying the C parameter between 0.3125 and 128 to see whether or not it affects the final result.

### Results

According to the accuracy, the database is a easy one to learn using this algorithm.





