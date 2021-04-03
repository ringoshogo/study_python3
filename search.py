import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, file_path):

    # 検索対象取得
    df=pd.read_csv("./source.csv")
    source=list(df["name"])

    # 検索
    if word in source:
        # 課題4 ログ表示領域に結果を追記
        eel.view_log_js(f"『{word}』はあります。")
    else:
        # 課題4 ログ表示領域に結果を追記
        eel.view_log_js(f"『{word}』はありません。新たに追加します。")
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(file_path,encoding="utf_8-sig")
