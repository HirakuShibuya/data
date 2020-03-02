class createHtml():
  
  import os
  
  def __init__(self):
    print("")
  
  def create_html2(self, dframe, dir):
    
    files=os.listdir('img/'+dir)
    list=[]
    for i, d in enumerate(files):
      src='<img src="graph/img/'+dir+'/'+d+'" alt="sample" width="100%" height="100%" /><br>'
      list.append(src)

    src2=""
    for i,d in enumerate(list):
      src2=src2+d

    return src2
  
  
  def cHtml(self, dframe, dir):
    html='''
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=shift_jis" />
  <!--
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  原則として、許可なしの再配布は禁止させていただきます。
  また、無料でお使いの方は、【ＰＲ枠】のリンクは全て削除禁止です。
  加工後の削除も禁止させていただいております。
  絶対に削除しないでお使いください。
  ご不明な点は、http://www.s-hoshino.com/info.html、または、
  http://www.megapx.com/info.htmlのフォームよりお問い合わせください。
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  -->
  <title>Sales Data</title>
  <meta name="Keywords" content="キーワード1,キーワード2,キーワード3" />
  <meta name="Description" content="SimpleTmpl011。ここには、サイトやページの紹介文等を入れてください。" />
  <link rel="stylesheet" href="style.css" type="text/css" />
  </head>
  <body>
  <div id="header">
  <h1><a href="#">Sales Data</a></h1>
  </div>
  <div id="nav">
    <ul>
      <li><a href="index.html">OE</a></li>
      <li><a href="OSF.html">OSF</a></li>
      <li><a href="OTBV.html">OTBV</a></li>
      <li><a href="OI.html">OI</a></li>
      <li><a href="ProductG.html">Product Group</a></li>
    </ul>
  </div>
  <div id="base">
    <div id="wrap">
      <div id="contents">
        <div id="c_pad">
          <h2>OE</h2>



  '''

    src=self.create_html2(dframe,dir)

    html=html+src

    html=html+'''


        </div>
      </div>
      <!--contents end-->
      <div id="side">
        <div class="side_box">
          <h3>By Subsidiaries</h3>
          <ul>
            <li><a href="index.html">OE</a></li>
            <li><a href="OSF.html">OSF</a></li>
            <li><a href="OTBV.html">OTBV</a></li>
            <li><a href="OI.html">OI</a></li>
          </ul>
        </div>
      <div class="side_box">
          <h3>By Product</h3>
          <ul>
            <li><a href="ProductG.html">Product Group</a></li>
      <li><a href="product.html">Product</a></li>
      <li><a href="price_qty.html">Price Qty</a></li>
          </ul>
        </div>


      </div>
    </div>
    <div id="f_menu">

  <!--　削除禁止【ＰＲ枠】ここから　-->
  <!--prno.130321ver2.01set016-->
  Design by <a href="http://www.megapx.com/" target="_blank">Megapx</a>　
  Template by <a href="http://www.s-hoshino.com/" target="_blank">s-hoshino.com</a>
  <!--　/削除禁止【ＰＲ枠】ここまで　-->
      </div>
    </div>
    <address>
    Copyright (C) SimpleTmpl011 All Rights Reserved.
    </address>
  </div>
  </body>
  </html>
  '''


    return(html)
