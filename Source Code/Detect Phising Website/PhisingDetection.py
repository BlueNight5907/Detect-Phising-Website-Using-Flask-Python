#importing libraries
import joblib
import FeatureExtraction
import pandas as pd
from sklearn.metrics import accuracy_score


class MODE:
    def __init__(self):
        self.RANDOM_FOREST = "rf_final"
        self.LOGISTIC_REGRESSION = "logisticR_final"
        self.SVM = "svm_final"

#-----------------------------------------

def getResult(url, mode):
    print(mode)
    try:
        classifier = joblib.load('./final_models/'+mode+".pkl")
        #checking and predicting
        checkprediction = FeatureExtraction.main(url)
        prediction = classifier.predict(checkprediction)
        if prediction == 1:
            return "Phising Website"
        else:
            return "Legimal Website"
    except Exception as e:
        print(e)
        return "An error occurred during execution!!!"

def getMultiResult(filepath, mode):
    print(mode)
    try:
        classifier = joblib.load('./final_models/'+mode+".pkl")
        dataset = pd.read_csv(filepath)
        list_domain = list(dataset['domain'])

        label_in_dataset = "label" in dataset
        if(label_in_dataset):
            y_true = list(dataset['label'])
        else:
            y_true = []
        y_predict = []
        result = []
        for i in range(len(list_domain)):
            url = list_domain[i]
            checkprediction = FeatureExtraction.main(url)
            prediction = classifier.predict(checkprediction)
            if prediction == 1:
                mess = "Phising Website"
            else:
                mess = "Legimal Website"
            ob = {"domain":url, "predict":mess}

            if len(y_true) > 0:
                y_predict.append(prediction)
                if y_true[i] == 1:
                    mess = "Phising Website"
                else:
                    mess = "Legimal Website"
                ob['right value'] = mess

            result.append(ob)
        if len(y_true) > 0:
            score = accuracy_score(y_true, y_predict)
            return {"accuracy score":score, "result":result}
        return {"result":result}
    except Exception as e:
        print(e)
        return "An error occurred during execution!!!"
    

        
Mode = MODE()