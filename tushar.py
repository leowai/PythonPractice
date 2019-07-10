__author__ = 'Administrator'
import tushare
import tushare as ts
print (tushare.__version__)


data=ts.get_hist_data('601857',start='2015-05-01',end='2019-07-01')
print(data)