# House-Predictor
Predicts house value based on lot sq. ft

# To Run:
-Used Google Colab to run\
-Need dataset from Kaggle to run this program, which I lost unfortunately, but code can be refactored to work for any other house prices dataset, just make sure it's saved to the same directory as the program.\
-In Colab, you need to upload the file and the path becomes /content/filename

# Notes for me
.fit() trains the model. Takes an input array and an output array (target values the inputs should map to)
adjusts model's params to find best-fit line with lowest RSS (sum of residuals). 

.reshape() reshapes the 1D input array (a row) to a 2D array (column), which is the input shape that the model takes.
args (-1, 1): -1 means Numpy should infer the size of one dimension based on the input. The other dimension size is specified by you (1). -1 just handles the calculations for you in cases where you have a big input and calculating the rows * cols of a 2D array would be hard. 

Program predicts value solely off of lot_sqft; for this to be an accurate model it would need to take more things into account like bedrooms, bathrooms, etc.



