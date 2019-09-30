import csv
import os
import shutil
import glob


def rename_a():
    data =[]
    pass_list = glob.glob(os.path.join('score_data\school_a', '*'))
    for f_pass in pass_list:
        with open(f_pass, newline='', encoding='utf_8_sig') as f:
            r = csv.reader(f)
            for line in r:
                data.append(line)
        with open(f_pass, 'w', newline='', encoding='utf_8_sig') as f:
            w = csv.writer(f)
            w.writerow(['氏名', 'メールアドレス', '得点'])
            w.writerows(data)


def rename_b():
    data = []
    pass_list = glob.glob(os.path.join('score_data\school_b', '*'))
    for f_pass in pass_list:
        fpass_list = glob.glob(os.path.join(f_pass, '*'))
        for fpass in fpass_list:
            with open(fpass, newline='', encoding='utf_8_sig') as f:
                r = csv.reader(f)
                for line in r:
                    data.append(line)
            with open(fpass, 'w', newline='', encoding='utf_8_sig') as f:
                w = csv.writer(f)
                w.writerow(['氏名', 'メールアドレス', '得点'])
                w.writerows(data)


def main():
    if not os.path.exists("back_up_data"):
        shutil.copytree(".\score_data", "back_up_data")

    rename_a()
    rename_b()


if __name__ == '__main__':
    main()
