from time import *
from selenium import webdriver as w 

videos = open('C:\\path\\to\\link.txt')
list = videos.readlines()

NUM_OF_TAB = 4
NUM_OF_VID = len(list)

vid_index = 0
tab_index = 0
count = 1

brow = w.Chrome('C:\\path\\chromedriver.exe')
brow.get(list[vid_index])

sleep(1)
play = brow.find_element_by_css_selector('#movie_player > div.ytp-cued-thumbnail-overlay > button')
play.click()

while 1:
    vid_index = (vid_index + 1) % NUM_OF_VID
    tab_index = (tab_index + 1) % NUM_OF_TAB

    if count < NUM_OF_TAB:
        count += 1
        brow.execute_script("window.open('"+list[vid_index].strip()+"')")
    else:
        brow.switch_to.window(brow.window_handles[tab_index])
        sleep(2)
        brow.get(list[vid_index])

    sleep(30)
