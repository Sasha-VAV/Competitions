from lightautoml.automl.presets.tabular_presets import TabularAutoML
from lightautoml.tasks import Task
import pandas as pd


train_df = pd.read_csv('data_task11/Предсказание победителя в раунде матча по Counter-Strike/train.csv')
test_df = pd.read_csv('data_task11/Предсказание победителя в раунде матча по Counter-Strike/test.csv')
automl = TabularAutoML(task = Task(name = 'binary', metric = 'auc'))
oof_preds = automl.fit_predict(train_df, roles = {'target': 'winnerSide'}).data
test_preds = automl.predict(test_df).data

exit(0)
