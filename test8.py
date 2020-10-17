 #効果音を鳴らす
from random import randint
import pyxel

class App:
    def __init__(self):
        # 画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 120, caption="Hello Pysel")
        # editorデータ読み込み(コードと同じフォルダにある)
        pyxel.load("my_resource.pyxres")
        #得点初期化
        self.score = 0
        # 初期配置
        self.player_x = 80
        self.player_y = 60
        # fruit初期配置 x座標 y座標 表示flag on を4個用意
        self.fruit = [(i * 60, randint(0, 104), True) for i in range(4)]

        #BGM再生(MUSIC 0番をloop再生)
        pyxel.playm(0, loop = True)
        # 実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_player()

        # i番目とv要素(各fruitの要素)　enumerate関数で各fruitの値を取得して実行しているっぽ
        for i, v in enumerate(self.fruit):
            # (*v)ってタプルという複数の要素を管理するデータ型の一つらしい
            # つまり、初期化で設定したデータをタプル型にしてupdate_fruit関数に渡しているっぽい
            self.fruit[i] = self.update_fruit(*v)

    def update_player(self):
        # key入力
        # max関数 min関数で画面外に行かないようにしているのか
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
        if pyxel.btn(pyxel.KEY_UP):
            self.player_y = max(self.player_y - 2, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)

    def update_fruit(self, x, y, is_active):
        #衝突判定(playerとfruitの座標の絶対値から衝突しているか判定している)
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False   #表示を消す
            self.score += 10    #scoe加算
            pyxel.play(1,0,loop = False)     #SE再生(CH 1,SOUND 0,単発再生)
            
        # 左に移動
        x -= 2

        # 画面外に出たら
        if x < -40:
            # 画面反対側に強制移動
            x += 240
            # y座標はランダム
            y = randint(0, 104)
            # 表示flag on
            is_active = True

        # 返り値を設定
        return (x, y, is_active)

    def draw(self):
        # 画面クリア 0は黒
        pyxel.cls(0)
        # editorデータ描画
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 0)

        # draw fruits
        for x, y, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 16, 0, 16, 16, 0)

        #score表示用に整形(format関数の文字列操作を利用)
        s = "Score:{:>4}".format(self.score)
        #text表示(x座標、y座標、文字列、color)
        pyxel.text(5, 4, s, 7)

App()
