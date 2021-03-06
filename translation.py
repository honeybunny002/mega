import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Hello there,</b>
    
I am a <b>Mega Link Downloader</b> bot!

Just enter your mega.nz link and I will return the file/video to you!๐

๐  I can set custom captions and custom thumbnails too!

๐  I can download links which are bigger than 2GB too! ๐

Press /help for more details!

โจ <b>I am open source so you can make your own bot from here!๐</b>"""
    
    DOWNLOAD_START = "<b>Downloading to my server now ๐ฅ</b> \n\n<code>Please wait uploading will start as soon as possible๐...</code>"
    UPLOAD_START = "Uploading to Telegram now ๐ค..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using This Free Service</b>"
    SAVED_CUSTOM_THUMB_NAIL = "๐๐๐๐๐ผ๐บ ๐ง๐ต๐๐บ๐ฏ๐ป๐ฎ๐ถ๐น ๐๐ ๐ฆ๐ฎ๐๐ฒ๐ฑ. ๐ง๐ต๐ถ๐ ๐๐บ๐ฎ๐ด๐ฒ ๐ช๐ถ๐น๐น ๐๐ฒ ๐จ๐๐ฒ๐ฑ ๐๐ป ๐ฌ๐ผ๐๐ฟ ๐ก๐ฒ๐๐ ๐จ๐ฝ๐น๐ผ๐ฎ๐ฑ๐ ๐.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "๐๐๐๐๐ผ๐บ ๐ง๐ต๐๐บ๐ฏ๐ป๐ฎ๐ถ๐น ๐๐น๐ฒ๐ฎ๐ฟ๐ฒ๐ฑ ๐ฆ๐๐ฐ๐ฐ๐ฒ๐๐๐ณ๐๐น๐น๐ โ.\nYou will now get an auto generated thumbnail for your video uploads!"

    HELP_USER = f"""<b><u>๐Hi I am a Mega Link Downloader Bot.. ๐</u></b>
 
<u>How to use me:-</u>

<b>Just Send me a mega.nz file link!</b>

<b>Important:-</b> 

- Folder links are not supported.

- Your link should be valid(not expired or been removed) and should not be password protected or encrypted or private!

โ๏ธ <b>If you want a custom thumbnail for your uploads send a photo before sending the mega link!.</b> <i>(This step is Optional)</i>

๐  It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto genarated thumbnail from the video.
The thumbnail you send will be used for your next uploads!

press /deletethumbnail if you want to delete the previously saved thumbnail.
(Then the video will be uploaded with an auto-genarated thumbnail!)

โ๏ธ <b>Special feature</b> :- <i>Set caption to any file you want!</i>

๐  Select an uploaded file/video or forward me <b>Any Telegram File</b> and Just write the text you want to be on the file as a reply to the File by selecting it (as replying to a message๐) and the text you wrote will be attached as caption!๐

Ex:- <a href="https://telegra.ph/file/bdc35efc07712050bc418.jpg">Send Like This! It's Easy๐ฅณ</a>

<b>Note</b> :- You can download links which are bigger than 2GB from me too! Due to telegram API limits I can't upload files which are bigger than 2GB so I will split such files and upload them to you!

โจ <b>I am open source so you can make your own bot from here!๐</b>"""
