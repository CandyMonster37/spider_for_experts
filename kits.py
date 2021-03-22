def usage_example():
    exp_lis = get_experts()
    for item in exp_lis:
        expert, info = get_info(item)
        if expert is None:
            continue
        else:
            print('do something you want to do')


def get_experts():
    """
    :return: names of all experts, list consists of strs
    """
    import os

    experts = os.listdir('./data/info')
    return experts


def get_info(expert):
    """
    :return: expert: the name of the experts, str
             info: expert's papers with details, list consists of dics

             You can combine these to returned values into an item of a key
             or something you want
    """
    import os
    from utils import load_file

    if os.path.exists('./data/info/' + expert):
        info = load_file('./data/info/' + expert)
        return expert, info
    else:
        print('no such expert!')
        return None, None
