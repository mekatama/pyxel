#keyで移動
import pyxel

class App:
    def __init__(self):
        # 画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 120, caption="Hello Pysel")
        # editorデータ読み込み(コードと同じフォルダにある)
        pyxel.load("my_resource.pyxres")
        # 初期配置
        self.player_x = 80
        self.player_y = 60
        # 実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_player()

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

    def draw(self):
        # 画面クリア 0は黒
        pyxel.cls(0)
        # editorデータ描画
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 0)
            #描画座標(左上のX座標)
            #描画座標(左上のY座標)
            #画像番号
            #切り出しの左上のX座標
            #切り出しの左上のY座標
            #切り出す幅
            #切り出す高さ
            #抜き色(パレット番号)
App()
