"""
    This file regroups different functions to be used to format and process
    the data of goo.gl/4JVvEk experiment.
"""

from dataclasses import  dataclass
from datetime import date, datetime
from pprint import pprint
from typing import List, Tuple


@dataclass
class HitData():
    hits: int
    near_misses: int
    full_misses: int
    mean_happiness_hits: int
    mean_willingness_hits: int
    mean_happiness_near_misses: int
    mean_willingness_near_misses: int
    mean_happiness_full_misses: int
    mean_willingness_full_misses: int


@dataclass
class ParticipantSummary():
    condition: str
    name: str
    age: int
    gender: int 
    hit_data: HitData
    maximum_happiness: Tuple[int, datetime]
    minimum_happiness: Tuple[int, datetime]


def parse_file(file_name) -> ParticipantSummary:
    pass


def create_summary_of_participants() -> List[ParticipantSummary]:
    # for each file
    # parse it
    return [] 


def write_participants(participants):
    pass


@dataclass
class DaySummary():
    date: date 
    number_of_participants: int
    number_of_participants_skill: int
    number_of_participants_luck: int
    number_of_participants_mixed: int
    average_number_of_trials: int 


def create_summary_of_days(summary_of_participants) -> List[DaySummary]:
    # create set of already seen IPs
    # create a map of DaySummary (date -> summary)
    # for each participant, if IP not seen: update DaySummary
    # return list
    return [] 


def write_summary_of_days(day_summaries):
    pass


def main():
    print("Creating summary of participants")
    participants = create_summary_of_participants()
    pprint(participants)  # pretty print of participants
    write_participants(participants)

    print("Creating summary of days")
    days = create_summary_of_days(participants)
    pprint(days)  # pretty print of days 
    write_summary_of_days(days)
    pass


if __name__ == "__main__":
    print("Hello, Malika")
    main()
    
