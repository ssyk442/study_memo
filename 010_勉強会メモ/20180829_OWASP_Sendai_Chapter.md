## OWASP Sendai Chapter 20180829 18:30-

### はじめてのOWASP Top10 2017： A3 機微な情報の露出
スピーカー：セキュリティ初心者やまだくん & 千葉 翔也（東北工業大学）  
OWASP Risk Rating Methodology  
Owasp Top10 スコアの出し方  
Risk = Likelihood(発生可能性) * Impact(影響度)  
原文は英語 　

A3 機微
シナリオ１  
ex.クレジットカードの話  
データベースの自動暗号化機能 　
ストレージ盗難には対応できるが、
平文はハッシュ化して保存

シナリオ２  
https通信をhttp通信にダウングレード  
MITM attack(中間者攻撃)  
Sslstrip attack  
loginページがhttp  
攻撃者にログインIDとパスワード筒抜け  
対策  
- hstsの利用  
- ウェブサイト全体をhttps化  
- 無線LAN

シナリオ３
ハッシュ化したパスワードについて  
平文を読まれないようにする  
復元方法例：リストに平文と対応するハッシュ値を入れておいて総当たりで検索  
レインボーテーブル  
RainbowCrack  
  https://project-rainbowcrack.com/index.htm  
対策  
- 平文の前にソルトをくっつける  
- ストレッチング(複数回ハッシュ化する)

パスワード管理に適していない：MD5,SHA-1,SHA-2  
パスワード管理に適している：bcrypt,argon2  


### WEB開発者が知っておくべきGitハッキング
スピーカー：小笠貴晴（OWASP Sendai Local Chapter Leader）  

#### Gitとは
CVSやSVNの進化系
gitのローカルリポジトリ時を例に 　
.gitを公開しない  

Namech_k  

GitHubにあるコードの特徴から、攻撃しやすい人かどうかわかる  
上がった内容からID判別→そのIDから 　 　

守る側も攻撃側を意識(クリエイティブに)　　


### DEF CONボランティアレポート
スピーカー：小笠貴晴（OWASP Sendai Local Chapter Leader）  


CSSナイト 　11/17  4,000 6,000  
仙台　xd (adobe)  9/21  
