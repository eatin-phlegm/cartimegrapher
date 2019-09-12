import pandas as pd
from ast import literal_eval as l_eval


class Logbook:
    def __init__(self, filename=""):
        self._event_df = pd.DataFrame()  # initialize event df
        self.filename = filename
        # load file if given
        self.load()  # preps new df if filename hasn't been given a value

    # sets up a new df to have the proper columns/rows headings, etc.
    def prep_dfs(self):
        # event timeline info
        self._event_df['Event Title'] = pd.Series()
        self._event_df['Event Description'] = pd.Series()
        self._event_df['Date Occurring'] = pd.Series()
        self._event_df['Characters Involved'] = pd.Series()
        self._event_df['Location'] = pd.Series()
        self._event_df['Civilizations Involved'] = pd.Series()
        self._event_df['Timeline'] = pd.Series()

    def load(self, filename=""):
        if filename:
            self.filename = filename

        if self.filename:
            self._event_df = pd.read_excel(self.filename, 'Events')
        else:
            self.prep_dfs()

    # adds the data from a given file to the current data
    def import_excel(self, filename):
        if filename:
            tmp_event = pd.read_excel(filename, 'Events')
            self._event_df = pd.concat([self._event_df, tmp_event], sort=False)

    # adds the current data into a given file
    def export_to_excel(self, filename):
        if filename:
            tmp_event = pd.read_excel(filename, 'Events')
            tmp_event = pd.concat([self._event_df, tmp_event], sort=False)
            writer = pd.ExcelWriter(filename)
            tmp_event.to_excel(writer, 'Events')
            writer.save()

    # save, assumes filename is set
    def save_excel(self):
        if self.filename:
            writer = pd.ExcelWriter(self.filename)
            self._event_df.to_excel(writer, 'Events')
            writer.save()

    # saves the dataframe to a given savefile destination, csv format
    def save_as_excel(self, filename="untitled.xlsx"):
        self.filename = filename
        self.save_excel()

    # returns a tuple of event names and their dates
    def get_event_timeline(self):
        return self._event_df['Event Title'].values, self._event_df['Date Occurring'].values

    def get_filtered_event_timeline(self, category, values_allowed):
        assert isinstance(category, str)
        assert isinstance(values_allowed, list)
        filtered_df = pd.DataFrame()
        for s in values_allowed:
            filtered_df = pd.concat([self._event_df[self._event_df[category].str.contains(s)], filtered_df], sort=False)
        return filtered_df['Event Title'].values, filtered_df['Date Occurring'].values

    def remove_event(self, event_titles):
        if event_titles:
            for event_title in event_titles:
                tmp_df = self._event_df[self._event_df['Event Title'] != event_title]
                self._event_df = tmp_df

    def edit_event(self, event_to_edit_name, new_event_data):
        self.remove_event(event_to_edit_name)
        self.new_event(new_event_data)

    def get_event_data(self, event_title):
        data = self._event_df[self._event_df['Event Title'].isin(event_title)].values
        return data

    def new_event(self, event_data):
        self._event_df = self._event_df.append({'Event Title': event_data[0], 'Event Description': event_data[1],
                                                'Date Occurring': event_data[2],
                                                'Characters Involved': event_data[3],
                                                'Location': event_data[4], 'Civilizations Involved': event_data[5],
                                                'Timeline': event_data[6]}, ignore_index=True)

    def get_unique_chars(self):
        data = self._event_df['Characters Involved'].values
        all_strings = list()
        to_be_uniques = list()
        if data.any():
            for s in data:
                s = l_eval(str(s))
                all_strings.append(s)
        for l in all_strings:
            for name in l:
                to_be_uniques.append(name)

        return set(to_be_uniques)

    def get_unique_civs(self):
        all_strings = list()
        to_be_uniques = list()
        data = self._event_df['Civilizations Involved'].values
        if data.any():
            for s in data:
                s = l_eval(str(s))
                all_strings.append(s)

        for l in all_strings:
            for name in l:
                to_be_uniques.append(name)

        return set(to_be_uniques)

    def get_unique_locs(self):
        data = self._event_df['Location'].apply(lambda x: str(x)).unique()
        return data

    def get_unique_timelines(self):
        data = self._event_df['Timeline'].apply(lambda x: str(x)).unique()
        return data
