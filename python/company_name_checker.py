'''
Script to display interview questions given by certain companies.
'''

import os


def check_for_companies():
    current_directory = os.path.join(
        'home', 'elvisrodriguez1992', 'daily_coding_problems', 'python')
    companies = {}
    filenames = os.listdir()
    for filename in filenames:
        if '.py' in filename and filename != 'company_name_checker.py':
            with open(filename, 'r') as file:
                for line in file.readlines():
                    if 'This problem was asked by' in line:
                        split_line = line.split(' ')
                        index = split_line.index('by')
                        split_line[-1] = split_line[-1][:-2]
                        company = ' '.join(split_line[index + 1:])
                        if company not in companies:
                            companies[company] = [filename]
                        else:
                            companies[company].append(filename)
                        break
    for company in sorted(companies.keys()):
        print('Company: {company} ({number}):'.format(
            company=company, number=len(companies[company])
        ))
        for filename in companies[company]:
            print(filename)
        print('-' * 40)


if __name__ == '__main__':
    check_for_companies()
