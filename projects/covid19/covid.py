#!/usr/bin/python3 -tt

import urllib.request
import json
import click

__author__ = "Abhishek Anand Amralkar"


@click.group()
def main():
    """
    Simple CLI for querying Covid19 Data for India by Oyetoke Toby
    """
    pass


#@main.command()
#@click.argument('statename')
def get_states_data(statename):
    with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
        states_data = json.loads(url.read())
        result = states_data[statename]['districtData']
        #print(result)
        return result

#print(get_states_data('Bihar'))
#name = str(sys.argv)
@main.command()
@click.argument('statename')
def get_state_all_cases(statename):
    state = get_states_data(statename)
    print(state)
    for district, info in state.items():
        print('<-********************->')
        print('Covid19 information for district', district)
        print('<-********************->')
        for key in info:
            click.echo(print(key, info[key]))

#print(get_district_cases('Maharashtra'))

state = get_states_data('Madhya Pradesh')
print(type(state))
#print(state)
for district, info in state.items():
    print(district, info['active'])

# This is the standard boilerplate that calls the main() function.
#if __name__ == '__main__':
#    main()
