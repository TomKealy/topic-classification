import numpy as np

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score


def map_target(x):
    """
    Function to re-map the target so that only relevant targets are considered.
    11, 12 ,13, 14 are the encoded targets of medicine, space, cryptography, electronics.
    All other topics are encoded as -1

    TODO: remove hardcoded values.
    :param x: target
    :return: new_target
    """
    if x == 11:
        return x
    elif x == 12:
        return x
    elif x == 13:
        return x
    elif x == 14:
        return x
    else:
        return -1


def main():
    ## Load Data
    
    remove = ('headers', 'footers', 'quotes')

    train = fetch_20newsgroups(subset='train', 
                               remove=remove,
                              )
    
    test = fetch_20newsgroups(subset='test', 
                              remove=remove)
    
    vmap = np.vectorize(map_target)
    
    train.new_target = vmap(train.target)
    test.new_target = vmap(test.target)
    
    ## Train Baseline
    
    logreg_pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', LogisticRegression(multi_class='multinomial', solver='lbfgs')),
    ])

    logreg_pipeline.fit(train.data, train.new_target)
    
    preds = logreg_pipeline.predict(test.data)
    
    print('Baseline score: ', f1_score(test.new_target, preds, average='weighted'))
    
    ## Train classifier
    
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge'))
    ])
    
    pipeline.fit(train.data, train.new_target)
    preds = pipeline.predict(test.data)
    
    ## Save model
    
    print('SGD score: ', f1_score(test.new_target, preds, average='weighted'))

if __name__ == '__main__':
    main()