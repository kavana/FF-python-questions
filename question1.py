class store_items:
    def __init__(self, items=None):
        if items is None:
            self.item_list = []
        else:
            self.item_list = [item for item in items]

    def get_unique_items(self):
        return list(set(self.item_list))

    def get_frequency(self):
        return {item : self.item_list.count(item) for item in set(self.item_list)}

    def append_item(self, item):
        self.item_list.append(item)
        return "append successful"

if __name__ == "__main__":
    store_items1 = store_items([1, 2, 3, 4, 1])
    print store_items1.get_unique_items()
    print store_items1.get_frequency()
    print store_items1.append_item(4)
    print store_items1.get_unique_items()
    print store_items1.get_frequency()