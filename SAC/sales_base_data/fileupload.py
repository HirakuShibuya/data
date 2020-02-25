# -*- coding: utf-8 -*-


class fupload:
  
  
  #def __init__(self,sname='all'):
        #self.sname = sname

############################################
#売上情報をアップロード
############################################
   
  def uploadFile(sname):

    import pandas as pd
    import datetime
    import pandas.tseries.offsets as offsets
    from dateutil.relativedelta import relativedelta
    from google.colab import files
    import imageio
    
    inputs = []
    images = []

    uploaded = files.upload()

    df=pd.read_excel(list(uploaded)[0],sheet_name=sname)
    
    return df
  

  
  


  def preprocessing(df):
  
    dfs=[]
  
    #内部取引を消去
    df_SEC=df[~df["得意先コード"].str.startswith("99")]
  
    #OE売上()
    df_OE=df_SEC[df_SEC["デパートメント（小）"].str.contains('(?:WEU|AFRICA|CEE|CIS|DACH|UK&IE|ME|Alliance)')]


    #OS売上
    df_OS=df_SEC[df_SEC["デパートメント（小）"].str.startswith("OS")]


    #OTBV売上
    df_OTBV=df_SEC[df_SEC["デパートメント（中）"].str.startswith("OTBV")]
    df_OTBV=df_OTBV[df_OTBV["デパートメント（小）"].str.startswith("Security")]


    #OI売上
    df_OI=df_SEC[df_SEC["デパートメント（中）"].str.startswith("OI")]
    df_OI=df_OI[df_OI["デパートメント（小）"].str.contains('(?:SEC|Export)')]

    #ソリューション売上
    df_SOL=df[df["デパートメント（特大）"].str.startswith("ｿﾘｭｰｼｮﾝ事業部")] #内部取引含めている

    #APAC売上
    df_APAC=df_SEC[df_SEC["デパートメント（特大）"].str.startswith("APAC営業本部")]
    df_APAC=df_APAC[df_APAC["デパートメント（中）"].str.startswith("APAC(SEC)営業(按分含)")]

    #OTH売上
    df_OTH=df_SEC[df_SEC["デパートメント（中）"].str.startswith("OTH")]
    df_OTH=df_OTH[df_OTH["デパートメント（小）"].str.startswith("SEC")]

    #製品G
    df_SEC_div=df_SEC[df_SEC['ディビジョン（特大）']=='SEC']
    df_SEC_div=df_SEC_div[df_SEC_div['会計年度']>2017]
    df_SEC_div=df_SEC_div[df_SEC_div['ディビジョン（小）'].str.match('(?:VXI|VXS|BX|WX|RLS|CMOD|QXI|SL|AX|IVPC|RXC|CDX|SIP)')]

    productG=df_SEC_div.pivot_table(values=['数量'],
                               index=['ディビジョン（中）','ディビジョン（小）'],columns=['会計年度','会計期間'],
                               aggfunc='sum', fill_value=0)#,margins=True,margins_name='TOTAL')

  
  
    return df_SEC, df_OE, df_OS, df_OTBV, df_OI, df_SOL, df_APAC, df_OTH, df_SEC


