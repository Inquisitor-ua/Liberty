import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship


engine = sqlalchemy.create_engine('postgresql://postgres:17012005@localhost:5432/oblik')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Pidrozdil(Base):
    __tablename__ = "pidrozdil"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_count = Column(Integer)
    current_count = Column(Integer)
    pidrozdil_soldier = relationship('Soldier', back_populates='soldier')

class Absence(Base):
    __tablename__ = "absence"
    id = Column(Integer, primary_key=True)
    soldier_id = Column(Integer, ForeignKey('soldier.id'))
    vid_absence = Column(String)
    plannd_return_date = Column(Integer)
    fact_return_date = Column(Integer)

class Naryad(Base):
    __tablename__ = "naryad"
    id = Column(Integer, primary_key=True)
    pidrozdil_id = Column(Integer, ForeignKey('pidrozdil.id'))
    data_naryady = Column(Date)
    required_quantity = Column(Integer)
    assigned_quantity = Column(Integer)

class Soldier(Base):
    __tablename__ = "soldier"
    id = Column(Integer, primary_key=True)
    pidrozdil_id = Column(Integer, ForeignKey('pidrozdil.id'))
    name = Column(String)
    second_name = Column(String)
    statys = Column(String)
    data_of_birth = Column(Date)
    pidrozdil_soldier = relationship('Pidrozdil', back_populates='pidrozdil')

# new = Pidrozdil(name ='Осмініг',  full_count = 3, current_count = 1)
# session.add(new)
# session.commit()
#info = session.query(Pidrozdil).filter(Pidrozdil.current_count >= 1000).all()
info = session.query(Soldier).join(Pidrozdil).all()
for i in info:
    print(f'{i.name}')
    for p in i.pidrozdil:
        print(p.name)