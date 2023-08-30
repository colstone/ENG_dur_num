import csv
from tqdm import tqdm

def read_vowel_list(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        _, vowel_list = line.split('=')
        return vowel_list.split()

def calculate_dur_num(phones, vowel_list):
    dur_num = []
    current_group = 0
    groups = [[]]
    for phone in phones:
        if phone in vowel_list:
            current_group += 1
            groups.append([])
        groups[current_group].append(phone)
        if len(dur_num) <= current_group:
            dur_num.append(1)
        else:
            dur_num[current_group] += 1
    return dur_num, groups

# 从文件读取元音列表
vowel_filename = "dur_num_dict.txt"
vowel_list = read_vowel_list(vowel_filename)

# 读取CSV文件，处理并保存
csv_file_path = input("请输入CSV文件的路径：")
output_csv_path = csv_file_path.replace(".csv", "_processed.csv")

with open(csv_file_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_file:
    csv_reader = csv.DictReader(input_file)
    fieldnames = csv_reader.fieldnames
    fieldnames.append('ph_num')

    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in tqdm(csv_reader, desc="Processing"):
        phones_list = row['ph_seq'].strip().split()
        dur_num_result, _ = calculate_dur_num(phones_list, vowel_list)
        row['ph_num'] = " ".join(map(str, dur_num_result))
        csv_writer.writerow(row)

print(f"Processed data saved to {output_csv_path}")
