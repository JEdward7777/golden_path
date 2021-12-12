import argparse


import REST.f9_data_source

parser = argparse.ArgumentParser(description='Run different components.')

#parser.add_argument('--f9_data_abstraction',  action='store_true', help="Run REST API for data abstraction")
parser.add_argument('--f9_data_abstraction',  nargs='?', default=False, const=1, help="Run REST API for data abstraction.  Specify datasource [1], 2 or 3.")


if __name__ == '__main__':
    args = parser.parse_args()


    if args.f9_data_abstraction:
        print( f"doing abstraction for number {args.f9_data_abstraction}" )

        REST.f9_data_source.run(args.f9_data_abstraction)

