# django-mysite
## 制作背景

　コロナ禍から洋服をECサイトで買う機会が増え、いつも通りMサイズを買ったのにサイズミスで買ったはいいものの着れず後悔することが多々ありました。  

この一番の要因は、ブランドやメーカーによってS,M,Lサイズの規格が違うからです。  

なので、S,M,Lのような一般サイズではなく、着丈や胸囲、袖丈のような絶対的なサイズで選べばいいんだと気づきました。  

しかし自分に合う丈や長さがわからなかったのでサイズ管理アプリを作りました。  

## 使用言語 

Python3, Django, SQLLite

## できること
  ### サイズ登録  
  
・服のカテゴリー（アウター、長袖トップス、半袖トップス、スウェット）毎にサイズ登録ができます  
  
・サイズは着丈、胸囲、肩幅、袖丈を登録することができます  
  
・登録したサイズの詳細を確認、編集、削除できます  
  
・サイズの平均をカテゴリー別で確認することができます  
  
・登録した服の着心地を｛ゆるめ、きつめ、ぴったり、ゆるすぎ、きつすぎ｝から登録することができます  
  
### User関連
  
・サインアップしないとトップページに入れません  
  
・ログインのためのパスワードやユーザー名を忘れても再設定できます  

## 工夫した点
  
特に工夫したのはカテゴリー別でサイズ平均を表示させる部分でした。  
  
平均表示では独自関数を作りました。Modelsからデータを取得し、それぞれの服のカテゴリー別で計算し、For文でList変数に格納させる関数を実装するのが非常に難しかったです。  
  
## 使い方
  
1⃣「サイズ入力」から、自分の持っている服や買ってちょうどよかった服の寸法を登録  
  
2⃣「サイズ一覧」から登録した服の一覧を見ることができます  
   詳細ボタンからその服のサイズ詳細、編集ボタンからサイズ編集、削除ボタンから登録サイズを削除できます
  
3⃣「平均表示」から登録したサイズの平均を確認することができます  
  
4⃣「ログアウト」でログイン画面に戻ります  
  
5⃣「パスワード変更」からパスワードの変更ができます  
  
6⃣「パスワードを忘れた場合」からサインアップ時に登録したメールアドレス経由でパスワードの再設定ができます  
  
## 改善点
  
### UXの向上としてInput、Output操作をより良くしていきたいです。  
Input  
「サイズ入力」は非常に面倒くさい工程なためPyOCR、Tesseractを用いた画像からの文字認識及び文字入力を実装し、  
サイズ表のスクリーンショット等から該当するサイズを自動入力できるようにしたい  
      
Output  
「平均表示」では着心地ごとにフィルターをかけて表示できるようにしたい。  
  
  　具体的には、ぴったりとフォーマルに着たいレギュラーシャツのサイズ確認する場合や、大きめなストリートスタイルで着たいTシャツのサイズのように、場合分けして確認できるようにしたい。  
  
### テストアカウント
ユーザー名：test1   
Pass：1234tete
