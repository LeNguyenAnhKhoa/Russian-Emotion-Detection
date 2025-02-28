import re

def remove_colons(text):
    # Giữ lại các emoji :о, :/, :), :(, :3, :о
    emoji_pattern = r'(:o|:/|:\)|:\(|:3|:З|:о)'
    
    # Lưu các emoji tạm thời bằng placeholder
    temp_text = re.sub(emoji_pattern, 'EMOJI_PLACEHOLDER', text)
    
    # Xóa tất cả dấu : còn lại
    temp_text = temp_text.replace(':', ' ')
    
    # Khôi phục lại các emoji
    final_text = temp_text
    for emoji in re.finditer(emoji_pattern, text):
        final_text = final_text.replace('EMOJI_PLACEHOLDER', emoji.group(), 1)
        
    return final_text

# Thay thế dấu '/' nhưng giữ nguyên ':/' , 'о/'
def remove_gach(text):
    emoji_pattern = r'(o/|:/|о/)'
    temp_text = re.sub(emoji_pattern, 'EMOJI_PLACEHOLDER', text)
    temp_text = temp_text.replace('/', ' ')
    final_text = temp_text
    for emoji in re.finditer(emoji_pattern, text):
        final_text = final_text.replace('EMOJI_PLACEHOLDER', emoji.group(), 1)
    return final_text

# Xóa dấu '.' nhưng giữ các trường hợp ngoại lệ ._. 
def remove_cham(text):
    emoji_pattern = r'(._.)'
    temp_text = re.sub(emoji_pattern, 'EMOJI_PLACEHOLDER', text)
    temp_text = temp_text.replace('.', ' ')
    final_text = temp_text
    for emoji in re.finditer(emoji_pattern, text):
        final_text = final_text.replace('EMOJI_PLACEHOLDER', emoji.group(), 1)
    return final_text

# bỏ dấu '>' trừ trường hợp ><
def remove_lon(text):
    emoji_pattern = r'(><)'
    temp_text = re.sub(emoji_pattern, 'EMOJI_PLACEHOLDER', text)
    temp_text = temp_text.replace('>', ' ')
    final_text = temp_text
    for emoji in re.finditer(emoji_pattern, text):
        final_text = final_text.replace('EMOJI_PLACEHOLDER', emoji.group(), 1)
    return final_text

# bỏ dấu '<' trừ trường hợp ><, <3
def remove_nho(text):
    emoji_pattern = r'(><|<3)'
    temp_text = re.sub(emoji_pattern, 'EMOJI_PLACEHOLDER', text)
    temp_text = temp_text.replace('<', ' ')
    final_text = temp_text
    for emoji in re.finditer(emoji_pattern, text):
        final_text = final_text.replace('EMOJI_PLACEHOLDER', emoji.group(), 1)
    return final_text

def preprocess_russian_text(text):
    '''
    # Thay thế các từ bậy
    replacements = {
      r'Х\*Й': 'ХУЙ',
      r'Е\*АЛО': 'ЕБАЛО',
      r'C\*YA': 'CYKA',
      r'С\*КА': 'СУКА',
      r'бл\*ть': 'блять',
      r'за\*бала': 'заебала',
      r'Ж\*па': 'Жопа',
      r'Ч\*рт': 'Черт',
      r'за\*бало': 'заебало',
      r'АХИРЕЛА': 'ОФИГЕЛА',
      r'лень': 'день',
      r'убейтеВиталия': 'убейте Виталия',
      r'неожидала': 'не ожидала',
      r'УЗІ': 'УЗД'
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    text = re.sub(r'\b(шок)\b', r'\1е', text)
    #Thay thế các kí tự đặc biệt
    replacements = {
        r'❗️|❗': ' ! ',
        r'#|\xa0|…|\r|@<username>|\(c\)|\(с\)|👇|w\/': ' ',
        r':с|:{2,}\({2,}|😔|😭|😩|😞|;-\(|😥|😢|😢|😒|😫|😓|😕|😖|😌|😣|;[\(]|:-\(|:c|Q_Q|T_T|т_т|=\({1,}|:\({2,}|\({2,}|:С|╯﹏╰|†‡†': ' грусть ',
        r'с:|;D|=\*\)|☺|\*-+\*|\*_+\*|✌️|⛄️|:3|:З|=\)|:з|♪|😊|🙈|🙉|👍|😏|❤️|♥|:\*|❤|💚|♡|💖|<3|<3|😁|😚|😘|🌸|😉|✌|🆗|👏|😜|🌹|🌷|👌|💋|⌓‿⌓|🤣|😍|😝|😂|😄|😃|💐|🌺|☺️|:-?\)|:D+|;[\)]|[xXхХ][dDдД]|[xXхХ]\)|:-D|\^\^|c:|\^.\^|❄️|☀️|✨|;-?\)|:\){2,}|\){2,}|B-\)|С:|☕️|\*_\*|\^_+\^|\*-\*': ' радость ',
        r'-_+-|=_+=|-\.+-|~_+~|X_x|\.-\.|😑': ' смущенный ',
        r'😳|\b0_0\b|о\.О|О_+о|;э|Оо|о_+О|0\.о|\*О\*|С\.С|Q_+Q|¤|омг|О\.о|O_+O|О_+О|о\.о|о__ О|😆': ' сюрприз ',
        r':-/': ' расстроенный ',
        r'😱|😨': ' испуганный ',
        r'👿|😠|😡|😈': ' злой ',
        r'😶': ' отвращение ',
        r'>+<+|>+_+<+': 'смущенный'
    }
    
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)

    # Xử lý kết hợp của dấu ?, số 1 và dấu ! với khoảng cách
    text = re.sub(r'[?!1]+', lambda m: ' ?! ' if set('?!').intersection(m.group()) == {'?', '!'} else
                                      ' ! ' if '!' in m.group() else
                                      ' ? ' if '?' in m.group() else '1', text)

    text = re.sub(r'[？！1]+', lambda m: ' ？！ ' if set('？！').intersection(m.group()) == {'？', '！'} else
                                      ' ！ ' if '！' in m.group() else
                                      ' ？ ' if '？' in m.group() else '1', text)

    # gộp các chữ liền nhau
    text = re.sub(r'([^0-9])\1+', r'\1', text)
    replacements = {
      r'руский': 'русский',
      r'Дани': 'Дании',
      r'Пасажиров': 'Пассажиров',
      r'класом': 'классом',
      r'група': 'группа',
      r'офигеное': 'офигенное',
      r'беременые': 'беременные'
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Xóa các dấu
    replacements = {
      r';|"|=|%|\+|«|»|—|\||@|©|–|“|”|‘|’|。|，|一|„|•|~|✓': ' ',
      r'\-': ' ',
      r',': '',
      r'_(?!([\.x\*]|(?<=\.)\.)|(?<=X)x|(?<=\*)\*)': ' ', # bỏ dấu '_' trừ trường hợp ._. 
      r'(?<!:)\)': ' ', # Xóa dấu ')' trừ trường hợp ':)'
      r'(?<!:)\）': ' ',
      r'(?<!:)\(': ' ', # Xóa dấu '(' trừ trường hợp ':('
      r'(?<!:)\（': ' ',
      r'(?<!_)\*(?!_)': ' ', # Xóa dấu *
      #r'\bа-яА-ЯёЁa-zA-Z\b': ' ' # Xóa các chữ đứng 1 mình
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    text = remove_cham(text)
    text = remove_colons(text)
    text = remove_gach(text)
    text = remove_nho(text)
    text = remove_lon(text)
    
    # tách số ra
    text = re.sub(r'(?<![\<\:])(?<=\d)(?=\D)|(?<=\D)(?=\d)(?!3)', ' ', text)

    text = re.sub(r':\)', ' радость ', text)
    text = re.sub(r':\(', ' грусть ', text)
    text = re.sub(r':o', ' сюрприз ', text)
    text = re.sub(r'\_\.\_|\.\_\.', ' смущенный ', text)
    text = re.sub(r':/', ' расстроенный ', text)
    # Loại bỏ khoảng trắng thừa
    '''
    text = re.sub(r'\s+', ' ', text).strip()

    return text