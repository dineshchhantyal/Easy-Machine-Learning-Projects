### Marks Predictions Model based on student's study hours

- This is a simple linear regression model to predict the marks of students based on their study hours.
- A simple web application is also created to demonstrate the model. [https://dineshchhantyal.pythonanywhere.com/](https://dineshchhantyal.pythonanywhere.com/)

### Dataset

- The dataset is available in the file `models/marks/scores.csv` and it contains 2 columns: `Hours` and `Scores`.

### Model

- The code for the model is available in the file `models/marks/marks.py`.
- The model is trained using the `LinearRegression` class from the `sklearn.linear_model` module.

### Usage

- The model can be used by calling the `predict` function and passing the number of study hours as an argument.

```python
from models.marks.marks import marks_prediction
```

### Deployment

- The model is deployed as a web application using the Flask framework.
- The code for the web application is available in the file `app.py`.
- The web application is deployed on Heroku and can be accessed using the following link: [Marks Prediction App](https://dineshchhantyal.pythonanywhere.com/)
