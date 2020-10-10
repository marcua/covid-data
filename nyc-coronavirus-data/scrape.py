import requests

from pydriller.repository_mining import RepositoryMining


RAW_FILE_PATTERN = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/{}/recent/recent-4-week-by-modzcta.csv'


def main():
    commits = (
        RepositoryMining('https://github.com/nychealth/coronavirus-data.git',
                         filepath='recent/recent-4-week-by-modzcta.csv',
                         order='reverse')
        .traverse_commits())
    for commit in commits:
        with open('raw/{}.csv'.format(commit.committer_date.date()), 'wb') as output:
            response = requests.get(RAW_FILE_PATTERN.format(commit.hash))
            output.write(response.content)
        break  # Only get the most recent commit to be kind.
            
    
if __name__ == '__main__':
    main()
