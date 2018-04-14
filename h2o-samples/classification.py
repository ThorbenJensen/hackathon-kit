
import pandas as pd
import h2o
from h2o.estimators import H2OXGBoostEstimator
from h2o.automl import H2OAutoML
from matplotlib import pyplot

# start h2o
h2o.init()  # h2o.shutdown()

# load data
df = pd.read_csv('h2o-samples/data/iris.csv')
hf = h2o.H2OFrame(df)

# partition data
train, test = hf.split_frame(ratios=[.8])

# run automl
aml = H2OAutoML(max_runtime_secs=30)
aml.train(y='class',
          training_frame=train,
          validation_frame=test)

# examine best models
aml.leaderboard
aml.leader
