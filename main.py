import keyboard,time,pyautogui,pyperclip
running = False
program = True

WIDTH, HEIGHT = pyautogui.size()
sell_string = '50K'
sell_slot = [1024,160]
confirm_slot = [1058, 159]
done_slot = [1021, 268]
craftgrid_slot = [1058,157]
craftresult_slot = [1096,149]
inventory_coordinates = [[[949, 208], [970, 208], [987, 207], [1004, 207], [1024, 208], [1041, 208], [1059, 209], [1077, 208], 
                         [1094, 209], [951, 224], [970, 224], [988, 224], [1004, 224], [1021, 224], [1041, 224], [1057, 223], 
                         [1075, 226], [1095, 226], [951, 245], [969, 241], [987, 240], [1005, 241], [1023, 240], [1041, 241], 
                         [1059, 241], [1076, 241], [1096, 241], [949, 262], [970, 262], [989, 261], [1005, 262], [1022, 262], 
                         [1042, 262], [1060, 263], [1077,263], [1096, 262]], [[952, 205], [970, 205], [988, 207], [1006, 207], 
                                                                               [1024, 208], [1042, 207], [1060, 207], [1078, 206], 
                                                                               [1095, 206], [951, 224], [969, 223], [988, 224], 
                                                                               [1006, 224], [1024, 223], [1043, 223], [1060, 222], 
                                                                               [1079, 223], [1097, 223], [949, 240], [970, 240], 
                                                                               [987, 242], [1006, 242], [1022, 242], [1041, 242], 
                                                                               [1061, 242], [1080, 242], [1096, 242], [951, 261], 
                                                                               [971, 264], [988, 264], [1005, 262], [1022, 262], 
                                                                               [1043, 263], [1060, 262], [1074, 262], [1094, 262]]]
your_item_coordinates = [1060,204]
auction_coordinates = [[952, 139], [972, 141], [987, 141], [1008, 143], [1024, 140], [1046, 138], [1056, 140], [1079, 142], 
                       [1092, 138], [951, 157], [969, 157], [989, 160], [1004, 161], [1023, 161], [1037, 161], [1060, 157], 
                       [1078, 157], [1093, 160], [951, 177], [966, 174], [986, 177], [1004, 176], [1023, 174], [1042, 174], 
                       [1057, 174], [1074, 175]]

def getMousePos():
    curX, curY = pyautogui.position()
    r,g,b = pyautogui.pixel(curX,curY)
    print(curX,curY, r,g,b)

def toggle_run():
    pyperclip.copy(sell_string)
    global running
    running = not running

def force_exit():
    print('Exiting')
    quit()

def scan_sell_button():
    for item in auction_coordinates:
        time.sleep(0.2)
        curX,curY = item
        pyautogui.moveTo(curX,curY,0.1,0.1)
        if pyautogui.pixelMatchesColor(curX,curY,[32,195,92],30):
            return auction_coordinates.index(item)
    return False

def find_item(inv, itm):
    item_indeces = []
    # Change pixel color to detect
    if itm == 0:
        color = [252,105,32]
    if itm == 1:
        color = [186,32,252]

    for item in inventory_coordinates[inv]:
        curX,curY = item
        pyautogui.moveTo(curX,curY,0.1,0.1)
        time.sleep(0.2)
        if pyautogui.pixelMatchesColor(curX,curY,color,70):
            item_indeces.append(inventory_coordinates[inv].index(item))

    return item_indeces

def go_auctionsell_gui():
    pyautogui.keyDown('altleft')
    time.sleep(0.2)
    pyautogui.keyUp('altleft')
    time.sleep(0.1)
    x,y = your_item_coordinates
    pyautogui.moveTo(x,y,0.1,0.1)
    pyautogui.leftClick()
    time.sleep(0.6)

def close_auctionsell_gui():
    time.sleep(0.2)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')

def check_eligible():
    eligibility = False
    go_auctionsell_gui()
    sell_index = scan_sell_button()
    print(sell_index)
    if sell_index < 17:
        eligibility = True
    close_auctionsell_gui()
    return eligibility

keyboard.add_hotkey('x', toggle_run)
keyboard.add_hotkey('z', getMousePos)
keyboard.add_hotkey('j', force_exit)

while program:
    if running:
        if check_eligible():
            go_auctionsell_gui()
            item_indeces = find_item(1,1)
            if not item_indeces:
                print('No more planks')
                close_auctionsell_gui()
                time.sleep(0.1)
                pyautogui.press('e')
                time.sleep(0.2)
                item_indeces = find_item(0,0)
                if not item_indeces:
                    print('No more oak logs as well')
                    pyautogui.press('e')
                    program = False
                else:
                    time.sleep(0.1)
                    time.sleep(0.3)
                    logx,logy = inventory_coordinates[0][item_indeces[0]]
                    pyautogui.moveTo(logx,logy,0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(0.1)
                    pyautogui.moveTo(craftgrid_slot[0], craftgrid_slot[1], 0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(0.5)
                    pyautogui.moveTo(craftresult_slot[0], craftresult_slot[1], 0.1,0.1)
                    pyautogui.keyDown('shift')
                    pyautogui.leftClick()
                    pyautogui.keyUp('shift')
                    time.sleep(0.2)
                    pyautogui.press('esc')
            else:
                time.sleep(1)
                for i in item_indeces:
                    time.sleep(1.5)
                    sell_index = scan_sell_button()
                    sellx,selly = auction_coordinates[sell_index]
                    pyautogui.moveTo(sellx,selly,0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(1)
                    x,y = inventory_coordinates[1][i]
                    pyautogui.moveTo(x,y-19,0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(0.2)
                    pyautogui.moveTo(sell_slot[0],sell_slot[1],0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(0.2)
                    pyautogui.moveTo(confirm_slot[0],confirm_slot[1],0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','v')
                    time.sleep(0.3)
                    pyautogui.moveTo(done_slot[0],done_slot[1],0.1,0.1)
                    pyautogui.leftClick()
                    time.sleep(1)
                    time.sleep(0.2)
                    pyautogui.moveTo(confirm_slot[0],confirm_slot[1],0.1,0.1)
                    pyautogui.leftClick()
                    go_auctionsell_gui()
                close_auctionsell_gui()
        time.sleep(60)