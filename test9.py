 #gameover作る
from random import randint
import pyxel

#画面遷移用の変数
SCENE_TITLE = 0	    #タイトル画面
SCENE_PLAY = 1	    #ゲーム画面
SCENE_GAMEOVER = 2  #ゲームオーバー画面

class App:
    def __init__(self):
        # 画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 120, caption="Hello Pysel")
        # editorデータ読み込み(コードと同じフォルダにある)
        pyxel.load("my_resource.pyxres")
        #画面遷移の初期化
        self.scene = SCENE_TITLE
        #得点初期化
        self.score = 0
        # 初期配置
        self.player_x = 80
        self.player_y = 60
        # fruit初期配置 x座標 y座標 表示flag on 種類(0と1)を4個用意
        self.fruit = [(i * 60, randint(0, 104), True, randint(0, 1)) for i in range(4)]

        #BGM再生(MUSIC 0番をloop再生)
        pyxel.playm(0, loop = True)
        # 実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #処理の画面分岐
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()


    #タイトル画面処理用update
    def update_title_scene(self):
        #ENTERでゲーム画面に遷移
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.scene = SCENE_PLAY

    #ゲーム画面処理用update
    def update_play_scene(self):

        self.update_player()

        # i番目とv要素(各fruitの要素)　enumerate関数で各fruitの値を取得して実行しているっぽ
        for i, v in enumerate(self.fruit):
            # (*v)ってタプルという複数の要素を管理するデータ型の一つらしい
            # つまり、初期化で設定したデータをタプル型にしてupdate_fruit関数に渡しているっぽい
            self.fruit[i] = self.update_fruit(*v)

    #ゲームオーバー画面処理用update
    def update_gameover_scene(self):
        #ENTERでタイトル画面に遷移
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.score = 0 #得点初期化
            self.scene = SCENE_TITLE

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

    def update_fruit(self, x, y, is_active, ver):
        #衝突判定(playerとfruitの座標の絶対値から衝突しているか判定している)
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            #種別で分岐
            if ver == 0:
                is_active = False   #表示を消す
                self.score += 10    #scoe加算
                pyxel.play(1,0,loop = False)     #SE再生(CH 1,SOUND 0,単発再生)
            elif ver == 1:
                is_active = False   #表示を消す
                pyxel.play(1,2,loop = False)     #SE再生(CH 1,SOUND 0,単発再生)
                self.scene = SCENE_GAMEOVER
            
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
            # 種類再設定(ランダム)
            ver = randint(0, 1)

        # 返り値を設定
        return (x, y, is_active, ver)

    def draw(self):
        # 画面クリア 0は黒
        pyxel.cls(0)

        #描画の画面分岐
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()

        #score表示用に整形(format関数の文字列操作を利用)
        s = "Score:{:>4}".format(self.score)
        #text表示(x座標、y座標、文字列、color)
        pyxel.text(5, 4, s, 7)

    #タイトル画面描画用update
    def draw_title_scene(self):
        pyxel.text(70, 40, "GAME", 7)
        pyxel.text(50, 80, "- PRESS ENTER -", 7)

    #ゲーム画面描画用update
    def draw_play_scene(self):
        # editorデータ描画
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 0)

        # draw fruits
        for x, y, is_active, ver in self.fruit:
            if is_active:
                #verを見て画像変更
                if ver == 0:
                    pyxel.blt(x, y, 0, 16, 0, 16, 16, 0)
                elif ver == 1:
                    pyxel.blt(x, y, 0, 32, 0, 16, 16, 0)

    #ゲームオーバー画面描画用update
    def draw_gameover_scene(self):
        pyxel.text(55, 40, "GAME OVER", 7)
        pyxel.text(50, 80, "- PRESS ENTER -", 7)
App()
