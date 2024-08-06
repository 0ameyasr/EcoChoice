import pandas,numpy
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

class supervised_dataset:
    def __init__(self,path="",test_size=0.20,split_random_state=None,drop=[],target=""):
        self.path = path
        self.test_size = test_size
        self.split_random_state = split_random_state
        self.dataset = pandas.read_csv(path)
        self.X = numpy.array(self.dataset.drop(drop,axis=1))
        self.y = numpy.array(self.dataset[target])
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(
            self.X,
            self.y,
            test_size=self.test_size,
            random_state=self.split_random_state
        )

class supervised_model:
    def __init__(self,estimator=LogisticRegression(),param_grid={}):
        self.estimator = estimator
        self.model_params = param_grid
        self.best_estimator = None
    
    def find_best_estimator(self,data=supervised_dataset|pandas.DataFrame,verbose=False,cv=5,pandas=False,target="",test_size=0.20):
        if not pandas:
            grid_search = GridSearchCV(self.estimator,param_grid=self.model_params,cv=cv)
            grid_search.fit(data.X_train,data.y_train)
            if verbose:
                print(f"Best Estimator: {grid_search.best_estimator_}")
            self.best_estimator = grid_search.best_estimator_
            return self.best_estimator
        else:
            y = numpy.array(data[target])
            X = numpy.array(data.drop(target,axis=1))
            X_train, _ , y_train, _ = train_test_split(X,y,test_size=test_size)
            grid_search = GridSearchCV(self.estimator,param_grid=self.model_params,cv=cv)
            grid_search.fit(X_train,y_train)
            if verbose:
                print(f"Best Estimator: {grid_search.best_estimator_}")
            self.best_estimator = grid_search.best_estimator_
            return self.best_estimator
    
    def fit_best_estimator(self,data):
        if not self.best_estimator:
            print(f"""ERROR: fit_best_estimator > The best estimator has not been initialized. Use .find_best_estimator() before fitting this method.""")
            return False
        else:
            try:
                self.data = data
                self.best_estimator.fit(data.X_train,data.y_train)
                return True
            except Exception as error:
                print(f"ERROR: fit_best_estimator > {error}")
                return False
        
    def predict(self,features):
        return self.best_estimator.predict(features)

    def eval_best_estimator(self):
        self.testing_accuracy = accuracy_score(self.predict(self.data.X_test),self.data.y_test)
        self.training_accuracy = accuracy_score(self.predict(self.data.X_train),self.data.y_train)
        print(f"\nBest Estimator: {self.best_estimator}")
        print(f"Training Accuracy Score: {self.training_accuracy}")
        print(f"Testing Accuracy Score: {self.testing_accuracy}")
        print(f"Absolute Model Bias: {numpy.round(abs(self.training_accuracy - self.testing_accuracy),3)}\n")

class semi_supervised_dataset:
    def __init__(self, path="Model/data/ec_food_dataset.csv", n_head=20, drop=[], target=""):
        self.path = path
        self.dataset = pandas.read_csv(path).drop(drop, axis=1)

        self.labeled = self.dataset.head(n_head)
        self.unlabeled = self.dataset.iloc[n_head:]
        self.X = numpy.array(pandas.concat([
            self.labeled.drop(columns=[target]),
            self.unlabeled.drop(columns=[target])
        ]))
        self.y = numpy.array(pandas.concat([
            self.labeled[target],
            self.unlabeled[target]
        ]))


class semi_supervised_model:
    def __init__(self, estimator=SelfTrainingClassifier(base_estimator=LogisticRegression()), param_grid={}):
        self.estimator = estimator
        self.model_params = param_grid
        self.best_estimator = None
    
    def fit_estimator(self, data: semi_supervised_dataset):
        self.data = data
        self.estimator.fit(data.X, data.y)
                
    def predict(self, features):
        return self.estimator.predict(features)

    def get_estimator(self):
        return self.estimator

class interface:
    def __init__(self,estimator=None):
        self.estimator = estimator

    def get_prediction(self,features=[]):
        return self.estimator.predict(features)[0]

    def ecf_classifier(self,verbose=True):
        data = semi_supervised_dataset(
            path = "Model/data/ec_food_dataset.csv",
            n_head= 25,
            drop=["PRICE","AVG_RATING","NUM_RATING"],
            target = "ECO"
        )
        
        dataset = pandas.read_csv("Model/data/ec_food_supervised.csv")
        
        classifier_params = {
            "C":[0.1,0.01,0.001],
            "kernel":['linear'],
            "random_state":[0],
            "probability":[True],
        }
        classifier = supervised_model(estimator=SVC(),param_grid=classifier_params)
        best_estimator = classifier.find_best_estimator(pandas=True,data=dataset,verbose=verbose,target="ECO")

        classifier = semi_supervised_model(SelfTrainingClassifier(base_estimator=best_estimator))
        classifier.fit_estimator(data)

        X_test = numpy.array(pandas.read_csv("Model/data/ec_test.csv").drop("ECO",axis=1))
        y_test = numpy.array(pandas.read_csv("Model/data/ec_test.csv")["ECO"])
        X_train = numpy.array(data.labeled.drop(["ECO"],axis=1))
        y_train = numpy.array(data.labeled["ECO"])
        y_pred = classifier.predict(X_test)

        if verbose:
            print(f"Accuracy Score: {accuracy_score(y_test,y_pred)}")
            print(f"Accuracy Score (Training): {accuracy_score(y_train,classifier.predict(X_train))}")
        return best_estimator

if __name__ == "__main__":
    io = interface()
    classifier = io.ecf_classifier(verbose=False)
    predictor = interface(classifier)