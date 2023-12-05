import ephem
import math

#태양위치계산 클래스
class SolarPositionCalculator:
    #위도, 경도, 시간을 입력받아 객체 생성
    def __init__(self, latitude, longitude, date):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.observer = self.create_observer()

    #observer 객체 생성
    def create_observer(self):
        observer = ephem.Observer()
        observer.lat = str(self.latitude)
        observer.long = str(self.longitude)
        observer.date = self.date
        return observer

    #입력된 정보로 태양의 방위각, 고도를 계산해주는 메서드
    def calculate_solar_position(self):
        sun = ephem.Sun(self.observer)

        azimuth = math.degrees(sun.az)
        elevation = math.degrees(sun.alt)

        return azimuth, elevation




if __name__ == "__main__":
    # 예시 데이터를 사용하여 객체를 생성하고 태양의 위치 계산
    latitude = '37.565890'
    longitude = '126.975149'
    current_date = '2023/9/5 02:14:00'

    seoul = SolarPositionCalculator(latitude, longitude, current_date)
    azimuth, elevation = seoul.calculate_solar_position()

    print(f"태양의 방위각 (Azimuth): {azimuth} 도")
    print(f"태양의 고도 (Elevation): {elevation} 도")
