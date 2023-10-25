from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json
import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

engine = create_engine(f'postgresql://{user}:{password}@{db_host}/{db_name}')


Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    genre = Column(String)
    main = Column(String)
    price_per_person = Column(Integer)
    opening_hours = Column(String)
    regular_holiday = Column(String)
    hp_links = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    comment = Column(String)
    image_object_name = Column(String)


class RestaurantCRUD():
    engine = ""
    session = ""
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:postgres@uecinformal_db/uecinformal")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self,name,genre,main,price_per_person,opening_hours,regular_holiday,hp_links,longitude,latitude,comment,image_object_name):
        new_restaurant = Restaurant(
            name = name,
            genre = genre,
            main = main,
            price_per_person = price_per_person,
            opening_hours = opening_hours,
            regular_holiday = regular_holiday,
            hp_links = hp_links,
            longitude = longitude,
            latitude = latitude,
            comment = comment,
            image_object_name = image_object_name,
        )
        self.session.add(new_restaurant)
        self.session.commit()
        self.session.close()

    def read_all(self):
        restaurants = self.session.query(Restaurant).all()
        result = []
        for restaurant in restaurants:
            result.append({
                'name': restaurant.name,
                'genre': restaurant.genre,
                'main' : restaurant.main,
                'price_per_person': restaurant.price_per_person,
                'opening_hours': restaurant.opening_hours,
                'regular_holiday': restaurant.regular_holiday,
                'hp_links': restaurant.hp_links,
                'longitude': restaurant.longitude,
                'latitude': restaurant.latitude,
                'comment': restaurant.comment,
                'image_object_name': restaurant.image_object_name,
            })

        return result
        # print(type(restaurants))
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    restaurantCRUD = RestaurantCRUD()
    restaurantCRUD.insert("そらまめらぁめん本舗","ラーメン","タンタンメン",1000,"11:30~24:00","","",35.65250,139.54523,"電気通信大学ソフトテニス部御用達。特大盛無料なので、食べ盛りに","")
    restaurantCRUD.insert("食神 餃子王","中華料理","日替わり定食",700,"11:30~15:00,17:00~23:00","2.4日","http://shokujinhp.web.fc2.com/",35.655804,139.542085,"電通大生御用達。安い、うまい、多い。三拍子そろった中華料理屋","")
    restaurantCRUD.insert("鯉寿司","寿司","ランチちらし",1000,"11:00~14:30,16:00~22:00","水","https://www.koisushi.co.jp/index.html",35.658046,139.540147,"11:00~14:00のランチメニューが学生の財布にも優しいお値段","")
    # test = restaurantCRUD.read_all()