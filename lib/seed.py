from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear old data
    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()
    session.commit()

    print("Seeding companies...")

    companies = [
        Company(
            name=fake.company(),
            founding_year=random.randint(1900, 2023)
        )
        for i in range(50)
    ]

    session.add_all(companies)

    print("Seeding devs...")

    devs = [
        Dev(
            name=fake.name()
        )
        for i in range(50)
    ]

    session.add_all(devs)

    print("Seeding freebies...")

    freebies = [
        Freebie(
            item_name=fake.word(),
            value=random.randint(1, 100),  # Adjust the range as needed
            dev=random.choice(devs),
            company=random.choice(companies)
        )
        for i in range(100)
    ]

    session.add_all(freebies)

    try:
        session.commit()
        print("Data committed successfully.")
    except Exception as e:
        session.rollback()
        print("Error committing data:", e)
