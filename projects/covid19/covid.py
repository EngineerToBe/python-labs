#!/usr/bin/python3 -tt

import urllib.request
import json
import click
import pprint

__author__ = "Abhishek Anand Amralkar"


@click.group()
def main():
    """
    Simple CLI for querying Covid19 Data for India by Abhishek Amralkar
    """
    pass


def get_states_data(statename):
    with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
        states_data = json.loads(url.read())
        result = states_data[statename]['districtData']
        #print(result)
        return result


@main.command()
@click.argument('statename')
def get_state_all_cases(statename):
    state = get_states_data(statename)
    #pprint(type(state))
    for district, info in state.items():
        print('<-****************************************************->')
        print('Covid19 information for district', district)
        print('<-****************************************************->')
        for key in info:
            click.echo(print(f"{key} {info[key]}"))


@main.command()
@click.argument('statename')
@click.option(
    '--key', '-k',
    help='active, deceased, recovered, confirmed'
)
def get_state_wise_cases_with_key(statename, key):
    '''
    function returns the district wise data for the key
    active, deceased, confirmed, recovered.
    It takes input as a state name and the key mentioned above
    with flag -k or --key.
    '''
    state = get_states_data(statename)
    for district, info in state.items():
        #print(type(info))
        print(f"{key} cases in district {district} are: {info.get(key)}")


if __name__ == '__main__':
    main()
