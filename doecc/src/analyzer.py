"""
File analyzer

"""

from typing import List
from dask import dataframe as dd
from datetime import datetime as dt

COLUMN_NAMES = ["Timestamp", "Source", "Destination"]


class FileAnalyzer:
    """
    Class for file analyzer

    """

    def __init__(
        self,
        filename: List[str],
        init_timestamp: str,
        end_timestamp: str,
        hosts: List[str],
    ):

        self.filename = filename
        self.init_timestamp = dt.fromtimestamp(float(init_timestamp) / 1000.0)
        self.end_timestamp = dt.fromtimestamp(float(end_timestamp) / 1000.0)
        self.hosts = hosts
        self.output = {}

    def _read_file(self) -> dd.DataFrame:
        """Read and return a single dask dataframe from list of files"""
        df = dd.read_csv(self.filename, sep=" ", header=None, names=COLUMN_NAMES)
        df["Timestamp"] = dd.to_datetime(df["Timestamp"], unit="ms")
        return df

    def _find(self, data: dd.DataFrame, host: str) -> List[str]:
        """Filter our values that are between init and end times and
        are connected to the specified host"""
        results = data[
            (
                (data["Timestamp"] >= self.init_timestamp)
                & (data["Timestamp"] <= self.end_timestamp)
                & (data["Destination"] == host)
            )
        ]
        return list(results.Source)

    def start(self):
        """
        Start analysing
        """
        dd = self._read_file()
        for host in self.hosts:
            self.output[host] = self._find(dd, host)

    def print_report(self):
        """
        Print out a report with found matches
        """
        init_time = self.init_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        end_time = self.end_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        report = []
        report.append(f"\nSTART TIME: {init_time}")
        report.append(f"END TIME: {end_time}")
        for key in self.output.keys():
            report.append(
                f"\nHosts connected to `{key}` between given times:\n\t{(', '.join(self.output[key]))}"
            )
        print("\n".join(report))
