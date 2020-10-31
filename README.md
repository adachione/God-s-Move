# God's Move(神の一手)
Derive the God's move of shogi
As of 20201031:There is no way to derive God's move, only the generation of commentary
shogiの神の一手を導き出す
20201031時点:神の一手を導き出す方法はできておらず、解説文の生成のみ

# Text_generate
Create a sentence like a commentary by a professional shogi player.
Please collect the learning texts of the commentary by yourself.
プロ棋士の解説のような文章を作成します。
解説文の学習テキストはご自身で収集してください。

## Usage
1. Create corpus
2. Create utils-> Sentece Piece (morphological analyzer)
3. Train with model-> TextGeneration to create the trained weights.
4. Generate text in main.py.

* Please execute with Google Colab Pro.

1. corpusを作成
2. utils->SentecePiece(形態素解析器)を作成
3. model->TextGenerationで学習させ、学習した重みが作成されます。
4. main.pyでテキストを生成します。

※GoogleColabProで実行ください。

