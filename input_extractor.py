from pathlib import Path
import csv


class InputExtractor:

    def __init__(self):
        """Init the extractor and load all data from CSV files."""
        self.file_path = Path(__file__).parent / "data"

        # data sets
        self.first_name_data = {}
        self.last_name_data = {}
        self.life_exp_data = {}
        self.gender_prob_data = {}
        self.marriage_rate_data = {}
        self.birth_rate_data = {}
        self.rank_prob_data = []

        # load data
        self.import_data()


    def import_data(self):
        """Load all reference data from CSV files """

        # load first name data
        fp = self.file_path / "first_names.csv"
        with open(fp, 'r') as first_name_data_input:
            reader = csv.DictReader(first_name_data_input)
            for r in reader:
                name = r['name']
                decade = r['decade']
                gender = r['gender']
                freq = float(r['frequency'])

                # match by gender and decade
                match_criteria = (gender, decade)
                match_result = (name, freq)

                # init list if not exists
                if match_criteria not in self.first_name_data:
                    self.first_name_data[match_criteria] = []

                # populate match lookup
                self.first_name_data[match_criteria].append(match_result)


        # load last name data
        fp = self.file_path / "last_names.csv"
        with open(fp, 'r') as last_name_data_input:
            reader = csv.DictReader(last_name_data_input)
            for r in reader:
                name = r['LastName']
                rank = int(r['Rank'])
                dec = r['Decade']

                # populate match lookup
                match_result = (name, rank, dec)

                if dec not in self.last_name_data:
                    self.last_name_data[dec] = []

                # populate match lookup
                self.last_name_data[dec].append(match_result)


        # load gender probs
        fp = self.file_path / "gender_name_probability.csv"
        with open(fp, 'r') as gender_prob_data_input:
            reader = csv.DictReader(gender_prob_data_input)
            for row in reader:
                prob = float(row['probability'])
                gender = row['gender']
                decade = row['decade']

                if decade not in self.gender_prob_data:
                    self.gender_prob_data[decade] = {}

                self.gender_prob_data[decade][gender] = prob

        # load birth rates
        fp = self.file_path / "birth_and_marriage_rates.csv"
        with open(fp, 'r') as birth_rate_data_input:
            reader = csv.DictReader(birth_rate_data_input)
            for row in reader:
                birth_rate = float(row['birth_rate'])
                marriage_rate = float(row['marriage_rate'])
                decade = row['decade']

                # set birth and marriage rates for decade
                self.birth_rate_data[decade] = birth_rate
                self.marriage_rate_data[decade] = marriage_rate

        # load life exp data
        fp = self.file_path / "life_expectancy.csv"
        with open(fp, 'r') as life_exp_data_input:
            reader = csv.DictReader(life_exp_data_input)
            for row in reader:
                exp = float(row['Period life expectancy at birth'])
                yr = int(row['Year'])

                # assign exp for the given year
                self.life_exp_data[yr] = exp


        # get and load ranks for last names
        fp = self.file_path / "rank_to_probability.csv"
        with open(fp, 'r') as rank_prob_data_input:
            ranks_raw = rank_prob_data_input.read().strip().split(',')
            for prob in ranks_raw:
                prob_fl = float(prob)

                # append last name probability ranking
                self.rank_prob_data.append(prob_fl)

        print('Data loaded successfully.')

