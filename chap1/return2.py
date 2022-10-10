def make_juice(fruit):
    return f"{fruit}+🥃" #이모티콘(이모지)은 윈도우+ ; . 을 누르면 된다

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🧂"


juice = make_juice("🍓") # 
cold_juice = add_ice(juice)
sweet_juice = add_sugar(cold_juice)
print(sweet_juice)
