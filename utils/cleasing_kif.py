import re
import string
import os
import glob
import pickle
import codecs
import mojimoji

def _clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    """
    テキストを小文字にし、角括弧内のテキストを削除し、リンクを削除し、句読点を削除します 数字を含む単語を削除します。
    """
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = mojimoji.han_to_zen(text)
    
    text = re.sub('(.*本局の感想戦取材はありません。.*)', '', text)
    text = re.sub('(\（棋譜・.*)', '', text)
    text = re.sub('(\［棋譜表示.*)', '', text)
    text = re.sub('(棋譜表示の＊はコメント付きの指し手)', '', text)
    text = re.sub('(【第\d{2}期.*】)', '', text)
    text = re.sub('(◆.*◆)', '', text)
    text = re.sub('(\d{4}年.*)', '', text)
    text = re.sub('(【.*】)', '', text)
    text = re.sub('(.*通算成績は.*)', '', text)
    text = re.sub('(.*昨年度成績は.*)', '', text)
    text = re.sub('(.*本年度成績は.*)', '', text)
    text = re.sub('(.*順位戦成績は.*)', '', text)
    text = re.sub('(.*今年度成績は.*)', '', text)
    text = re.sub('(.*タイトル戦登場は.*)', '', text)
    text = re.sub('(.*終局時刻は.*)', '', text)
    text = re.sub('(.*日時：.*)', '', text)
    text = re.sub('(.*場所：.*)', '', text)
    text = re.sub('(.*解説者：.*)', '', text)
    text = re.sub('(.*入場料：.*)', '', text)
    text = re.sub('(.*料金：.*)', '', text)
    text = re.sub('(.*\（.\）\解説：.*)', '', text)
    text = re.sub('(.*新聞.*)', '', text)
    text = re.sub('(.?名人戦、順位戦は朝日新聞社.*)', '', text)
    text = re.sub('(.*■AbemaTV■.*)', '', text)
    text = re.sub('(.*■ニコニコ生放送■.*)', '', text)
    text = re.sub('(.*※局後の感想※.*)', '', text)
    text = re.sub('(\（\d*）)', '', text)
    text = re.sub('(\(\d*\))', '', text)
    text = re.sub('\u3000','', text)
    text = re.sub('(.*\d勝\d敗.*)', '', text)
    text = re.sub('(対局再開。.食休憩.*)', '', text)
    text = re.sub('(.*昼食休憩に入.*)', '', text)
    text = re.sub('(.*＝各種リンク.*)', '', text)
    text = re.sub('(.*対局立会人は.*)', '', text)
    text = re.sub('(.*\w級\d組.*)', '', text)
    text = re.sub('(.*チェスクロック使用.*)', '', text)
    text = re.sub('(.*将棋会館.*)', '', text)
    text = re.sub('(.*降級点.*)', '', text)
    text = re.sub('(.*解説会.*)', '', text)

    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('＊', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)   # 特殊記号除去
    text = re.sub('\n', '', text)   #改行除去
    text = re.sub('\'','', text)
    
    return text
    
def dumpPickle(fileName, obj):
    with open(fileName, mode="wb") as f:
        pickle.dump(obj, f)

def main():
    kif_path = os.getcwd() + "/kif"
    kif_list = sorted(glob.glob(kif_path + '/*' + ".txt"))
    corpus = []
    for i, kif in enumerate(kif_list):
        print("---process{}-------".format(str(i)))
        with open(kif, "r", encoding="cp932") as f:
            lines = f.readlines()
            
            for line in lines:
                if line[0] == "*" and line != "*\n":
                    line = _clean_text(line)
                    
                    if line != "" and line != " " and len(line) >=5:
                        corpus.append(line)
                        
    dumpPickle(os.getcwd()+os.sep+"corpus.pickle", corpus)

if __name__ == "__main__":
    main()