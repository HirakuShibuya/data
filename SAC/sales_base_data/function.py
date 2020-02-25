

class func:


  #######################################################
  #関数
  #######################################################
  
  import datetime

  d_today = datetime.date.today()


  ########################################
  #pivotをTOP5とそれ以下をその他とするデータ作成
  ########################################

  def create_top5(ddata, item,num):
    #ddata:元となるpivot_table
    #item:データ（value）名

    ddata_top=ddata[:num]
    ddata_other=ddata[num:].sum()[item]
    ddata_other=pd.DataFrame(ddata_other).transpose()
    ddata_index=ddata_top.index.values.tolist()
    ddata_index.append('OTHERS')
    ddata_total=pd.concat([ddata_top[item],ddata_other], ignore_index=True)
    ddata_total['zone']=ddata_index
    ddata_total=ddata_total.set_index('zone')
    return ddata_total

  ########################################
  #pivot作成
  ########################################
  def create_pivot(dframe, value, idx, clmn, YTD=0, num=5):
    #dframe:元となるdataframe
    #value:pivot_tableのデータ名
    #idx:pivot_tableのインデックス（行）名
    #clmn:pivot_tableのカラム（列）名
    #YTD:YTD=0（通年）、YTD=1（YTD）

    d_today = datetime.date.today()

    if(YTD==1):
      if(d_today.month>1):
        dframe=dframe[dframe['会計期間'].astype(int)<d_today.month]

    dframe=dframe.pivot_table(values=[value],
                                index=[idx],columns=[clmn],
                                aggfunc='sum', fill_value=0)#,margins=True,margins_name='TOTAL')

    dframe = dframe.reindex(dframe[value].sort_values(by=d_today.year-1, ascending=False).index)
    dframe[value]=dframe[value].astype(int)
    dframe=create_top5(dframe,value,num)
    return dframe


  ########################################
  #積み上げ棒グラフ作成
  ########################################
  def bar_graph(ddata, xlbl,ylbl,title):
    fig, ax = plt.subplots(figsize=(10, 8))

    for i in range(len(ddata)):
      ax.bar(ddata.columns.values, ddata.iloc[i].values, bottom=ddata.iloc[:i].sum())
    
    ax.set(xlabel=xlbl, ylabel=ylbl, title=title)
    ax.set_xticks(ddata.columns.values.astype(int))
    ax.legend(ddata.index,loc='upper right')
    plt.savefig('img/barGraph/'+title+'.png')
    plt.show()


  ########################################
  #台数および移動平均プロット(製品群)
  ########################################

  def plot_qty(dframe,new_dir):

    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    #%matplotlib inline
    import os

    os.makedirs("img", exist_ok=True)
    os.makedirs("img/"+new_dir, exist_ok=True)

    dframe=dframe.droplevel(level=0)


    forecast=[]
    for i in range(len(dframe.index)):
      try:
        result=[]
        result.append(dframe.index[i])

        data=pd.DataFrame(dframe.loc[dframe.index[i]].values)

        for j in range(6):
            data=data.append(pd.DataFrame(pd.DataFrame(data).rolling(6).mean().values[-1]))

        for j in range(6):
            result.append(data.values[len(data.values)-6+j][0])

        forecast.append(result)
      
        for j in range(len(data.values)):
            data.values[j][0]=0

        print(dframe.index[i])


        plt.plot(dframe.loc[dframe.index[i]].values, label='result')
        plt.plot(pd.DataFrame(dframe.loc[dframe.index[i]].values).rolling(6).mean(), label='rolling mean')
        plt.ylabel("Unit")
        plt.title(dframe.index[i])
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
        plt.text(0,dframe.loc[dframe.index[i]].values.max(),'rolling mean : '+str(int((pd.DataFrame(dframe.loc[dframe.index[i]].values).rolling(6).mean().values[-1]))))
        plt.savefig('img/'+new_dir+'/'+dframe.index[i]+'.png')

        plt.show()

      except:
        print("")


  ########################################
  #台数および移動平均プロット(製品)
  ########################################

  def plot_qty2(dframe,new_dir):

    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    #%matplotlib inline
    import os

    os.makedirs("img", exist_ok=True)
    os.makedirs("img/"+new_dir, exist_ok=True)

    dframe=dframe.droplevel(level=0)

    forecast=[]
    for i in range(len(dframe.index)):
      try:
        result=[]
        result.append(dframe.index[i])

        data=pd.DataFrame(dframe.loc[dframe.index[i]].values)

        for j in range(6):
            data=data.append(pd.DataFrame(pd.DataFrame(data).rolling(6).mean().values[-1]))

        for j in range(6):
            result.append(data.values[len(data.values)-6+j][0])

        forecast.append(result)
      
        for j in range(len(data.values)):
            data.values[j][0]=0

        #print(str(int(pd.DataFrame(dframe.loc[dframe.index[i][0]].values).rolling(6).mean().values[-1])))

        plt.plot(dframe.loc[dframe.index[i]].values, label='result')
        plt.plot(pd.DataFrame(dframe.loc[dframe.index[i]].values).rolling(6).mean(), label='rolling mean')
        plt.ylabel("Unit")
        plt.title(dframe.index[i][0]+" : "+dframe.index[i][1])
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
        #plt.text(0,dframe.loc[dframe.index[i][0]].values.max(),'rolling mean : '+str(int(pd.DataFrame(dframe.loc[dframe.index[i][0]].values).rolling(6).mean().values[-1]))
        plt.savefig('img/'+new_dir+'/'+dframe.index[i][0]+"_"+dframe.index[i][1]+'.png')

        plt.show()

      except:
        print("")


  ########################################
  #HTML表示用
  ########################################

  def create_html(dframe,dir):
    html_s=[]
    for i in range(0,len(dframe)):
      dsc='<img src="graph/img/'+dir+'/'+dframe.index[i][1]+"_"+dframe.index[i][2]+'.png" alt="sample" width="100%" height="100%" /><br>'
      html_s.append(dsc)

    for j in range(0,len(html_s)):
      print(html_s[j])
