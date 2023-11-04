import os
from dotenv import load_dotenv
import logging
from plexapi.myplex import MyPlexAccount

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def main():
    username = os.getenv('PLEX_USERNAME')
    password = os.getenv('PLEX_PASSWORD')

    try:
        account = MyPlexAccount(username, password)
        watchlist = account.watchlist()

        for item in watchlist:
            logging.info(f"Removing {item.title} from watchlist")
            account.removeFromWatchlist(item)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
