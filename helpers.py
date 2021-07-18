import pandas as pd


def show_products_info(product_ids, similarities = [], with_sims = True):
    """ Displays the products information (with similarities) given a list of product_ids """

    meta = pd.read_pickle('pickled_dfs/meta.pkl')
    output_products = meta[meta['productid'].isin(product_ids)].copy()
    output_products.reset_index(drop=True, inplace=True)
    if with_sims:
        output_products['similarity'] = similarities 
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  #display the whole df in the terminal.
        print(output_products)


