import csv
import os
import shutil
import glob


def re_content(fpass):
    backpass = fpass.replace('score_data', 'back_up_data')
    data = []
    with open(backpass, newline='', encoding='utf_8_sig') as f:
        r = csv.reader(f)
        for line in r:
            data.append(line)
    with open(fpass, 'w', newline='', encoding='utf_8_sig') as f:
        w = csv.writer(f)
        w.writerow(['氏名', 'メールアドレス', '得点'])
        w.writerows(data)


def add_header():
    for school_pass in glob.glob(os.path.join('score_data', '*')):
        for file_pass in glob.glob(os.path.join(school_pass, '*')):
            if os.path.isfile(file_pass):
                re_content(file_pass)
            else:
                for csv_pass in glob.glob(os.path.join(file_pass, '*')):
                    re_content(csv_pass)


def main():
    if not os.path.exists("back_up_data"):
        shutil.copytree(".\score_data", "back_up_data")
    add_header()


if __name__ == '__main__':
    main()
