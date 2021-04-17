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
        is_csv = lambda f: '.csv' in f
        csvs = tuple(filter(is_csv, os.listdir(self.csv_directory)))
        for csv_file in csvs:
            yield os.sep.join(['resources', csv_file,])

    def merge_csvs(
        self, 
        csv_directory: str = None,
        ) -> pd.DataFrame:
        if csv_directory is None:
            if self.csv_directory is None:
                raise TypeError('No CSV directory given')
            csv_directory = self.csv_directory
        csvs = tuple(self.get_csv_directory_files())
        data = pd.read_csv(csvs[0])
        i = 0
        while True:
            if i >= len(csvs) - 1:
                break
            data = pd.concat((data, pd.read_csv(csvs[i]),))
            i += 1
        return data

