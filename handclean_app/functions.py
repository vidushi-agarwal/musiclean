import cloudinary
from cloudinary.uploader import upload
import cloudinary.api


def upload_to_cloudinary(imagestr):
    cloudinary.config( cloud_name = "dlfssqpay", api_key = "216762747948992", api_secret = "ZjAMLJdFyewub6cquX7ipRhriwQ")
    x = upload(imagestr)
    return x


