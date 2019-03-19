from splinter import Browser
import string
import shutil
import urllib.request as request

import os, zipfile
from shutil import copyfile

def get_urls():
    urlfile = open("urls_part_1.txt", 'r')
    return [line.rstrip() for line in urlfile.readlines()]


def slugify(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)

def scrape_page():
    with Browser('chrome') as browser:
        # Visit URL
        urls = get_urls()
        root_path = 'C:/Users/samhains/Downloads/'
        sub_path = "HUMAN"
        for url in urls:
            if not url.startswith("http"):

                if sub_path != "":
                    files = os.listdir(root_path)
                    for f in files:
                        if not os.path.isdir(f):
                            shutil.move(root_path+f, root_path+sub_path)
                sub_path = url
                files = os.listdir(root_path)

                if not os.path.exists(root_path+sub_path):
                    print("path doesn't exist. trying to make")
                    os.makedirs(root_path+sub_path)
                    continue

            else:
                browser.visit(url)
                try:
                    download_link = browser.find_by_text("Download this Model")
                    download_link_name = slugify(browser.find_by_css("th.noborder div")[0]["title"])
                    print(download_link_name)

                    img = browser.find_by_css(".bigiconbody img")[0]
                    img_link_url = img["src"]
                    file_ending = "."+img_link_url.split(".")[-1]
                    download_link.click()

                    download_path = root_path+sub_path+"/"+download_link_name+file_ending

                    request.urlretrieve(img_link_url, download_path)
                except Exception as e:
                    print(e)

scrape_page()
# dir_name = 'C:/Users/samhains/Downloads/'
# extension = ".zip"
#
# os.chdir(dir_name) # change directory from working dir to dir with files
#
# for item in os.listdir(dir_name): # loop through items in dir
#     if item.endswith(extension): # check for ".zip" extension
#         file_name = os.path.abspath(item) # get full path of files
#         zip_ref = zipfile.ZipFile(file_name) # create zipfile object
#         zip_ref.extractall(dir_name) # extract file to dir
#         zip_ref.close() # close file
#         # os.remove(file_name) # delete zipped file
    # old_file_name = download_path+'old_file_name'
    # new_file_name = download_path+'new_file_name'
    # copyfile(old_file_name, new_file_name)


    # browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    # button = browser.find_by_name('btnG')
    # Interact with elements
    # button.click()
    # if browser.is_text_present('splinter.readthedocs.io'):
    #     print("Yes, the official website was found!")
    # else:
    #     print("No, it wasn't found... We need to improve our SEO techniques")
