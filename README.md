# 音素数量计算（For DiffSinger）

这个 Python 脚本用于计算给定音素序列中音素的数量，并将计算得到的音素数量作为 "dur_num" 输出；另一个 Python 脚本可以将 "dur_num" 添加到一个 CSV 文件中。

## 前提条件

- Python 3.x
- tqdm 库（用于显示进度条）

## 使用方法

1. 克隆仓库：

   ```shell
   git clone https://github.com/colstone/ENG_dur_num.git
   ```

2. 安装所需的库：

   ```shell
   pip install tqdm
   ```

3. 在相同的目录中创建一个名为 `dur_num_dict.txt` 的文件。按以下格式添加您的元音列表：

   ```
   vowels=ay iy uw aa...
   ```

4. 运行脚本：

   ```shell
   python ENG_dur_num.py
   ```


5. 另一个脚本将处理 CSV 文件，将 "dur_num" 添加到一个新的 CSV 文件中，原文件名后面加上 "_processed"。(只适用于DiffSinger Variance模型的csv处理)

## 其他说明

关于处理二段式音素（包括复合元音）的方法

   1. 二段式音素（如日语，中文（不想拆分复合元音的）等）处理方式如下：

      修改 `dur_num_dict.txt` ，把元音的音素写进去：

      ```
      vowels=a an ir iang A1 E1 N1...
      ```

   2. 二段式音素（如中文（需要拆分复合元音的），粤语，韩语等）处理方式如下：

      修改 `dur_num_dict.txt` ，把元音部分的第一个音位的音素写进去（例如 `liang-->l iA ng`中的 `iA`，即为元音的第一个音位代表的音素）：

      ```
      vowels=iA ee AA ya oi oo...
      ```
