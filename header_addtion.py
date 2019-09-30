import csv
import os
import shutil


def rename_a(fn):
    data =[]
    f_pass = 'score_data\school_a' + '\\' + fn
    with open(f_pass, newline='', encoding='utf_8_sig') as f:
        r = csv.reader(f)
        for line in r:
            data.append(line)
    with open(f_pass, 'w', newline='', encoding='utf_8_sig') as f:
        w = csv.writer(f)
        w.writerow(['氏名', 'メールアドレス', '得点'])
        w.writerows(data)


def rename_b(fn,semester,final):
    data = []

    if final == 1:
        l_pass = 'score_data\school_b' + '\\' + fn
        with open(l_pass, newline='', encoding='utf_8_sig') as f:
            r = csv.reader(f)
            for line in r:
                data.append(line)
        with open(l_pass, 'w', newline='', encoding='utf_8_sig') as f:
            w = csv.writer(f)
            w.writerow(['氏名', 'メールアドレス', '得点'])
            w.writerows(data)
    else:
        f_pass = 'score_data\school_b' + '\\' + 'semester' + str(semester) + '\\' + fn
        with open(f_pass, newline='', encoding='utf_8_sig') as f:
            r = csv.reader(f)
            for line in r:
                data.append(line)
        with open(f_pass, 'w', newline='', encoding='utf_8_sig') as f:
            w = csv.writer(f)
            w.writerow(['氏名', 'メールアドレス', '得点'])
            w.writerows(data)

        if final == 1:
            l_pass = 'score_data\school_b' + '\\' + fn
            with open(l_pass, newline='', encoding='utf_8_sig') as f:
                r = csv.reader(f)
                for line in r:
                    data.append(line)
            with open(l_pass, 'w', newline='', encoding='utf_8_sig') as f:
                w = csv.writer(f)
                w.writerow(['氏名', 'メールアドレス', '得点'])
                w.writerows(data)


def main():
    if not os.path.exists("back_up_data"):
        shutil.copytree(".\score_data", "back_up_data")

    rename_a('english_score.csv')
    rename_a('science_score.csv')

    for i in range(1, 4):
        rename_b('english_score.csv',  i, 0)
        rename_b('mathematics_score.csv', i, 0)
        rename_b('mathematics_score.csv', i, 0)

    rename_b('final_score.csv', 0, 1)


if __name__ == '__main__':
    main()
