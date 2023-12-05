# Image Metadata and Solar Position Calculator

## Description

This repository contains Python scripts for extracting metadata from JPEG images and calculating the solar position based on the image's location and capture time. The project consists of two main components:

1. **Image Metadata Extraction:**
   - The `Image_Metadata_Extractor.py` script utilizes the Python Imaging Library (PIL) and the exifread library to extract metadata, including latitude, longitude, and capture time, from JPEG images.

2. **Solar Position Calculator:**
   - The `Solar_Position_Calculator.py` script uses the PyEphem library to calculate the solar position (azimuth and elevation) based on a given location's latitude, longitude, and a specific date and time.

## Usage

1. **Image Metadata Extraction:**
   - Ensure that the required libraries are installed by running `pip install Pillow exifread timezonefinder`.
   - Use the `Image_Metadata_Extractor` script to extract metadata from a JPEG image.
   - Example:
     ```python
     from Image_Metadata_Extractor import ImageMetadata

     jpg_file = "DSCN0010.jpg"
     sample_image = ImageMetadata(jpg_file)
     sample_image.get_exif_info()
     sample_image.convert_to_utc()

     print(f"Latitude: {sample_image.latitude}")
     print(f"Longitude: {sample_image.longitude}")
     print(f"Capture Time (UTC): {sample_image.get_formatted_utc_time()}")
     ```

2. **Solar Position Calculator:**
   - Ensure that the required libraries are installed by running `pip install ephem timezonefinder`.
   - Use the `Solar_Position_Calculator.py` script to calculate the solar position based on a given location's latitude, longitude, and a specific date and time.
   - Example:
     ```python
     from Solar_Position_Calculator import SolarPositionCalculator

     latitude = '37.565890'
     longitude = '126.975149'
     current_date = '2023/9/5 02:14:00'

     seoul = SolarPositionCalculator(latitude, longitude, current_date)
     azimuth, elevation = seoul.calculate_solar_position()

     print(f"Solar Azimuth: {azimuth} degrees")
     print(f"Solar Elevation: {elevation} degrees")
     ```

3. **Main Solar Position Calculation:**
   - The `main.py` script demonstrates the combined use of the metadata extraction and solar position calculation scripts for a given image.
   - Example:
     ```python
     from Solar_Position_Calculator import SolarPositionCalculator
     from Image_Metadata_Extractor import ImageMetadata

     jpg_file = "DSCN0010.jpg"
     sample_image = ImageMetadata(jpg_file)
     sample_image.get_exif_info()
     sample_image.convert_to_utc()

     solar_calculator = SolarPositionCalculator(sample_image.latitude, sample_image.longitude, sample_image.get_formatted_utc_time())
     azimuth, elevation = solar_calculator.calculate_solar_position()

     print(f"Solar Azimuth: {azimuth} degrees")
     print(f"Solar Elevation: {elevation} degrees")
     ```

## Dependencies

- **Image Metadata Extraction:**
  - Pillow
  - exifread
  - timezonefinder

- **Solar Position Calculator:**
  - ephem
  - timezonefinder

## License
All code and documentation in this project are available under the [MIT License](https://opensource.org/licenses/MIT).
