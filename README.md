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

3. 将您的输入 CSV 文件放置在与脚本相同的目录中。

4. 在相同的目录中创建一个名为 `dur_num_dict.txt` 的文件。按以下格式添加您的元音列表：

   ```
   vowels=ay iy uw aa...
   ```

5. 运行脚本：

   ```shell
   python ENG_dur_num.py
   ```

   按照提示输入输入的 CSV 文件名。

6. 另一个脚本将处理 CSV 文件，将 "dur_num" 添加到一个新的 CSV 文件中，原文件名后面加上 "_processed"。(只适用于DiffSinger Variance模型的csv处理)
