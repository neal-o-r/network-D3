import pandas as pd
import json

def make_network_json(df, n=100):
    """
    takes in a df and a number of links,
    saves a json of nodes and connections to n
    """
    col = '#000'
    top = df.sort_values(by='Frequency').tail(n)

    ns = {*top.K1} | {*top.K2}

    nodes = [{'colour':col,
              'name':n,
              'id': n} for n in ns]

    links = [{'source': t.K1,
              'target': t.K2,
              'value' : t.Frequency} for i, t in top.iterrows()]

    json.dump({'nodes':nodes, 'links':links}, open('network.json', 'w'),
            indent=4)

    return nodes, links



if __name__ == '__main__':

    df = pd.read_csv('data.csv')
    n, l = make_network_json(df)
