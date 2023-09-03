#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Freebie,Company,Dev


if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Replace this with the actual Freebie ID you want to debug
    freebie_id_to_debug = 1  # Replace with the ID of the Freebie you want to inspect

    freebie = session.query(Freebie).get(freebie_id_to_debug)

    if freebie:
        print(f"Freebie ID: {freebie.id}")
        print(f"Freebie Item Name: {freebie.item_name}")
        print(f"Freebie Value: {freebie.value}")

        # Check if Freebie has a Dev associated
        if freebie.dev:
            print(f"Dev for Freebie: {freebie.dev.name}")
        else:
            print("No Dev associated with this Freebie")

        # Check if Freebie has a Company associated
        if freebie.company:
            print(f"Company for Freebie: {freebie.company.name}")
        else:
            print("No Company associated with this Freebie")
    else:
        print(f"Freebie with ID {freebie_id_to_debug} not found.")
    


company_id_to_test = 1  # Replace with a valid Company ID
dev_id_to_test = 1      # Replace with a valid Dev ID

# Test 1: Fetch a Company and inspect its freebies and devs
company = session.query(Company).get(company_id_to_test)

if company:
    print(f"Company ID: {company.id}")
    print(f"Company Name: {company.name}")
    print(f"Company Founding Year: {company.founding_year}")

    print("Freebies for this Company:")
    for freebie in company.freebies:
        print(f"  Freebie ID: {freebie.id}")
        print(f"  Item Name: {freebie.item_name}")
        print(f"  Value: {freebie.value}")

    print("Devs associated with this Company:")
    for dev in company.devs:
        print(f"  Dev ID: {dev.id}")
        print(f"  Name: {dev.name}")
else:
    print(f"Company with ID {company_id_to_test} not found.")

# Test 2: Fetch a Dev and inspect the companies they collected freebies from
dev = session.query(Dev).get(dev_id_to_test)

if dev:
    print(f"Dev ID: {dev.id}")
    print(f"Dev Name: {dev.name}")

    print("Companies associated with this Dev:")
    for company in dev.companies:
        print(f"  Company ID: {company.id}")
        print(f"  Name: {company.name}")
else:
    print(f"Dev with ID {dev_id_to_test} not found.")
# Replace dev_id_to_query with the ID of the Dev you want to query
dev_id_to_query = 1  # Replace with the ID of the Dev you want to query

dev = session.query(Dev).get(dev_id_to_query)

if dev:
   

    for freebie in dev.collected_freebies:
        print(f"Freebie ID: {freebie.id}")
        print(f"Item Name: {freebie.item_name}")
        print(f"Value: {freebie.value}")
else:
    print(f"Dev with ID {dev_id_to_query} not found.")

session.close()


