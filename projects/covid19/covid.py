#!/usr/bin/python3 -tt

import urllib.request
import json
import click
import pprint

__author__ = "Abhishek Anand Amralkar"


@click.group()
def main():
    """
    CLI for querying Covid19 Data for India by Abhishek Amralkar
    """
    pass


def states_data(statename):
    '''
    function queries the covid19 india api and get the state data
    district wise
    '''
    with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
        states_data = json.loads(url.read())
        result = states_data[statename]['districtData']
        return result


@main.command()
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def country(acrd):
    '''
    function return the total cases across country
    '''
    with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
        states_data = json.loads(url.read())
        count = 0
        for state, info in states_data.items():
            #print(info['districtData'])
            #print(type(info['districtData']))
            for district, info1 in info['districtData'].items():
                count += info1.get(acrd)
        click.echo(
            print(f"Total {acrd} cases in India are : {count}", end=''))


@main.command()
def states_name():
    '''
    function return the Indian States and Union Territories Name
    '''
    with urllib.request.urlopen("https://api.covid19india.org/state_district_wise.json") as url:
        states_data = json.loads(url.read())
        print(f"India's States and Union Territories Names are:")
        print("<--******************************************-->")
        state_list = []
        for state, info in states_data.items():
            state_list.append(state)
        click.echo(
            print(state_list[1:]))

#print(states_name())


@main.command()
@click.argument('statename')
def districts_name(statename):
    '''
    function return the districts name given the state name
    '''
    state = states_data(statename)
    print(f"State {statename} districts names are:")
    print("<-******************************************->")
    district_list = []
    for district, info in state.items():
        district_list.append(district)
    click.echo(
        print(district_list))
        


@main.command()
@click.argument('statename')
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def state(statename, acrd):
    '''
    function returns the total statewise cases like
    active, recovered, deceased, confirmed
    '''
    state = states_data(statename)
    #print(state)
    count = 0
    for district, info in state.items():
        count += info.get(acrd)
    click.echo(
                print(f"Total {acrd} cases in {statename} are: {count}", end=''))
    return count


@main.command()
@click.argument('statename')
def state_cases(statename):
    '''
    fucntion returns the state data district wise
    with all the keys
    '''
    state = states_data(statename)
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
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def districts_cases(statename, acrd):
    '''
    function returns the district wise data for the key
    active, deceased, confirmed, recovered, delta.
    It takes input as a state name and the key mentioned above
    with flag -a or --acrd.
    '''
    state = states_data(statename)
    for district, info in state.items():
        #print(type(info))
        click.echo(
            print(f"{acrd} cases in district {district} are: {info.get(acrd)}", end=''))


@main.command()
@click.argument('statename')
@click.argument('districtname')
@click.option(
    '--acrd', '-a',
    help='active, deceased, recovered, confirmed'
)
def district(statename, districtname, acrd):
    '''
    function returns the district wise data for the key
    active, deceased, confirmed, recovered, delta.
    It takes input as a state name and the key mentioned above
    with flag -a or --acrd.
    '''
    state = states_data(statename)
    for district, info in state.items():
        if district.lower() == districtname.lower():
            click.echo(
                print(f"{acrd} cases in district {districtname} are: {info.get(acrd)}", end=''))



if __name__ == '__main__':
    main()
