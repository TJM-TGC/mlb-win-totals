import os
import pandas as pd

class Broom:
    """
    A class to simplify reading and merging CSVs from a 
    given directory, namely 'resources'
    """
    
    def __init__(
        self, 
        csv_directory: str = 'resources',
        ):
        self.csv_directory = csv_directory

    def get_csv_directory_files(
        self,
        ) -> map:
        """
        Returns all csvs in self.csv_directory or None if 
        the attribute has been set to None
        """
        if self.csv_directory is None:
            return
        if not os.path.isdir(self.csv_directory):
            raise FileNotFoundError('CSV Directory not found')
        is_csv = lambda f: '.csv' in f and 'team' in f
        csvs = tuple(filter(is_csv, os.listdir(self.csv_directory)))
        for csv_file in csvs:
            yield os.sep.join(['resources', csv_file,])

    def data_all_years(
            self,
            ) -> pd.DataFrame:
        data = list(self.make_frames())
        for i in range(1, len(data)):
            data[0] = pd.concat((data[i], data[0]),)
        data[0].year = pd.to_numeric(data[0].year)
        data[0].columns = tuple(colname.lower().replace('/', '_per_') for colname in data[0].columns)
        return data[0]

    def make_frames(
        self, 
        csv_directory: str = None,
        usecols: list = ['Tm', 'R', 'R.1', 'RA/G', 'R/G'],
        ) -> map:
        if csv_directory is None:
            if self.csv_directory is None:
                raise TypeError('No CSV directory given')
            csv_directory = self.csv_directory
        for file in tuple(self.get_csv_directory_files()):
            df = pd.read_csv(file, usecols = usecols).dropna()
            df['year'] = file.split(os.sep)[-1][:4]
            yield df


