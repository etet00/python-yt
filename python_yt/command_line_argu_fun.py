import sys
import getopt


def command_fun(inputs):
    default = inputs.copy()
    argv = sys.argv[1:]
    short_opts = "hc:s:l:"  # 當 short_opts 後面有需要承接引數時，需在後面加上冒號
    # 當 long_opts 後面有需要承接引數時，需在後面加上等號
    long_opts = "help channel_id= search_word= limit= clean_output clean_downloads".split()
    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
    except getopt.GetoptError:
        print("Lose some arguments!!")
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-c", "--channel_id"):
            inputs["channel_id"] = arg
        elif opt in ("-s", "--search_word"):
            inputs["search_word"] = arg
        elif opt in ("-l", "--limit"):
            inputs["limit"] = arg
        elif opt == "--clean_output":
            inputs["clean_output"] = False
        elif opt == "--clean_downloads":
            inputs["clean_downloads"] = True
    # check 1 處理options後面未接引數的錯誤
    if inputs["channel_id"][0] == "-" or inputs["search_word"][0] == "-" or inputs["limit"][0] == "-":
        print("Some errors in arguments!!")
        print("Apply the default value for processing")
        inputs = default
    return inputs


def print_usage():
    print("python main.py OPTIONS")
    print("OPTIONS:")
    print("{:>6} {:<20} {}".format("-h", "--help", "Print arguments usage of this project"))
    print("{:>6} {:<20} {}".format("-c", "--channel_id", "Channel ID of the Youtube channel to download"))
    print("{:>6} {:<20} {}".format("-s", "--search_word", "The key word that you want to capture in videos"))
    print("{:>6} {:<20} {}".format("-l", "--limit", "The maximum number of capture videos in the output video"))
    print("{:>6} {:<20} {}".format("", "--clean_output", "Remove previous output video"))
    print("{:>6} {:<20} {}".format("", "--clean_downloads", "Remove downloaded subtitle files and videos during running"))
