from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder

class ImageMetadata:
    def __init__(self, image_path):
        self.image_path = image_path
        self.latitude = None
        self.longitude = None
        self.timezone = None
        self.utc_time = None

    def get_exif_info(self):
        #예외처리
        try:
            # 이미지 열기
            img = Image.open(self.image_path)

            # 이미지의 EXIF 데이터 읽기
            exif_data = img._getexif()

            # 필요한 정보 추출
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    gps_info = {GPSTAGS.get(key, key): value[key] for key in value}
                    latitude = gps_info.get('GPSLatitude')
                    longitude = gps_info.get('GPSLongitude')
                    if latitude and longitude:
                        self.latitude = float(latitude[0]) + float(latitude[1]) / 60 + float(latitude[2]) / 3600 #도분초 -> 좌표(도)
                        self.longitude = float(longitude[0]) + float(longitude[1]) / 60 + float(longitude[2]) / 3600 #도분초 -> 좌표(도)
                elif tag_name == 'DateTimeOriginal':
                    self.timezone = datetime.strptime(value, '%Y:%m:%d %H:%M:%S') #문자열로 된 날짜와 시간 정보를 파싱하여 Python의 datetime 객체로 변환

        except Exception as e:
            print(f"Error: {e}")

    def convert_to_utc(self):
        try:
            if self.latitude is None or self.longitude is None or self.timezone is None:
                print('EXIF 정보를 읽을 수 없거나 필요한 정보가 없습니다.')
                return

            tf = TimezoneFinder()
            timezone_str = tf.timezone_at(lng=self.longitude, lat=self.latitude) #예를 들어, self.longitude가 경도 값 -73.9857이고 self.latitude가 위도 값 40.748817인 경우, timezone_str 변수에 해당 지역의 시간대 문자열 (예: 'America/New_York')이 저장

            if timezone_str:
                timezone = pytz.timezone(timezone_str) #시간대 문자열(timezone_str)을 사용하여 pytz.timezone() 함수를 호출하여 해당 지역의 시간대(timezone)를 얻습니다.
                print(timezone)
                localized_time = timezone.localize(self.timezone)
                print(localized_time)
                self.utc_time = localized_time.astimezone(pytz.utc)
            else:
                print('시간대 정보를 찾을 수 없습니다.')
        except Exception as e:
            print(f"Error: {e}")

    def get_formatted_utc_time(self, format_str="%Y/%m/%d %H:%M:%S"):
        if self.utc_time:
            return self.utc_time.strftime(format_str)
        else:
            return None


#Test
if __name__ == "__main__":
    try:
        image_path = "DSCN0010.jpg"

        extractor = ImageMetadata(image_path)
        extractor.get_exif_info()
        extractor.convert_to_utc()

        print(f'위도: {extractor.latitude}, 경도: {extractor.longitude}')
        print(f'사진 촬영 시간 (지역 시간대): {extractor.timezone}')
        print(f'사진 촬영 시간 (UTC 시간대): {extractor.get_formatted_utc_time()}')
    except Exception as e:
        print(f"Error: {e}")
