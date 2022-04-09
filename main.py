import api
from tweepy.errors import Unauthorized

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

        Post 1
    '''

    ntnb = '''
        Tesouro IPCA+ com Juros Semestrais
        Brazilian sovereign inflation-linked bonds: coupons
        2032 5.41% (+1.7%)
        2040 5.47% (+1.1%)
        2055 5.57% (+0.9%)

        Post 5
    '''
    # Query
    query_ptax = 'BRL USD exchange rate  -is:retweet'
    query_ntnb = 'Tesouro IPCA+ com Juros Semestrais  -is:retweet'

    try:
        response = api.tweet_to_publish(ntnb, query_ntnb)
        if response is not None:
            print('Successfully tweeted\n' + \
                  f'Tweet ID: {response.data["id"]}')
    except Unauthorized as e:
        print('Put your keys in the settings.ini file.')
        print('Error: {}'.format(e))
    except BaseException as e:
        print('Erro: {}'.format(e))


if __name__ == '__main__':
    main()
