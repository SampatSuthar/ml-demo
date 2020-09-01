import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import pickle




#import xgboost
#from xgboost import XGBClassifier # import XGBoost Classifier

#from sklearn.linear_model import LogisticRegression # Import Logistic Regression
#from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.ensemble import RandomForestClassifier # importRandom forest Classifier 
from sklearn import model_selection
from sklearn.model_selection import train_test_split  # import 'train_test_split'
#from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn import preprocessing
#Import scikit-learn metrics module for accuracy calculation

# sklearn modules for performance metrics
#from sklearn.metrics import confusion_matrix, classification_report, precision_recall_curve
#from sklearn.metrics import auc, roc_auc_score, roc_curve, recall_score, log_loss
#from sklearn.metrics import f1_score, accuracy_score, roc_auc_score, make_scorer
#from sklearn.metrics import average_precision_score
#from sklearn.metrics import explained_variance_score
#from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
#from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import cross_val_score


# Import and suppress warnings
import warnings
warnings.filterwarnings('ignore')

# loading data
initiative = pd.read_csv('C:/Users/Sampat Suthar/Desktop/Excel files/new_test.csv')

## Drop insignificant variables

initiative = initiative.drop(['ID', 'set_id','goal','category','init_id','initiative','stratgoals','groups','duedate','assignoto','manager','updatedate'], axis=1)

# converting target variable in numeric value

le = preprocessing.LabelEncoder()
new_initiative = initiative ##  
new_initiative = new_initiative.apply(le.fit_transform)

# spilit data into x and y

x = new_initiative.drop('completion on time',axis =1)
y = new_initiative['completion on time']

## running random forest 

rf = RandomForestClassifier(oob_score = True, random_state = 0)
random_forest = rf.fit(x,y)

# Prediction
prediction = random_forest.predict(x)

# saving model to disk

pickle.dump(random_forest, open('model.pkl', 'wb'))

# loading model to compare results

model = pickle.load(open('model.pkl', 'rb'))