# -*- coding: utf-8 -*-


class fileupload:
  def uploadFile(self,name='all'):
############################################
#売上情報をアップロード
############################################

    import pandas as pd
    import datetime
    import pandas.tseries.offsets as offsets
    from dateutil.relativedelta import relativedelta
    from google.colab import files
    import imageio
    
    inputs = []
    images = []

    uploaded = files.upload()

    df=pd.read_excel(list(uploaded)[0],sheet_name=name)
