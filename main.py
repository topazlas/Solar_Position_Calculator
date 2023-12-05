from Image_Metadata_Extractor import *
from Solar_Position_Calculator import *

class main():
    jpg_file = "DSCN0010.jpg"
    sampleImage = ImageMetadata(jpg_file)
    sampleImage.get_exif_info()
    sampleImage.convert_to_utc()

    test01 = SolarPositionCalculator(sampleImage.latitude, sampleImage.longitude, sampleImage.get_formatted_utc_time())
    azimuth, elevation = test01.calculate_solar_position()

    print(f"방위각: {azimuth}")
    print(f"고도: {elevation}")



