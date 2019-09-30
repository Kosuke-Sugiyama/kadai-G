import csv
import os
import shutil
import glob


def rename():
    data = []
    dir_list = glob.glob(os.path.join('score_data', '*'))
    for dir_pass in dir_list:
        f_pass_list = glob.glob(os.path.join(dir_pass, '*'))
        for fpass in f_pass_list:
            csv_pass_list = glob.glob(os.path.join(fpass, '*'))
            for cpass in csv_pass_list:
                with open(cpass, newline='', encoding='utf_8_sig') as f:
                    r = csv.reader(f)
                    for line in r:
                        data.append(line)
                with open(cpass, 'w', newline='', encoding='utf_8_sig') as f:
                    w = csv.writer(f)
                    w.writerow(['氏名', 'メールアドレス', '得点'])
                    w.writerows(data)


def main():
    if not os.path.exists("back_up_data"):
        shutil.copytree(".\score_data", "back_up_data")

    rename()


if __name__ == '__main__':
    main()
