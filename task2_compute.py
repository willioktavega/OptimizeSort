import os

def set_or_get_tmp(out_file):
    # split path and filename
    split_path_files = os.path.split(os.path.abspath(out_file))
    tmp_merge = "{path}/tmp".format(path=split_path_files[0])
    if not os.path.exists(tmp_merge):
        os.makedirs(tmp_merge)

    return tmp_merge


def mapping(in_file, out_file):
    tmp_merge = set_or_get_tmp(out_file)

    # each number put in its file with has same name
    # ex: number 1 put in file with name 1.txt
    with open(in_file, 'r') as f_in:
        for each in f_in:
            if int(each) < 10:
                with open("{path}/0{part}.txt".format(path=tmp_merge, part=each.strip()), 'ab') as f_out:
                    f_out.write(each.strip())
                    f_out.write('\n')
            else:
                with open("{path}/{part}.txt".format(path=tmp_merge, part=each.strip()), 'ab') as f_out:
                    f_out.write(each.strip())
                    f_out.write('\n')

def compute_sort(out_file):
    tmp_merge = set_or_get_tmp(out_file)
    list_tmp_merge = os.listdir(tmp_merge)

    # merge all temporary file and sort by name file
    with open(out_file, 'w') as f_merge:
        for file in sorted(list_tmp_merge):
            with open('{path}/{name}'.format(path=tmp_merge, name=file), 'rb') as f_tmp:
                for number in f_tmp:
                    f_merge.write(number)

def remove_tmp(out_file):
    tmp_merge = set_or_get_tmp(out_file)
    list_tmp_merge = os.listdir(tmp_merge)

    # remove temporary directory / files
    try:
        for file in list_tmp_merge:
            os.remove('{path}/{name}'.format(path=tmp_merge, name=file))

        os.rmdir(tmp_merge)
    except Exception:
        pass

# if __name__ == '__main__':
#     mapping('input/test.txt', 'output/merge.txt')
#     compute_sort('output/merge.txt')
#     remove_tmp('output/merge.txt')