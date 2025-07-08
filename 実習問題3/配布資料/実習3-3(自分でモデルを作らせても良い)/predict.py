# モデルがきちんと動作することのチェック用プログラムです
# 予測まで動作できない場合
# モデルを作成したときと予測させているときのscikit-learnのバージョンを揃えてください
import pickle

# モデルの読み込み
with open('KvsT.pkl', 'rb') as f:
    model = pickle.load(f)

# 予測データの作成
predict_data = [[180, 75, 30]]

# 予測
print(model.predict(predict_data))