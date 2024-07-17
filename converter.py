from colorama import Fore, Style
import time

def process_tokens():
    try:
        with open("tokens.txt", "r") as file:
            tokens = file.readlines()
            print(f"{Fore.YELLOW}Started!{Style.RESET_ALL}")
            start_time = time.time()
            with open("tokens.txt", "w") as rewrite_tokens_file:
                for token in tokens:
                    cut_token = token.split(":")[2].strip()
                    print(f"{Fore.GREEN}Success! {Style.RESET_ALL}Token: {Fore.BLUE}{cut_token}{Style.RESET_ALL}")
                    rewrite_tokens_file.write(f"{cut_token}\n")
            elapsed_time = time.time() - start_time
            print(f"{Fore.YELLOW}Finished in {elapsed_time:.2f} seconds. {Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED} Error occurred: {e} {Style.RESET_ALL}")

if __name__ == "__main__":
    process_tokens()
