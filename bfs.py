from queue import Queue

result = Queue()
glo_queue = Queue()

def breadth_first_search(dictionary, vertex):
    result.queue(vertex)
    glo_queue.queue(vertex)
    while glo_queue.show_queue() != []:
        pivot = glo_queue.get_item()
        if pivot in dictionary.keys():
            while dictionary[pivot] != []:
                glo_queue.queue(min(dictionary[pivot]))
                result.queue(min(dictionary[pivot]))
                dictionary[pivot].remove((min(dictionary[pivot])))
        glo_queue.dequeue()

def read_file():
    dic = {}
    with open('arcs.txt','r+') as ofs:
        str1 = ofs.readlines()
        for arc in str1:
            temp = arc.split("->")
            first_ele = temp[0].strip()
            second_ele = temp[-1].strip()
            if first_ele in dic:
                temp_list = dic[first_ele]
                temp_list.append(second_ele)
                dic[first_ele] = temp_list
            else:
                dic[first_ele] = [second_ele]
    # Start point
    breadth_first_search(dic, "S")
    print result.show_queue()[::-1]
    

def main():
    read_file()

if __name__ == "__main__":
    main()