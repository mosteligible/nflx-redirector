from utils import TEST_DB, DB_PAYLOAD

def main():
    TEST_DB.DeleteMovie(netflixid=DB_PAYLOAD.NetflixId)


if __name__ == "__main__":
    main()
