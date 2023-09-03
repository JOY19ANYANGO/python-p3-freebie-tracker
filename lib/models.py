from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    # Define a one-to-many relationship between Company and Freebie
    freebies = relationship("Freebie", back_populates="company")

    # Define a many-to-many relationship between Company and Dev
    devs = relationship("Dev", secondary="freebies", back_populates="companies")

    def __repr__(self):
        return f'<Company {self.name}>'
    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
     
        return new_freebie
    @classmethod
    def oldest_company(cls, session):
       oldest = session.query(cls).order_by(cls.founding_year).first()
       return oldest
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'
    collected_freebies  = relationship("Freebie", back_populates="dev")
    
    # Define the many-to-many relationship between Dev and Company
    companies = relationship("Company", secondary="freebies", back_populates="devs")
    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False
    
    def give_away(self, target_dev, freebie):
        if freebie.dev == self:
            freebie.dev = target_dev
            return True
        else:
            return False
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value= Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship("Dev", back_populates="collected_freebies")
    company = relationship("Company", back_populates="freebies")
    def print_details(self):
        if self.dev and self.company:
            return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
        else:
            return "Details not available"

