def calculate_dur_num(phones, vowel_list):
    dur_num = []
    current_group = 0
    groups = [[]]
    for phone in phones:
        if phone in vowel_list or phone in ['AP', 'SP']:  # 强制将 'AP' 和 'SP' 视为元音
            current_group += 1
            groups.append([])
        groups[current_group].append(phone)
        if len(dur_num) <= current_group:
            dur_num.append(1)
        else:
            dur_num[current_group] += 1
    return dur_num, groups

def read_vowel_list(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        _, vowel_list = line.split('=')
        return vowel_list.split()

# 从文件读取元音列表
vowel_filename = "dur_num_dict.txt"
vowel_list = read_vowel_list(vowel_filename)

# 输入的音素序列
input_ph_seq = input("请输入用空格隔开的音素序列：")
phones_list = input_ph_seq.strip().split()

dur_num_result, groups_result = calculate_dur_num(phones_list, vowel_list)
print("Calculated dur_num:", " ".join(map(str, dur_num_result)))
for i, group in enumerate(groups_result):
    print(f"Group {i + 1}:", " ".join(group))
