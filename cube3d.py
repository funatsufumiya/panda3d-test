# https://www.kkaneko.jp/cc/3d/panda3d.html

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# import simplepbr

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)  # Panda3Dエンジンの初期化
        # super().__init__()
        # simplepbr.init()

        # 回転する立方体
        self.cube = self.loader.loadModel("models/box")  # 組み込みモデルの読み込み
        self.cube.setScale(1)  # スケールの設定（1.0が元のサイズ）
        self.cube.setPos(0, 5, 0)  # 位置の設定（X, Y, Z座標）
        self.cube.setColor(1, 0.5, 0, 1)  # 色の設定（R, G, B, A）
        self.cube.setTextureOff(1)  # テクスチャを強制的にオフ
        self.cube.reparentTo(self.render)  # シーングラフへの追加

        # 更新タスクの追加
        self.taskMgr.add(self.update, "updateTask")  # 毎フレーム呼び出される関数を登録

        # 前回のフレーム時刻を記録
        self.prev_time = globalClock.getFrameTime()  # エンジン起動からの経過時間を取得

    def update(self, task):
        # デルタ時間の計算
        current_time = globalClock.getFrameTime()
        dt = current_time - self.prev_time  # 前フレームからの経過時間（デルタ時間）
        self.prev_time = current_time

        # 立方体の回転（フレームレート非依存）
        self.cube.setH(self.cube.getH() + 50 * dt)  # Y軸周りの回転（Heading）
        self.cube.setP(self.cube.getP() + 30 * dt)  # X軸周りの回転（Pitch）

        return Task.cont  # タスクを継続

app = MyApp()
app.run()  # ゲームループの開始
