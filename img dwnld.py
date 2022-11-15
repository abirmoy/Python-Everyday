#https://www.slideshare.net/shantypath/24398947-strategicmanagementfinalnotes
# https://stackoverflow.com/questions/30229231/python-save-image-from-url
import urllib.request

page_num = 309
last_page = 638


# urllib.request.urlretrieve(imgURL, f"C:\\Users\\nabir\OneDrive\\Desktop\\New folder\\New folder\\{page_num}.jpg")
for i in range (page_num, last_page):
    # print(page_num)
    imgURL = f"https://image.slidesharecdn.com/24398947-strategic-management-final-notes-110104211134-phpapp02/85/24398947-strategicmanagementfinalnotes-{page_num}-638.jpg?cb=166689146767"
    urllib.request.urlretrieve(imgURL, f"C:\\Users\\nabir\OneDrive\\Desktop\\New folder\\New folder\\{page_num}.jpg")
    print(f'Downloading {page_num}th Page of the slide')
    page_num += 1
    print('Next Page:', page_num)
    i = page_num
    

