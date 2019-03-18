from splinter import Browser
import string
import urllib.request as request
from shutil import copyfile


def slugify(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)


with Browser('chrome') as browser:
    # Visit URL
    url = "https://models-resource.com"
    browser.visit(url)
    links = browser.find_by_css('.iconcontainer')

    for i in range(len(links)):
        browser.visit(url)
        links = browser.find_by_css('.iconcontainer')
        link = links[i]
        try:

            link.click()

            download_link = browser.find_by_text("Download this Model")
            download_link_name = slugify(browser.find_by_css("th.noborder div")[0]["title"])
            print(download_link_name)

            img = browser.find_by_css(".bigiconbody img")[0]
            img_link_url = img["src"]
            file_ending = "."+img_link_url.split(".")[-1]
            download_link.click()

            download_path = 'C:/Users/samhains/Downloads/'+download_link_name+file_ending

            request.urlretrieve(img_link_url, download_path)
        except:
            print("error next link")

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
