import glob

from csv import DictReader
from csv import DictWriter
from datetime import datetime

def main():
    raw_csvs = glob.glob('raw/*.csv')
    raw_csvs.sort(
        key=lambda x: datetime.strptime(x[:-4], 'raw/%Y-%m-%d'),
        reverse=True)
    # Read the various CSVs as DictReaders and output them with a
    # DictWriter: this allows us to protect against the different CSV
    # files having different column orders.
    with open('recent-4-week-by-modzcta.csv', 'w+') as output_csv:
        writer = None
        for raw_csv in raw_csvs:
            day = raw_csv[4:-4]  # Strip 'raw/*' and '*.csv'
            with open(raw_csv) as input_csv:
                reader = DictReader(input_csv)
                for row in reader:
                    if not writer:
                        writer = DictWriter(output_csv, ['date'] + list(row.keys()))
                        writer.writeheader()
                    row['date'] = day
                    writer.writerow(row)
                        
            
    
if __name__ == '__main__':
    main()
