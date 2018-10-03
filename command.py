import argparse
import task2_compute as prc
import task2_create_file as cr
import time

parser = argparse.ArgumentParser()
parser.add_argument('type', help='type can be [create/sort]')
create_data = parser.add_argument_group('create')
create_data.add_argument('--output', '-o', nargs=1, help='store data to specific path')
create_data.add_argument('--amount', '-a', nargs=1, help='amount of age data')
sort_data = parser.add_argument_group('sort')
sort_data.add_argument('--input-file', '-if', nargs=1, help='path input file')
sort_data.add_argument('--output-file', '-of', nargs=1, help='path output file')

args = parser.parse_args()

if args.type == 'create' and args.output != None and args.amount != None:
    cr.create_file(args.output[0], int(args.amount[0]))
    print('create completed')
elif args.type == 'create' and (args.output == None or args.amount == None):
    parser.print_help()
elif args.type == 'sort' and args.input_file != None and args.output_file != None:
    start_time = time.time()
    prc.mapping(args.input_file[0], args.output_file[0])
    prc.compute_sort(args.output_file[0])
    prc.remove_tmp(args.output_file[0])
    print("--- running process %s seconds ---" % (time.time() - start_time))
elif args.type == 'sort' and (args.input_file == None or args.output_file == None):
    parser.print_help()
elif args.type != 'create' or args.type != 'sort':
    parser.print_help()
