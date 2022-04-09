import api
'''
    Main module.
    For a new post we need for 2 parameters.
    1. Text to be posted
    2. Phrase used to search for tweets. (query filter)
'''

def main():
    # Samples text
    ptax = '''
        BRL USD exchange rate
        PTAX: cotação de compra
        10:00h 4,7390
        11:00h 4,7613
        12:00h 4,7512

        Post 4
    '''

    ntnb = '''
        Tesouro IPCA+ com Juros Semestrais
        Brazilian sovereign inflation-linked bonds: coupons
        2032 5.41% (+1.7%)
        2040 5.47% (+1.1%)
        2055 5.57% (+0.9%)

        Post 4
    '''
    # Query
    query_ptax = 'BRL USD exchange rate  -is:retweet'
    query_ntnb = 'Tesouro IPCA+ com Juros Semestrais  -is:retweet'

    response = api.tweet_to_publish(ptax, query_ptax)
    if response is not None:
        print('Successfully tweeted\n' + \
              f'Tweet ID: {response.data["id"]}')


if __name__ == '__main__':
    main()
