# How to run

Please create a new conda environment

`conda create -n topics python=3.6 anaconda`

Use `pip freeze` to check that `sklearn` and `numpy` are installed.

`python topics.py` will run the main script.

With `docker` please run `make build` to build the container.

Then `docker run -it IMAGE_ID bash` to launch bash in the container, and then `python topics/topics.py` to run the script.

# Solution Description

## Business problem

We have customers who are interested in domain-specific analyses of documents in these fields:

- medicine
- space
- cryptography
- electronics

We intend to tag our document stream (of news articles, blogs, social media postings) with these topics so that we can identify subsets of articles for more intensive domain-specific processing.

### Data

We use the 20 newsgroups dataset. The 20 newsgroups dataset comprises around 18000 newsgroups posts on 20 topics split in two subsets: one for training (or development) and the other one for testing (or for performance evaluation). The split between the train and test set is based upon a messages posted before and after a specific date. (From scikit-learn user guide). We remove metadata such as header and footers, and remove messages which quote other posts.

We encode the targets of sci.med, sci.space, sci.crypt, sci.electronics with their target from the 20 newsgroups datset. All other targets are encoded as -1.

## Evaluating the classifiers

We preprocess the raw text documents by filtering stopwords and tokenising (using a CountVectoriser) and then creating TF-IDF features for our classifiers.

We fit Logistic regression and Support Vector Machine classifiers. 

We evaluate using the weighted F1-score. This is the F1 score for each class, weighted by the number of samples from that class. A higher F1 score indicates a better classifier.

## Otimizing your classifier

Due to illness we have not done this part.

## Ensuring the research is reproducible and fit for sharing

Ideally this would be wrapped in a Docker container, but due to illness this hasn't been completed.

## Scaling and generalizing

N/A due to illness.
