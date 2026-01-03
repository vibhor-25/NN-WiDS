Vidit Nagpurkar

25B1270



Implementation, specifically in week-2 centers on a custom implementation of Linear Regression.

Rather than using high level libraries, optimisation was done using a from-scratch implementation of Vectorised Gradient Descent



Data in the form of text like Furnishing Status and Floor Level were converted into numerical scales to be able to feed into Linear Regression Model

Target Encoding was implemented for encoding the "city" variable in a rent-calculation model to be able to effectively capture geographic trends

Z-score normalisation was implemented to ensure fast convergence. All features were standardised to a mean of 0 and standard deviation of 1



For the non-linear dataset, Polynomial Expansion was implemented to be able to use the linear regression model for fitting the given quadratic curve

Models were evaluated using metrics like Root-Mean Square Error and Mean-Absolute Error.





Mastered the use of Google Colab and .ipynb files.

Learnt to use widely used Python Libraries like:

Numpy: For high performace n-dimensional array processing.

This was critical to the actual project to allow simultaneous calculation of gradients across an entire data sets instead of using slow Python Loops



Pandas: Learnt to handle csv files, including managing missing data and performing complex data encoding implementations



Matplotlib:

Used to plot available data points for visualising correlations between environment variables and crop yields



Scikit-Learn: Transitioned from manual implementations to industry-standard libraries. Studied the standard implementation for linear regression through gradient descent



Studied Linear and polynomial regression and understood the relationship between independent features and continuous target variables



Understood Optimization through gradient descent to understand how models learn by minimising cost functions



Challenges Overcome:



A. Vanishing and exploding gradients:

A challenge in the "House Rent" model was the scale of the data. Initially when I ran my original model, it returned NaN or infinity because the "Size" feature caused my gradient updates

to be very large. To counter this, I implemented Z-score standardisation to scale all features to a mean of 0 and standard deviation of 1



B. Heuristic Data Transformation:

The provided "Floor" data text was quite unstructred. I engineered a custom parsing function that extracted floor number and total floors data from the irregular strings. Categorical

labels like "Ground" and "Basement" were found and converted into numerical values. This also allowed me to generate a "floor ratio" feature for the linear regression model, allowing 

for higher accuracry



C.Learning Rate problems:

Though thre initial implementation was simple, the learning rate proved to be a difficult value to tune for a custom-made model. The value of 10^-2 that worked for the fruit harvest

model did not work at all for the rent model and a much finer learning rate was required. Making the learning rate too fine led to the model being run for several minutes without improved

results. Finding the exact value for the learning rate that worked was quite a slow process for larger data sets



Solving these issues provided to me a deeper insight into why preprocessing is much more important than the model itself.





Do not change any of my language or text, simply format it into a more systematic way (Just better indexing and titles should be slightly larger)
