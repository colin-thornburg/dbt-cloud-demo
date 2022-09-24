import pandas as pd
import collections
from dataclasses import dataclass



def model(dbt, session):
    dbt.config(materialized="table")
    people = [("Michele", "Vallisneri", "July 15"),
        ("Albert", "Einstein", "March 14"),
        ("John", "Lennon", "October 9"),
        ("Jocelyn", "Bell Burnell", "July 15")]


    ###--- Collections/Named Tuples ---###
    # persontype = collections.namedtuple('person', ['firstname', 'lastname', 'birthday'])
    # namedpeople = [persontype(*person) for person in people]
    # df = pd.DataFrame(namedpeople)
    # return df

    ###--- Apply a filter ---###
    # july_15_bdays = [person for person in namedpeople if person.birthday == "July 15"]
    # df = pd.DataFrame(july_15_bdays)
    # return df

    ###--- dataclasses ---###
    @dataclass
    class personclass:
        firstname: str
        lastname: str
        birthday: str = 'unknown'

        def fullname(self):
            return self.firstname +' '+ self.lastname

    michele = personclass('Michele', 'Vallisneri')
    michele_df = pd.DataFrame([michele]) #add a return for this df to see michele's record
    name = michele.fullname()
    df = pd.DataFrame([name], columns=['fullname']) #this will return michele's full name as the DataFrame
    return df    
    