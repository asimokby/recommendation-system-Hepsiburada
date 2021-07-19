import pandas as pd


def cb_m1_recommend(product_id, n_products):
    """ Returns similar products ids to the product id given along with the similarities using method 1"""

    m1_sim_mat = pd.read_pickle("cb_m1.pkl")
    product_profile = m1_sim_mat[m1_sim_mat['productid'] == product_id]
    product_profile_dict = product_profile.to_dict()
    del product_profile_dict['productid'] # deleting the product_id (1st column)
    productid_sim_tuples = [(key, sub_dict[list(sub_dict)[0]]) for key, sub_dict in product_profile_dict.items()]
    top_n_products = sorted(productid_sim_tuples, key=lambda productid_sim_tuples:productid_sim_tuples[1],
                reverse=True)[1:n_products+1]
    product_ids, similarities = list(zip(*top_n_products))
    return product_ids, similarities

